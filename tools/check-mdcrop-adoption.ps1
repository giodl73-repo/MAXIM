[CmdletBinding()]
param(
  [string]$ProviderPath
)

$ErrorActionPreference = "Stop"
$ProviderPath = if ($ProviderPath) {
  $ProviderPath
} else {
  Join-Path $PSScriptRoot "..\..\..\tools-infra\mdcrop"
}
$repoRoot = Split-Path $PSScriptRoot -Parent
$manifestPath = Join-Path $repoRoot "docs\dependencies\mdcrop.json"
$manifest = Get-Content $manifestPath -Raw | ConvertFrom-Json
$provider = (Resolve-Path $ProviderPath).Path

$providerHead = (& git -C $provider rev-parse HEAD).Trim()
if ($LASTEXITCODE -ne 0) {
  throw "Unable to read MDCROP revision from '$provider'."
}
if ($providerHead -ne $manifest.provider.revision) {
  throw "MDCROP checkout '$providerHead' does not match pinned revision '$($manifest.provider.revision)'."
}

$workspaceManifest = Get-Content (Join-Path $provider "Cargo.toml") -Raw
$declaredVersion = [regex]::Match(
  $workspaceManifest,
  '(?m)^\s*version\s*=\s*"([^"]+)"'
).Groups[1].Value
if ($declaredVersion -ne $manifest.provider.version) {
  throw "MDCROP version '$declaredVersion' does not match '$($manifest.provider.version)'."
}

$trackedViews = @(& git -C $repoRoot ls-files ".mdcrop/views/*.json")
if ($LASTEXITCODE -ne 0) {
  throw "Unable to enumerate tracked MAXIM views."
}
if ($trackedViews.Count -lt $manifest.usage.minimumTrackedViewCount) {
  throw "Expected at least $($manifest.usage.minimumTrackedViewCount) tracked views; found $($trackedViews.Count)."
}

foreach ($proofView in $manifest.consumerProof.views) {
  $viewPath = Join-Path $repoRoot $proofView.path
  $stdout = & cargo run --offline --quiet --manifest-path (Join-Path $provider "Cargo.toml") -- `
    view --inspect --file $viewPath
  if ($LASTEXITCODE -ne 0) {
    throw "MDCROP rejected '$($proofView.path)'."
  }
  $inspection = ($stdout -join "`n") | ConvertFrom-Json
  if ($inspection.schema_version -ne "mdcrop.view-inspect.v1") {
    throw "Unexpected inspection schema '$($inspection.schema_version)' for '$($proofView.path)'."
  }
  if ($inspection.supported_source_count -ne $proofView.expectedSupportedSourceCount) {
    throw "Expected $($proofView.expectedSupportedSourceCount) supported sources for '$($proofView.path)'; found $($inspection.supported_source_count)."
  }
}

Write-Output "MAXIM MDCROP adoption proof passed for $($manifest.consumerProof.views.Count) views."
