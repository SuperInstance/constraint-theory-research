# Peer Review Process

**Version:** 1.0
**Last Updated:** 2025-03-16
**Status:** Active

---

## 1. Overview

This document outlines the peer review process for Constraint Theory research papers, including internal review, external review, and response procedures.

---

## 2. Internal Review Process

### 2.1 Pre-Submission Checklist

Before external submission, all papers must pass internal review:

#### Technical Review
- [ ] All mathematical proofs verified
- [ ] Algorithm correctness confirmed
- [ ] Code reproducibility validated
- [ ] Benchmark methodology reviewed
- [ ] Statistical analysis verified

#### Content Review
- [ ] Abstract within word limit (200-400 words)
- [ ] Contributions clearly stated
- [ ] Related work comprehensive
- [ ] Conclusions supported by evidence
- [ ] Future work appropriate

#### Format Review
- [ ] Correct template used
- [ ] Citations properly formatted
- [ ] Figures legible and numbered
- [ ] Tables properly formatted
- [ ] No grammatical errors
- [ ] Consistent notation throughout

### 2.2 Internal Review Timeline

| Phase | Duration | Activities |
|-------|----------|------------|
| Self-review | 2 days | Author checks |
| Peer review | 1 week | Team member review |
| Revision | 3 days | Address feedback |
| Final check | 1 day | Lead author approval |
| **Total** | **~2 weeks** | |

### 2.3 Internal Review Form

```markdown
## Internal Review Report

**Paper:** [Title]
**Reviewer:** [Name]
**Date:** [YYYY-MM-DD]

### Overall Assessment
- [ ] Ready for submission
- [ ] Minor revisions needed
- [ ] Major revisions needed
- [ ] Not ready for submission

### Technical Correctness (1-5): ___
Comments:

### Clarity (1-5): ___
Comments:

### Significance (1-5): ___
Comments:

### Reproducibility (1-5): ___
Comments:

### Specific Issues

#### Section-by-Section Comments:
1. Introduction:
2. Methodology:
3. Results:
4. Discussion:
5. Conclusion:

### Required Changes:
1. 
2. 
3. 

### Suggestions:
1. 
2. 
3. 

### Minor Issues:
1. 
2. 
```

---

## 3. External Review Process

### 3.1 Journal Submission

#### NeurIPS/ICML/ICLR Process

```
Week 0:    Submission
Week 1-2:  Desk review (rejection or review)
Week 2-10: Peer review
Week 10:   Rebuttal period (typically 1 week)
Week 12:   Decision notification
Week 14:   Camera-ready deadline (if accepted)
```

#### Journal Process (JMLR, etc.)

```
Week 0:     Submission
Week 1-2:   Editor assignment
Week 2-4:   Desk review
Week 4-16:  Peer review (2-3 reviewers)
Week 16-18: Decision
Week 18-20: Revisions (if needed)
Week 20-24: Final decision
```

### 3.2 arXiv Preprint

**Timeline:**
- Post to arXiv after internal review
- Update with new versions as needed
- Link to submitted journal version when available

**Requirements:**
- LaTeX source recommended
- Include all figures
- Add "Submitted to [Venue]" note

---

## 4. Reviewer Response Guidelines

### 4.1 Response Structure

```markdown
# Response to Reviewers

We thank the reviewers for their constructive feedback. Below we address 
each comment point by point.

## Response to Reviewer 1

### Point 1: [Summary of reviewer's comment]
**Response:** We appreciate this observation. We have [action taken].
**Change:** See Section X, paragraph Y, lines Z.

### Point 2: [Summary of reviewer's comment]
**Response:** We agree that [acknowledgment]. To address this, we [action].
**Change:** Added Section X.Y with detailed explanation.

...

## Summary of Changes

1. Added new Section X.Y on [topic]
2. Expanded Figure 3 with additional data
3. Corrected equation in Section 4
4. Added references [A, B, C]
5. Clarified methodology in Section 3.2
```

### 4.2 Response Best Practices

**DO:**
- Thank reviewers sincerely
- Address every point raised
- Be specific about changes made
- Reference line numbers and sections
- Explain reasoning when disagreeing respectfully
- Highlight major changes prominently

**DON'T:**
- Dismiss reviewer concerns
- Be defensive or argumentative
- Ignore any comments
- Make vague promises
- Claim changes made without showing them
- Blame space limitations for major omissions

### 4.3 Handling Disagreements

When disagreeing with a reviewer:

1. **Acknowledge the concern**: "We understand the reviewer's point about..."
2. **Explain your position**: "However, we believe that..."
3. **Provide evidence**: "This is supported by..."
4. **Offer alternatives**: "We have instead added a discussion of..."

**Example:**
```markdown
### Point X: Reviewer suggests additional experiments

**Response:** We appreciate the reviewer's suggestion for additional 
experiments on larger datasets. While we agree this would strengthen the 
paper, we note that:

1. Our current experiments cover datasets up to 1M elements
2. The O(log n) complexity is already demonstrated
3. Computational resources limited further scaling

We have added a paragraph in Section 5.4 discussing this limitation and 
outlining plans for future scaling experiments.
```

---

## 5. Review Criteria by Venue

### 5.1 NeurIPS Criteria

| Criterion | Description | Weight |
|-----------|-------------|--------|
| Quality | Technical correctness, methodology | 30% |
| Clarity | Writing quality, organization | 20% |
| Originality | Novelty of contribution | 25% |
| Significance | Impact on field | 25% |

### 5.2 ICLR Criteria

| Criterion | Description | Weight |
|-----------|-------------|--------|
| Quality | Soundness of claims | 25% |
| Clarity | Paper organization | 20% |
| Originality | Novelty | 25% |
| Significance | Potential impact | 20% |
| Reproducibility | Code/data availability | 10% |

### 5.3 Journal Criteria (JMLR)

| Criterion | Description |
|-----------|-------------|
| Correctness | Mathematical and technical accuracy |
| Depth | Comprehensive treatment of topic |
| Reproducibility | Code and data availability |
| Impact | Long-term value to field |
| Presentation | Writing quality |

---

## 6. Rejection Handling

### 6.1 Understanding Rejections

Common rejection reasons:
- Insufficient novelty
- Methodological flaws
- Poor writing/presentation
- Out of scope for venue
- Incomplete validation

### 6.2 Post-Rejection Actions

1. **Read feedback carefully**: Extract actionable items
2. **Don't respond immediately**: Wait 24-48 hours
3. **Create revision plan**: Prioritize changes
4. **Seek second opinions**: Get colleagues' input
5. **Choose next venue**: Consider feedback on fit

### 6.3 Revision Before Resubmission

| Timeframe | Action |
|-----------|--------|
| Week 1 | Absorb feedback, plan revisions |
| Week 2-3 | Major revisions |
| Week 4 | Minor revisions, polish |
| Week 5 | Internal review |
| Week 6 | Submit to new venue |

---

## 7. Acceptance to Publication

### 7.1 Camera-Ready Preparation

**Checklist:**
- [ ] Address all reviewer comments
- [ ] Update author information
- [ ] Final figure/table polish
- [ ] Reference formatting
- [ ] Page limit compliance
- [ ] Copyright forms signed
- [ ] Supplementary materials finalized

### 7.2 Post-Acceptance Timeline

| Event | Timeline |
|-------|----------|
| Acceptance notification | Day 0 |
| Camera-ready deadline | Day 14-30 |
| Copyright transfer | Day 14-30 |
| Page proof review | Day 30-60 |
| Publication | Day 60-90 |

---

## 8. Open Science Practices

### 8.1 Code Release

- Release code upon publication (not before)
- Use DOI for code version (Zenodo)
- Include README with instructions
- Test reproducibility on clean system

### 8.2 Data Release

- Anonymize if needed
- Provide documentation
- Use persistent identifiers
- License appropriately

### 8.3 Preprint Policy

- Post to arXiv upon acceptance
- Update with published version
- Cross-reference DOI

---

## 9. Appeals Process

### 9.1 When to Appeal

Valid grounds:
- Factual errors in review
- Reviewer bias
- Procedural irregularities

Not valid:
- Disagreement with evaluation
- Complaints about tone

### 9.2 Appeal Structure

```markdown
**Appeal for Paper [ID]**

We respectfully request reconsideration of the decision on our paper 
"[Title]". We believe there was a misunderstanding regarding:

[Specific issue]

The reviewer stated: "[quote]"

However, our paper actually: "[explanation with evidence]"

We have attached a detailed response addressing all reviewer comments.

Thank you for your consideration.
```

---

## 10. Review Templates

### 10.1 NeurIPS Review Template

```markdown
## Review Summary

**Paper ID:** [ID]
**Title:** [Title]

### Summary
[Brief description of paper content]

### Strengths
1. 
2. 
3. 

### Weaknesses
1. 
2. 
3. 

### Questions
1. 
2. 

### Limitations
Have the authors discussed limitations? 

### Ethics
Are there ethical considerations?

### Overall Score (1-10): ___

### Confidence (1-5): ___
```

---

## 11. Contact Information

**Primary Contact:** constraint-theory@example.com
**GitHub Issues:** https://github.com/SuperInstance/Constraint-Theory/issues

---

**Status:** Active
**Review Cycle:** Annual
**Next Review:** 2026-03-16
