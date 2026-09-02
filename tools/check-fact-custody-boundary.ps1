$ErrorActionPreference = "Stop"

function Assert-Contains {
    param(
        [string]$Path,
        [string]$Needle
    )

    $text = Get-Content -Raw -Path $Path
    if ($text.IndexOf($Needle, [StringComparison]::Ordinal) -lt 0) {
        throw "$Path is missing required text: $Needle"
    }
}

$root = Split-Path -Parent $PSScriptRoot

$checks = @(
    @{
        Path = "README.md"
        Needles = @(
            "Specific-fact custody gate",
            "number, proper noun, date,",
            "fact-custody boundary",
            "MAXIM-PF-02"
        )
    },
    @{
        Path = "docs/adoption/fact-custody-boundary.md"
        Needles = @(
            'This boundary closes `MAXIM-PF-02`',
            "guide path and exact claim",
            "Reference Integrity Auditor review",
            "If any field is missing, the guide is a research lead"
        )
    },
    @{
        Path = "docs/adoption/reuse-boundary.md"
        Needles = @(
            "Specific facts have a stricter custody gate",
            "supporting audit",
            "fact-custody-boundary.md"
        )
    },
    @{
        Path = ".pitfall/maxim-pitfalls.md"
        Needles = @(
            "## MAXIM-PF-02",
            "**Status:** MITIGATED",
            "guide path, exact claim",
            "tools/check-fact-custody-boundary.ps1"
        )
    },
    @{
        Path = ".pitfall/maxim-invariants.md"
        Needles = @(
            "## MAXIM-I-06",
            "Specific Facts Require Custody Before Reuse",
            "supporting audit or fact-check wave",
            "tools/check-fact-custody-boundary.ps1"
        )
    },
    @{
        Path = ".roles/ROLE.md"
        Needles = @(
            "## PITFALL gates",
            '`MAXIM-PF-02` specific-fact custody',
            "Reference Integrity Auditor; Executable Evidence Auditor; Learner Advocate; Reader Path Editor"
        )
    },
    @{
        Path = ".roles/parliament/reference-integrity-auditor.md"
        Needles = @(
            "Numbers, proper nouns, dates, formulas, standards, versions",
            "source-first custody"
        )
    },
    @{
        Path = "context/audits/2026-06-27-honest-gap-audit.md"
        Needles = @(
            "Factual accuracy: confident confabulation",
            "number, name, or formula"
        )
    },
    @{
        Path = "context/audits/2026-07-29-ks-fact-and-rescore.md"
        Needles = @(
            "Fact fixes",
            "Library-wide numbers/proper-nouns fact-check"
        )
    }
)

foreach ($check in $checks) {
    $path = Join-Path $root $check.Path
    if (-not (Test-Path -Path $path)) {
        throw "Missing required file: $($check.Path)"
    }
    foreach ($needle in $check.Needles) {
        Assert-Contains -Path $path -Needle $needle
    }
}

Write-Output "MAXIM fact-custody boundary check passed."
