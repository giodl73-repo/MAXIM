# genomics/ — Status

## Files

| File | Topic | Status |
|------|-------|--------|
| 00-OVERVIEW.md | Landscape: from Sanger to short-read to long-read; the bioinformatics stack; genomics vs. transcriptomics vs. epigenomics | 🔜 |
| 01-SEQUENCING-TECH.md | Sanger sequencing, Illumina (bridge PCR/SBS), Oxford Nanopore, PacBio HiFi, single-cell 10x, spatial transcriptomics | 🔜 |
| 02-GENOME-ASSEMBLY.md | Overlap-Layout-Consensus, de Bruijn graphs, reference-guided assembly, phasing, telomere-to-telomere | 🔜 |
| 03-VARIANT-CALLING.md | SNPs, indels, CNVs, SVs; GATK HaplotypeCaller pipeline; population genomics (1000 Genomes/gnomAD) | 🔜 |
| 04-GENE-EXPRESSION.md | RNA-seq library prep, alignment (STAR/HISAT2), quantification (kallisto/salmon), DESeq2/edgeR differential expression | 🔜 |
| 05-EPIGENOMICS.md | DNA methylation (bisulfite-seq), histone ChIP-seq, ATAC-seq chromatin accessibility, Hi-C 3D genome organization | 🔜 |
| 06-GWAS.md | Linkage disequilibrium, population stratification, Manhattan plots, polygenic risk scores, Mendelian randomization | 🔜 |
| 07-CRISPR.md | Cas9 PAM/guide RNA mechanism, delivery (AAV/LNP), base editing, prime editing, CRISPRi/CRISPRa, off-target analysis | 🔜 |
| 08-BIOINFORMATICS-PIPELINE.md | File formats (FASTQ/BAM/VCF/BED), workflow systems (Snakemake/Nextflow/WDL), cloud (Terra/DNAnexus), databases (Ensembl/UCSC/dbSNP) | 🔜 |
| 09-PERSONALIZED-MEDICINE.md | Pharmacogenomics (CYP450), somatic cancer genomics, rare disease diagnosis (exome/genome), liquid biopsy (ctDNA) | 🔜 |

## Coverage Notes

The molecular biology of the genome at scale. Distinct from biology/ (cell/evolution fundamentals) and natural-sciences/ (molecular biology chapter) — this directory covers the technology-driven field that emerged from HGP. Heavy bioinformatics component bridges to computing/ and data-science/. Connects to medicine/ (personalized medicine), immunology/ (immune repertoire sequencing), and microbiology/ (metagenomics). The pipeline file will resonate with the learner's Azure Data Factory and CI/CD background — genomics workflows are the data engineering of biology.
