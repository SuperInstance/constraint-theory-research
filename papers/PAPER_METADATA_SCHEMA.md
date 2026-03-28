# Paper Metadata Schema

**Version:** 1.0
**Last Updated:** 2025-03-16
**Status:** Standard for all papers

---

## 1. Metadata Fields

Each paper in this repository must include the following metadata fields:

### 1.1 Required Fields

```yaml
paper_id: string           # Unique identifier (e.g., "paper1", "paper2")
title: string              # Full paper title
short_title: string        # Abbreviated title for citations
authors:                   # Author list
  - name: string
    affiliation: string
    email: string
    orcid: string          # Optional ORCID identifier
    corresponding: boolean # Is this the corresponding author?
abstract: string           # Paper abstract (200-400 words)
keywords: string[]         # 3-6 keywords
primary_domain: string     # Main research area
secondary_domains: string[] # Related research areas
```

### 1.2 Publication Information

```yaml
publication_status: enum   # draft | submitted | under_review | accepted | published
submission_date: date      # Date submitted (YYYY-MM-DD)
target_venue: string       # Primary target venue
secondary_venues: string[] # Alternative venues
arxiv_id: string           # arXiv identifier (e.g., "2503.15847")
doi: string                # DOI when published
publication_date: date     # Date of publication
```

### 1.3 Document Information

```yaml
page_count: integer        # Approximate page count
word_count: integer        # Word count
figures: integer           # Number of figures
tables: integer            # Number of tables
algorithms: integer        # Number of algorithms
theorems: integer          # Number of theorems
supplementary_pages: integer # Supplementary material page count
```

### 1.4 Code and Data

```yaml
code_repository: url       # GitHub repository URL
code_version: string       # Version tag or commit hash
data_availability: string  # Statement on data availability
reproducibility_statement: string # Reproducibility commitment
```

### 1.5 Relationships

```yaml
related_papers:            # Papers in this series
  - paper_id: string
    relationship: enum     # precedes | follows | related | cites
cross_references:          # Sections referenced in other papers
  - paper_id: string
    section: string
    description: string
```

---

## 2. Notation Standards

### 2.1 Mathematical Notation

All papers must use consistent mathematical notation:

| Symbol | Description | LaTeX |
|--------|-------------|-------|
| Ω | Origin-centric geometry | `\Omega` |
| Φ | Phi-folding operator | `\Phi` |
| ρ(x) | Constraint density function | `\rho(x)` |
| ℳ | Manifold | `\mathcal{M}` |
| 𝒢 | Gauge field | `\mathcal{G}` |
| H(γ) | Holonomy matrix | `H(\gamma)` |
| h_norm | Normalized holonomy | `h_{\text{norm}}` |
| κ_ij | Discrete Ricci curvature | `\kappa_{ij}` |
| p_c | Percolation threshold | `p_c` |
| LVQ | Lattice Vector Quantization | LVQ |

### 2.2 Algorithmic Notation

| Symbol | Description |
|--------|-------------|
| O(n) | Big-O complexity |
| T(n) | Time complexity function |
| S(n) | Space complexity function |
| SIMD | Single Instruction Multiple Data |
| GPU | Graphics Processing Unit |
| FFI | Foreign Function Interface |

### 2.3 Units and Formats

| Quantity | Unit | Format |
|----------|------|--------|
| Time (small) | nanoseconds | 74 ns |
| Time (medium) | milliseconds | 0.5 ms |
| Time (large) | seconds | 1.5 s |
| Speedup | factor | 200× |
| Memory | bytes | 12 MB |
| Throughput | ops/sec | 13.5 M ops/s |
| Percentage | percent | 99.99% |

---

## 3. Figure and Table Numbering

### 3.1 Numbering Convention

- Figures: `Figure N` where N is sequential within paper
- Tables: `Table N` where N is sequential within paper
- Algorithms: `Algorithm N` where N is sequential within paper
- Theorems: `Theorem N` where N is sequential within paper
- Equations: Numbered as `(N)` within sections

### 3.2 Caption Format

```
Figure N: [Title]. [Description of content].
```

Example:
```
Figure 1: System Architecture. Four-layer hybrid architecture showing TypeScript API, 
Rust acceleration, Go concurrent processing, and CUDA GPU layers.
```

### 3.3 Cross-Reference Format

Within papers:
- "as shown in Figure 3"
- "see Table 2 for comparison"
- "Algorithm 1 describes the construction"

Between papers:
- "see Paper 1, Section 3.2"
- "as demonstrated in Paper 2, Table 4"

---

## 4. Section Structure Standard

### 4.1 Standard Paper Sections

1. **Abstract** (200-400 words)
2. **Introduction**
   - Motivation
   - Problem Statement
   - Contributions
3. **Background / Mathematical Framework**
4. **Methodology / Algorithm Design**
5. **Implementation Details**
6. **Experimental Results**
7. **Applications** (if applicable)
8. **Related Work**
9. **Discussion** (optional)
10. **Conclusion**
    - Summary
    - Future Work
11. **References**
12. **Appendix** (supplementary material)

### 4.2 Section Numbering

- Top-level: 1, 2, 3, ...
- Second-level: 1.1, 1.2, 1.3, ...
- Third-level: 1.1.1, 1.1.2, ...

---

## 5. Citation Format

### 5.1 In-Text Citations

- Single author: `(Author, Year)` or `Author (Year)`
- Two authors: `(Author1 and Author2, Year)`
- Three+ authors: `(Author1 et al., Year)`
- Multiple citations: `(Author1, Year; Author2, Year)`

### 5.2 BibTeX Entry Format

```bibtex
@article{key2025,
  author = {Last, First and Last2, First2},
  title = {Full Title of the Paper},
  journal = {Journal Name},
  year = {2025},
  volume = {1},
  pages = {1--20},
  doi = {10.1000/xxx},
  url = {https://doi.org/10.1000/xxx}
}

@inproceedings{key2025conf,
  author = {Last, First and Last2, First2},
  title = {Full Title of the Paper},
  booktitle = {Proceedings of Conference Name},
  year = {2025},
  pages = {1--10},
  publisher = {Publisher Name},
  doi = {10.1000/xxx}
}

@misc{key2025arxiv,
  author = {Last, First and Last2, First2},
  title = {Full Title of the Paper},
  year = {2025},
  eprint = {2503.15847},
  archiveprefix = {arXiv},
  primaryclass = {cs.LG}
}
```

---

## 6. File Naming Conventions

### 6.1 Paper Files

- Main paper: `paper{N}_{short_title}.tex`
- Supplementary: `paper{N}_supplementary.tex`
- Bibliography: `paper{N}_references.bib`

### 6.2 Figure Files

- Raster: `figure{N}_{description}.png` (300 DPI minimum)
- Vector: `figure{N}_{description}.pdf` or `.svg`

### 6.3 Data Files

- CSV: `data_{description}.csv`
- JSON: `data_{description}.json`
- Binary: `data_{description}.bin`

---

## 7. Version Control

### 7.1 Version Numbers

- Major: Substantial changes (new sections, new results)
- Minor: Small additions, corrections
- Patch: Typo fixes, formatting

Format: `v{MAJOR}.{MINOR}.{PATCH}`

### 7.2 Change Log

Each paper should include a `CHANGELOG.md` with:

```markdown
## [1.1.0] - 2025-03-16
### Added
- New experimental results for GPU scaling

### Changed
- Updated Figure 3 with corrected data

### Fixed
- Typo in Theorem 2 proof
```

---

## 8. Quality Checklist

Before submission, verify:

### 8.1 Content Quality
- [ ] Abstract within word limit
- [ ] All claims supported by evidence
- [ ] All figures referenced in text
- [ ] All tables referenced in text
- [ ] No undefined terms
- [ ] Consistent terminology throughout

### 8.2 Format Quality
- [ ] Correct template used
- [ ] Correct page margins
- [ ] Correct font size
- [ ] All equations properly formatted
- [ ] All citations resolved
- [ ] No orphan/widow lines

### 8.3 Reproducibility
- [ ] Code repository linked
- [ ] Random seeds specified
- [ ] Hardware specifications provided
- [ ] Software versions listed
- [ ] Parameters documented

---

**Status:** Approved
**Applies to:** All papers in this repository
**Review cycle:** Annually or when major changes needed
