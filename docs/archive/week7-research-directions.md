# Week 7: Research Directions and Future Work

**MIT Blended AI+X PBL – AI-Enabled Cybersecurity (Anthropic Project)**  
**Date:** January 2026

---

## Overview

This document defines concrete research questions emerging from our Week 2–6 work, categorized by timeline and alignment with engineering robustness vs. scientific proof-of-concept goals.

---

## Research Questions

### RQ1: Can confidence scoring reduce false positive burden without sacrificing recall?

**Question:** How can we assign meaningful confidence scores to findings that help developers prioritize review without hiding real vulnerabilities?

**Justification:**  
Our Week 4 validation showed a ~70-95% false positive rate depending on category. Binary "vulnerable/not vulnerable" labels force developers to review everything or risk missing issues. A well-calibrated confidence score could enable triage: high-confidence findings get immediate attention, low-confidence findings go to a backlog.

**Potential Approaches:**
- Rule-based scoring (file path context, pattern specificity, entropy)
- Ensemble methods combining multiple detector signals
- LLM-assisted confidence calibration (post-detection)

**Timeline:** Short-term (2–3 weeks)  
**Alignment:** Engineering robustness

---

### RQ2: Which vulnerability categories benefit most from AI assistance?

**Question:** For which vulnerability types does LLM-assisted classification meaningfully outperform deterministic detection?

**Justification:**  
Our Week 5 evaluation showed the baseline outperforming LLMs overall (F1 0.77 vs 0.54), but per-category results hint at nuance. SQL injection detection showed LLM promise (F1 0.86 vs baseline 0.75 in some runs). Understanding where AI genuinely helps—and where it doesn't—informs resource allocation.

**Potential Approaches:**
- Expand evaluation dataset per category (N>50 per type)
- Compare LLM performance on semantic vs. syntactic vulnerabilities
- Measure AI value-add for edge cases vs. clear-cut patterns

**Timeline:** Short-term (2–3 weeks)  
**Alignment:** Scientific proof-of-concept

---

### RQ3: How can AI reduce false positives without becoming the primary detector?

**Question:** Can LLMs serve as a reliable "second opinion" filter that reduces false positives while preserving the auditability of deterministic primary detection?

**Justification:**  
Our design philosophy keeps LLMs out of primary detection for reliability reasons. However, using LLMs as a post-detection filter could capture their contextual understanding without relying on them for the security-critical first pass. The challenge is calibrating when to trust the LLM's override.

**Potential Approaches:**
- Two-stage pipeline: deterministic detection → LLM filtering
- Confidence thresholds for when LLM opinion is requested
- Human-in-the-loop validation of LLM filter decisions

**Timeline:** Medium-term (4–6 weeks)  
**Alignment:** Hybrid (engineering + scientific)

---

### RQ4: Can we quantify the reliability of LLM-based classification across model versions and providers?

**Question:** How consistent are LLM vulnerability classifications across different runs, model versions, and providers?

**Justification:**  
One concern with AI-assisted detection is reproducibility. If the same code snippet gets different classifications on different days (due to model updates, temperature, or provider changes), the tool becomes unreliable. Quantifying this variance is essential for production deployment decisions.

**Potential Approaches:**
- Run identical test suite across multiple models (Claude, GPT-4, Llama, Mistral)
- Measure classification variance over repeated runs (same model, different times)
- Track consistency degradation as models are updated

**Timeline:** Medium-term (4–6 weeks)  
**Alignment:** Scientific proof-of-concept

---

### RQ5: What patterns distinguish high-value findings from noise in real-world codebases?

**Question:** Can we identify structural or contextual patterns that distinguish true vulnerabilities from false positives in production code?

**Justification:**  
Our Week 4 scans revealed that many false positives follow predictable patterns: test files, documentation, placeholder values, British spellings. Understanding these patterns systematically could enable allowlist generation or automatic severity adjustment.

**Potential Approaches:**
- Analyze false positives from Week 4 scans to identify common features
- Build file path and context classifiers
- Develop heuristics for test file detection, documentation detection, etc.

**Timeline:** Short-term (2–3 weeks)  
**Alignment:** Engineering robustness

---

## Timeline Summary

| Research Question | Timeline | Primary Goal |
|-------------------|----------|--------------|
| RQ1: Confidence scoring | Short-term (2–3 weeks) | Engineering robustness |
| RQ2: Per-category AI value | Short-term (2–3 weeks) | Scientific proof-of-concept |
| RQ3: AI as second-opinion filter | Medium-term (4–6 weeks) | Hybrid |
| RQ4: LLM reliability quantification | Medium-term (4–6 weeks) | Scientific proof-of-concept |
| RQ5: FP pattern identification | Short-term (2–3 weeks) | Engineering robustness |

---

## Alignment Matrix

| Goal | Research Questions | Focus |
|------|-------------------|-------|
| **Engineering robustness** | RQ1, RQ5 | Improve usability and reduce noise |
| **Scientific proof-of-concept** | RQ2, RQ4 | Rigorous measurement and comparison |
| **Hybrid** | RQ3 | Practical improvement with theoretical grounding |

---

## Recommended Next Steps (Week 8+)

### Immediate (Week 8)

1. **Implement RQ1 prototype:** Add confidence score field to findings schema using rule-based heuristics (file path, pattern specificity)
2. **Expand evaluation dataset:** Add 20+ cases per category to improve statistical power for RQ2

### Near-term (Weeks 9–10)

3. **Analyze Week 4 false positives:** Systematically categorize FPs to inform RQ5 heuristics
4. **Multi-model evaluation:** Run same test suite against 3+ LLM providers for RQ4

### Medium-term (Weeks 11–12)

5. **Two-stage pipeline prototype:** Implement deterministic → LLM filter architecture for RQ3
6. **Paper completion:** Finalize all sections with updated results

---

## Success Criteria

| Research Question | Success Metric |
|-------------------|----------------|
| RQ1 | Confidence scores correlate with actual FP rate (r > 0.5) |
| RQ2 | Identify at least one category where LLM outperforms baseline by >10% F1 |
| RQ3 | Two-stage pipeline reduces FP rate by >20% without recall loss >5% |
| RQ4 | Measure inter-run variance; identify providers with <10% classification variance |
| RQ5 | Develop heuristics that correctly classify >80% of Week 4 FPs |

---

## Constraints and Ethical Considerations

All research directions must maintain the responsible innovation principles established in Week 6:

- **No expansion of detection to exploitation.** Research remains focused on finding, not exploiting, vulnerabilities.
- **Redaction preserved.** Any new features maintain mandatory secret redaction.
- **Human-in-the-loop.** Automated filtering or confidence scoring does not remove human review requirement.
- **Reproducibility.** All experiments documented with methodology and datasets (using synthetic/placeholder data only).

---

*Research directions documented as part of Week 7 deliverables – MIT Blended AI+X PBL*
