# Week 7: Deliverable Decision

**MIT Blended AI+X PBL – AI-Enabled Cybersecurity (Anthropic Project)**  
**Date:** January 2026

---

## Deliverable Type

**Selected Format:** Short Academic-Style Paper

---

## Target Audience

| Audience | Priority | Why |
|----------|----------|-----|
| **Security practitioners** | Primary | Engineers evaluating AI-assisted vulnerability detection tools |
| **Academic researchers** | Secondary | Those studying human-AI collaboration in security workflows |
| **Engineering teams** | Tertiary | Teams considering similar hybrid detection architectures |

---

## Justification: Why This Format

### Project Strengths That Support This Choice

1. **Structured research progression.** The project naturally follows the academic paper structure:
   - **Problem:** Vulnerability detection at scale with high false positive rates
   - **Method:** Hybrid architecture (deterministic detection + LLM explanation)
   - **Evaluation:** Formal metrics (91% precision, 67% recall) on curated dataset
   - **Discussion:** Responsible innovation considerations and tradeoffs

2. **Quantitative evaluation results.** Week 5 established reproducible metrics that support rigorous claims:
   - Precision/recall/F1 comparisons across detection categories
   - Baseline vs. LLM-assisted performance analysis
   - Per-category breakdown (secrets, SQLi, typos)

3. **Real-world validation.** Week 4 tested the scanner on 5 production OSS repositories (109K+ combined GitHub stars), providing evidence beyond synthetic benchmarks.

4. **Responsible innovation framing.** Week 6's essay provides substantial ethical discussion material that fits the "Discussion" section of an academic paper.

5. **Reproducibility.** All code, evaluation harness, and datasets are available in the repository, supporting the transparency expected in academic work.

### Why Not Other Formats

| Format | Reason for Not Selecting |
|--------|-------------------------|
| **Technical blog post** | Less rigorous; doesn't showcase the formal evaluation adequately |
| **Demo application** | The CLI already works well; a demo would duplicate existing documentation |
| **Video** | Production overhead; less permanent and harder to cite |
| **Hybrid (blog + repo)** | Close second choice, but the paper format better matches the project's research-oriented structure |

---

## What Success Looks Like

### Minimum Viable Deliverable (Week 7)

- [ ] Complete outline with all section headings
- [ ] Fully written Introduction and Background sections
- [ ] Bullet points for remaining sections
- [ ] Clear abstract summarizing the contribution

### Complete Deliverable (Week 8)

- [ ] All sections fully written (3,000–5,000 words)
- [ ] Figures: architecture diagram, evaluation results table
- [ ] References properly cited
- [ ] Peer review incorporated
- [ ] Final PDF or Markdown version ready for submission

### Quality Criteria

1. **Clarity:** A security engineer can understand the approach and replicate it
2. **Rigor:** Claims are supported by evaluation data with acknowledged limitations
3. **Defensibility:** Ethical considerations are prominently addressed
4. **Reproducibility:** Reader can run the scanner and evaluation harness themselves
5. **Contribution:** Clear articulation of what this project adds to the field

---

## Paper Structure Preview

```
1. Abstract
2. Introduction
3. Background & Related Work
4. System Design
5. Evaluation Methodology
6. Results
7. Discussion (including Responsible Innovation)
8. Limitations & Future Work
9. Conclusion
10. References
```

---

## Decision Rationale Summary

The short academic-style paper best showcases this project because:

- The work already has the structure of a research contribution
- Formal evaluation results (Week 5) deserve rigorous presentation
- Responsible innovation discussion (Week 6) fits naturally as a Discussion subsection
- The target audience (security practitioners, researchers) expects this format
- The repository serves as the "appendix" with full implementation details

---

*Decision documented as part of Week 7 deliverables – MIT Blended AI+X PBL*
