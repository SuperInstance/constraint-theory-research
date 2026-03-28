# Supplementary Material Checklist

**Version:** 1.0
**Last Updated:** 2025-03-16
**Status:** Active

---

## 1. Overview

This checklist ensures all supplementary materials are complete and properly prepared for academic paper submissions.

---

## 2. Required Supplementary Materials

### 2.1 Code Repository

| Item | Requirement | Status |
|------|-------------|--------|
| GitHub repository | Public URL provided | [ ] |
| README.md | Complete documentation | [ ] |
| Installation guide | Step-by-step instructions | [ ] |
| Usage examples | At least 3 examples | [ ] |
| Test suite | All tests passing | [ ] |
| License file | MIT or specified license | [ ] |
| Citation file | CITATION.cff or equivalent | [ ] |
| DOI | Zenodo DOI for version | [ ] |

**Repository Structure:**
```
constraint-theory/
├── README.md
├── LICENSE
├── CITATION.cff
├── docs/
│   ├── INSTALLATION.md
│   ├── API_REFERENCE.md
│   └── EXAMPLES.md
├── src/
│   ├── core/
│   ├── gpu/
│   └── api/
├── tests/
│   ├── unit/
│   └── integration/
├── benchmarks/
│   ├── scripts/
│   └── results/
└── data/
    └── sample/
```

### 2.2 Data Files

| Item | Requirement | Status |
|------|-------------|--------|
| Raw data | CSV/JSON format | [ ] |
| Processed data | Ready for analysis | [ ] |
| Data dictionary | Variable descriptions | [ ] |
| Sample data | Small example dataset | [ ] |
| Data license | Usage terms specified | [ ] |

**Data Organization:**
```
data/
├── raw/
│   ├── experiment1_raw.csv
│   └── experiment2_raw.csv
├── processed/
│   ├── experiment1_processed.csv
│   └── experiment2_processed.csv
├── sample/
│   └── small_sample.csv
└── DATA_DICTIONARY.md
```

### 2.3 Extended Proofs

| Item | Requirement | Status |
|------|-------------|--------|
| Complete proofs | All theorems proved | [ ] |
| Lemmas | Supporting statements | [ ] |
| Derivations | Step-by-step | [ ] |
| Alternative proofs | If applicable | [ ] |

**Proof Document Structure:**
```markdown
# Supplementary: Mathematical Proofs

## Appendix A: Theorem Proofs

### Theorem 1: [Title]
**Statement:** [Formal statement]
**Proof:** [Complete proof]

### Lemma A.1: [Title]
**Statement:** [Formal statement]
**Proof:** [Complete proof]

## Appendix B: Derivations

### Derivation of Equation X
[Step-by-step derivation]
```

### 2.4 Additional Experiments

| Item | Requirement | Status |
|------|-------------|--------|
| Ablation studies | Component analysis | [ ] |
| Sensitivity analysis | Parameter variations | [ ] |
| Extended results | Additional benchmarks | [ ] |
| Failure cases | Negative results | [ ] |
| Statistical details | Full test results | [ ] |

### 2.5 Implementation Details

| Item | Requirement | Status |
|------|-------------|--------|
| Hyperparameters | All values listed | [ ] |
| Hardware specs | CPU, GPU, RAM | [ ] |
| Software versions | All dependencies | [ ] |
| Random seeds | For reproducibility | [ ] |
| Training time | Wall-clock duration | [ ] |
| Memory usage | Peak consumption | [ ] |

**Implementation Document:**
```markdown
# Supplementary: Implementation Details

## Hardware Configuration
- CPU: [Model, cores, clock speed]
- GPU: [Model, memory]
- RAM: [Size, type]
- Storage: [Type, size]

## Software Environment
- OS: [Version]
- Python: [Version]
- Rust: [Version]
- CUDA: [Version]
- Dependencies: [From requirements.txt]

## Hyperparameters
| Parameter | Value | Description |
|-----------|-------|-------------|
| learning_rate | 0.001 | Initial learning rate |
| batch_size | 64 | Training batch size |
| ... | ... | ... |

## Random Seeds
| Experiment | Seed |
|------------|------|
| Main results | 42 |
| Ablation 1 | 123 |
| Ablation 2 | 456 |
```

---

## 3. Figure Preparation

### 3.1 Technical Requirements

| Format | Resolution | Use Case |
|--------|------------|----------|
| PDF | Vector | Line plots, diagrams |
| PNG | 300+ DPI | Raster images, screenshots |
| SVG | Vector | Web display |

### 3.2 Figure Checklist

- [ ] All figures numbered (Figure 1, Figure 2, ...)
- [ ] All figures have captions
- [ ] Text legible at publication size
- [ ] Consistent font across figures
- [ ] Color-blind friendly palette
- [ ] Axis labels present
- [ ] Legend clearly positioned
- [ ] Source code for figures included

### 3.3 Figure Types

| Type | Description | Tool |
|------|-------------|------|
| Architecture diagrams | System structure | draw.io, Figma |
| Performance plots | Bar/line charts | matplotlib, seaborn |
| Scatter plots | Correlation | matplotlib |
| Heatmaps | Matrix data | seaborn |
| Flowcharts | Algorithm flow | draw.io |

---

## 4. Table Preparation

### 4.1 Table Checklist

- [ ] All tables numbered (Table 1, Table 2, ...)
- [ ] All tables have captions
- [ ] Column headers clear
- [ ] Units specified
- [ ] Significant figures appropriate
- [ ] Best results highlighted
- [ ] Table notes for abbreviations

### 4.2 Standard Table Format

```markdown
Table N: [Descriptive Title]. [Brief description of content.]

| Method | Accuracy (%) | Time (ms) | Memory (MB) |
|--------|-------------|-----------|-------------|
| Baseline | 85.2 ± 0.5 | 150.3 | 512 |
| Proposed | **98.7 ± 0.2** | 12.5 | 256 |

Note: Best results shown in bold. ± indicates standard deviation.
```

---

## 5. Video and Interactive Materials

### 5.1 Video Requirements

| Item | Requirement | Status |
|------|-------------|--------|
| Format | MP4 (H.264) | [ ] |
| Resolution | 1080p minimum | [ ] |
| Duration | < 10 minutes | [ ] |
| Audio | Clear narration | [ ] |
| Captions | Subtitles available | [ ] |
| Thumbnail | Representative frame | [ ] |

### 5.2 Interactive Demos

| Item | Requirement | Status |
|------|-------------|--------|
| Web demo | Live URL | [ ] |
| Instructions | How to use | [ ] |
| Sample inputs | Provided | [ ] |
| Expected outputs | Documented | [ ] |
| Browser support | Chrome, Firefox, Safari | [ ] |

---

## 6. Document Preparation

### 6.1 Supplementary PDF

**Structure:**
1. Title page (matches main paper)
2. Table of Contents
3. Appendices A, B, C, ...
4. Additional References

**Formatting:**
- Page numbers throughout
- Section numbers consistent with main paper
- Cross-references to main paper sections

### 6.2 File Naming Convention

```
paper1_supplementary.pdf
paper1_appendix_proofs.pdf
paper1_appendix_experiments.pdf
paper1_code.zip
paper1_data.zip
```

---

## 7. Repository Badges

Add the following badges to README:

```markdown
[![DOI](https://zenodo.org/badge/DOI/xxx.svg)](https://doi.org/xxx)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Code style: rustfmt](https://img.shields.io/badge/code%20style-rustfmt-green)](https://github.com/rust-lang/rustfmt)
[![Tests](https://github.com/SuperInstance/Constraint-Theory/workflows/Tests/badge.svg)](https://github.com/SuperInstance/Constraint-Theory/actions)
```

---

## 8. Reproducibility Checklist

### 8.1 Code Reproducibility

- [ ] All dependencies specified
- [ ] Virtual environment file included
- [ ] Docker container available
- [ ] One-click reproduction script
- [ ] Tested on clean machine

### 8.2 Experiment Reproducibility

- [ ] Random seeds documented
- [ ] Exact commands to run
- [ ] Expected outputs shown
- [ ] Hardware requirements stated
- [ ] Estimated runtime given

### 8.3 Results Reproducibility

- [ ] Raw output files included
- [ ] Analysis scripts provided
- [ ] Figure generation code included
- [ ] Table generation code included

---

## 9. Submission Package Checklist

### 9.1 For Conference Submission

```
submission/
├── main_paper.pdf
├── supplementary.pdf
├── code.zip (or GitHub link)
├── README.txt (instructions)
└── LICENSE.txt
```

### 9.2 For Journal Submission

```
submission/
├── main_paper.pdf
├── main_paper.tex
├── figures/
├── supplementary.pdf
├── supplementary.tex
├── references.bib
├── code.zip
├── data.zip
├── README.txt
└── COVER_LETTER.txt
```

### 9.3 Final Checks

- [ ] All files present
- [ ] File sizes under limits
- [ ] PDF renders correctly
- [ ] Links are working
- [ ] Contact information current
- [ ] No identifying information (if blind)

---

## 10. Post-Acceptance Checklist

### 10.1 Camera-Ready Materials

- [ ] Addressed all reviewer comments
- [ ] Updated acknowledgments
- [ ] Copyright transfer completed
- [ ] Final proofreading done
- [ ] Author information finalized

### 10.2 Public Release

- [ ] Code repository public
- [ ] Data repository public
- [ ] arXiv preprint updated
- [ ] Project website updated
- [ ] Social media announcement

---

## 11. Venue-Specific Requirements

### 11.1 NeurIPS

| Item | Requirement |
|------|-------------|
| Main paper | 8 pages + references |
| Supplementary | Unlimited |
| Code submission | Optional but encouraged |
| Reviewer feedback | Anonymized response |

### 11.2 ICLR

| Item | Requirement |
|------|-------------|
| Main paper | 8 pages + references |
| Supplementary | Unlimited |
| Code submission | Optional |
| Open review | Public during review |

### 11.3 JMLR

| Item | Requirement |
|------|-------------|
| Length | No strict limit (~20-30 pages) |
| Supplementary | Included in submission |
| Code | Strongly encouraged |
| Data | Required if possible |

---

## 12. Quality Assurance

### 12.1 Pre-Submission QA

- [ ] Spell check all documents
- [ ] Grammar check all documents
- [ ] Verify all citations resolve
- [ ] Verify all cross-references work
- [ ] Test all code on sample data
- [ ] Verify all URLs accessible
- [ ] Check file permissions

### 12.2 Reproducibility Test

```bash
# Test script
git clone https://github.com/SuperInstance/Constraint-Theory
cd Constraint-Theory
pip install -r requirements.txt
python scripts/reproduce_results.py
# Verify output matches paper
```

---

**Status:** Active
**Review Cycle:** With each submission
**Contact:** constraint-theory@example.com
