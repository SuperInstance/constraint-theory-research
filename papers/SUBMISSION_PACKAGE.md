# Submission Package Template

**Version:** 1.0
**Last Updated:** 2025-03-16

---

## Package Structure

```
constraint-theory-paper{N}_submission/
├── paper.tex                    # Main LaTeX source
├── paper.pdf                    # Compiled PDF
├── neurips_2024.sty            # Conference style file
├── references.bib              # Bibliography
├── figures/
│   ├── architecture.pdf        # Figure 1
│   ├── performance.pdf         # Figure 2
│   ├── manifold.pdf           # Figure 3
│   └── scaling.pdf            # Figure 4
├── supplementary/
│   ├── appendix.tex           # Supplementary material
│   ├── appendix.pdf           # Compiled appendix
│   ├── proofs/
│   │   ├── theorem1.pdf       # Detailed proofs
│   │   └── theorem2.pdf
│   └── code_snippets/
│       ├── rust_core.rs       # Core implementation
│       └── cuda_kernel.cu     # GPU implementation
├── data/
│   ├── benchmark_results.csv  # Raw benchmark data
│   └── statistical_tests.json # Statistical analysis
├── code_link.txt              # Link to GitHub
├── README.md                  # Package description
└── CHECKLIST.md               # Submission checklist
```

---

## README Template

```markdown
# Constraint Theory Paper {N}: {Title}

## Overview

This package contains all materials for the submission of:

**Title:** {Full Title}

**Authors:** {Authors (anonymized for review)}

**Target Venue:** {Conference}

## Contents

- `paper.pdf` - Main paper (8 pages)
- `supplementary/appendix.pdf` - Supplementary material
- `figures/` - All figures in PDF format
- `data/` - Raw experimental data
- `code_link.txt` - Link to code repository

## Reproducibility

All experiments can be reproduced using the code at:
https://github.com/SuperInstance/Constraint-Theory

### Quick Reproduction

```bash
# Clone repository
git clone https://github.com/SuperInstance/Constraint-Theory
cd Constraint-Theory

# Run benchmarks
cargo bench

# Generate figures
python scripts/generate_figures.py
```

### Hardware Requirements

- CPU: 8+ cores recommended
- RAM: 16GB minimum
- GPU: NVIDIA GPU with CUDA support (optional)
- OS: Linux, macOS, or Windows

## Contact

For questions about this submission, please contact the program committee 
through the conference submission system.

## License

Paper content: CC BY 4.0
Code: MIT License
```

---

## Checklist Template

```markdown
# Submission Checklist

## Pre-Submission

### Content
- [ ] Abstract word count: ___ (target: 200-400)
- [ ] Main paper page count: ___ (target: 8)
- [ ] All figures referenced in text
- [ ] All tables referenced in text
- [ ] All theorems have proofs (main or appendix)
- [ ] All algorithms have complexity analysis
- [ ] All citations are in bibliography

### Format
- [ ] Correct conference template used
- [ ] Correct page margins
- [ ] Font size >= 10pt
- [ ] Line numbers enabled
- [ ] PDF compiles without errors
- [ ] All figures render correctly

### Anonymization
- [ ] No author names in paper
- [ ] No institutional affiliations
- [ ] No acknowledgments section
- [ ] GitHub links use anonymous repo (if required)

### Reproducibility
- [ ] Code repository is public/accessible
- [ ] README has reproduction instructions
- [ ] Random seeds are documented
- [ ] Hardware specs are documented
- [ ] Software versions are documented

### Supplementary
- [ ] Appendix PDF compiles
- [ ] Code snippets are correct
- [ ] Data files are complete

## Submission

### Upload
- [ ] Main paper PDF uploaded
- [ ] Supplementary PDF uploaded
- [ ] Code link provided
- [ ] Metadata form completed
- [ ] Author conflicts declared

### Confirmation
- [ ] Submission confirmation received
- [ ] Paper ID recorded: _________
- [ ] Confirmation email saved

## Post-Submission
- [ ] Monitor for reviewer questions
- [ ] Prepare rebuttal responses
- [ ] Update arXiv after review period
```

---

## Metadata Form

```
Paper Title: _________________________________________________

Short Title: _________________________________________________

Abstract: (200-400 words)
_____________________________________________________________
_____________________________________________________________
_____________________________________________________________

Keywords (3-6):
1. _______________
2. _______________
3. _______________
4. _______________
5. _______________

Primary Subject Area:
[ ] Machine Learning
[ ] Algorithms and Theory
[ ] Systems
[ ] Applications
[ ] Other: _______________

Secondary Subject Areas:
[ ] Computational Geometry
[ ] High-Performance Computing
[ ] Distributed Systems
[ ] Computer Graphics
[ ] Other: _______________

Code Availability:
[ ] Code is publicly available
    URL: _________________________________________________
[ ] Code will be made available upon acceptance
[ ] Code is not available (explain why)

Data Availability:
[ ] All data is synthetic/generated
[ ] Data is publicly available
    URL: _________________________________________________

Conflict of Interest:
[ ] No conflicts of interest
[ ] Conflicts disclosed in paper

Prior Publication:
[ ] This work has not been published previously
[ ] This work is an extension of: _________________________

arXiv Preprint:
[ ] Will be posted prior to submission
[ ] Will be posted upon acceptance
[ ] Will not be posted
```

---

## Code Link File Template

```
CODE REPOSITORY LINK
====================

Repository: https://github.com/SuperInstance/Constraint-Theory

Version: v1.0.0 (tagged release corresponding to this submission)

Branch: main

Commit Hash: [To be filled at submission time]

Direct Download:
https://github.com/SuperInstance/Constraint-Theory/archive/refs/tags/v1.0.0.zip

Reproduction Instructions:
1. Clone repository
2. Run: cargo build --release
3. Run: cargo bench --bench all
4. See papers/TRACEABILITY_MATRIX.md for full reproduction guide

License: MIT

Contact: constraint-theory@example.com
```

---

## File Naming Conventions

### Main Paper
- `paper.tex` or `main.tex`
- `paper.pdf` (compiled output)

### Figures
- `figure{N}_{description}.pdf` (vector)
- `figure{N}_{description}.png` (raster, 300 DPI minimum)

### Tables
- Embedded in LaTeX source
- Raw data in `data/table{N}_{description}.csv`

### Algorithms
- Embedded in LaTeX source using `algorithm` package
- Pseudocode format following algorithmic style

### Supplementary
- `appendix.tex` / `appendix.pdf`
- `supplementary.tex` / `supplementary.pdf`

---

## Compilation Instructions

### LaTeX Compilation

```bash
# Standard compilation
pdflatex paper.tex
bibtex paper
pdflatex paper.tex
pdflatex paper.tex

# With latexmk (recommended)
latexmk -pdf paper.tex

# Clean auxiliary files
latexmk -c
```

### Figure Generation

```bash
# Generate all figures from data
python scripts/generate_figures.py --output figures/

# Generate specific figure
python scripts/generate_figure.py --figure 1 --output figures/figure1.pdf
```

### Benchmark Data Export

```bash
# Run benchmarks and export data
cargo bench --bench all -- --save-baseline submission
python scripts/export_benchmark_data.py --output data/
```

---

## Verification Script

```bash
#!/bin/bash
# verify_submission.sh

echo "Verifying submission package..."

# Check required files
required_files=("paper.pdf" "paper.tex" "references.bib" "code_link.txt")
for file in "${required_files[@]}"; do
    if [ ! -f "$file" ]; then
        echo "ERROR: Missing required file: $file"
        exit 1
    fi
done

# Check page count
pages=$(pdfinfo paper.pdf | grep "Pages:" | awk '{print $2}')
if [ "$pages" -gt 8 ]; then
    echo "WARNING: Paper has $pages pages (target: 8)"
fi

# Check PDF size
size=$(stat -f%z paper.pdf 2>/dev/null || stat -c%s paper.pdf)
if [ "$size" -gt 10000000 ]; then
    echo "WARNING: PDF is larger than 10MB"
fi

# Verify figures
for fig in figures/*.pdf; do
    if [ ! -f "$fig" ]; then
        echo "ERROR: Missing figure: $fig"
        exit 1
    fi
done

echo "Verification complete. Package ready for submission."
```

---

## Package Archive

### Creating Archive

```bash
# Create tar.gz archive
tar -czvf submission_package.tar.gz constraint-theory-paper1_submission/

# Create zip archive
zip -r submission_package.zip constraint-theory-paper1_submission/
```

### Archive Contents Verification

```bash
# List archive contents
tar -tzvf submission_package.tar.gz

# Verify archive integrity
tar -tzvf submission_package.tar.gz | wc -l
```

---

**Status:** Template Ready
**Last Updated:** 2025-03-16
