# Week 5: Evaluation Findings & Recommendations

**MIT Blended AI+X PBL – AI-Enabled Cybersecurity (Anthropic Project)**  
**Date:** January 2026

---

## 1. Executive Summary

Week 5 established an evaluation framework for measuring vulnerability detection performance. Key finding: **baseline deterministic detectors achieve 91% precision but only 67% recall**, leaving room for AI-assisted improvements.

---

## 2. Top 3 Evaluation Findings

### Finding 1: Baseline Achieves High Precision (91%) but Moderate Recall (67%)

**Observation:**
- Deterministic regex patterns correctly identify most flagged items (low false positive rate)
- However, 33% of real vulnerabilities are missed (false negatives)
- Primary gaps: typo variations not in dictionary, secret patterns not in regex list

**Implication:**
- Adding more regex patterns would improve recall but risk precision degradation
- AI classification could help identify edge cases without expanding regex complexity

### Finding 2: False Positives Concentrate in Specific Categories

**Observation:**
| Category | FP Cases | Root Cause |
|----------|----------|------------|
| Typos | `teh` variable flagged | No context awareness |
| Secrets | Commented examples flagged | No semantic understanding |
| SQLi | Static queries sometimes flagged | Pattern too broad |

**Implication:**
- AI-assisted filtering could reduce FPs by 20-30% by understanding context
- Simple allowlist/blocklist could handle common FP patterns

### Finding 3: Pattern Coverage Gaps in Secret/SQLi Detection

**Observation:**
- Baseline missed: Stripe keys, Google API keys, some SQLAlchemy patterns
- Reason: Regex patterns don't cover all vendor-specific formats

**Implication:**
- Need to expand pattern library OR use AI for flexible pattern matching
- Consider integrating more comprehensive tools (gitleaks, semgrep)

---

## 3. Model Comparison Summary

| Model | Precision | Recall | F1 | FPR | Latency |
|-------|-----------|--------|-----|-----|---------|
| **Baseline** | **0.91** | **0.67** | **0.77** | 0.07 | <1ms |
| Ollama (llama3.1:8b) | 0.72 | 0.43 | 0.54 | 0.17 | ~54s/case |
| Ollama (mistral) | 0.50 | 0.03 | 0.06 | 0.03 | ~58s/case |

**Key Finding: Baseline significantly outperforms both LLMs!**
- Baseline F1=0.77 vs llama3.1:8b F1=0.54 vs mistral F1=0.06
- LLMs are too conservative, missing most true positives
- Latency cost is massive: 54-58 seconds vs <1ms per case

### Where AI Helps (Per-Category Analysis)

1. **SQLi detection:** llama3.1:8b achieved F1=0.86 (better than baseline F1=0.75)
   - AI recognized more SQL injection patterns than regex
   - Higher recall (0.90 vs 0.60) at cost of some false positives

### Where AI Falls Short

1. **Typo detection:** Both LLMs performed poorly (F1=0.17 and F1=0.00)
   - LLMs don't recognize typos as "vulnerabilities"
   - Baseline regex patterns work much better here
2. **Secret detection:** LLMs underperformed (F1=0.40 and F1=0.00)
   - LLMs too conservative, missing real secrets
3. **Latency:** 54-58 seconds per case vs <1ms for regex
2. **Consistency:** Same input may get different outputs across runs
3. **Cost:** Token usage adds up for large codebases

---

## 4. Recommended Direction for Week 6

### **Recommendation: Hybrid Approach (Engineering Robustness Primary)**

**Rationale:**
1. Baseline is already strong (91% precision) – small improvements yield high value
2. AI filtering is most valuable for *reducing* false positives, not primary detection
3. Scientific PoC (advanced vuln discovery) requires more foundation work

### Week 6 Action Plan

#### Priority 1: Engineering Robustness (70% effort)

| Action | Expected Impact | Effort |
|--------|-----------------|--------|
| Add allowlist for common FP patterns | -20% FP rate | Low |
| Expand secret patterns (Stripe, Google, etc.) | +15% recall | Low |
| Add confidence scoring to findings | Better triage | Medium |
| Optional AI gating for borderline cases | -10% FP | Medium |

#### Priority 2: Scientific PoC Preparation (30% effort)

| Action | Expected Impact | Effort |
|--------|-----------------|--------|
| Document path traversal patterns | Future detection | Low |
| Document command injection patterns | Future detection | Low |
| Identify 3 candidate OSS repos for testing | Validation targets | Low |
| Prototype advanced SQLi (2nd-order) | PoC | Medium |

---

## 5. Concrete Next Steps

### Week 6 Sprint 1: FP Reduction

```python
# Example: Add allowlist to typo detector
ALLOWLIST_PATTERNS = [
    r'^[a-z]{2,4}$',  # Short variable names (teh, idx, cnt)
    r'^[A-Z_]+$',     # Constants (MAX_SIZE, API_URL)
]

# Example: Confidence scoring
class Finding:
    confidence: float  # 0.0 - 1.0
    context: str       # "production", "test", "docs"
```

### Week 6 Sprint 2: Pattern Expansion

Add missing patterns for:
- Stripe API keys (`sk_live_`, `pk_live_`)
- Google API keys (`AIza...`)
- Twilio (`SK...`, `AC...`)
- Database URLs (expand regex)

### Week 6 Sprint 3 (Optional): AI Gating

```python
def should_flag(finding: Finding) -> bool:
    if finding.confidence > 0.9:
        return True
    if finding.confidence < 0.5:
        return False
    # Borderline: use AI classifier
    return ai_classifier.classify(finding)
```

---

## 6. Success Criteria for Week 6

| Metric | Current | Target |
|--------|---------|--------|
| Overall F1 | 0.77 | ≥0.82 |
| False Positive Rate | 3.3% | ≤2.0% |
| Recall | 67% | ≥75% |
| Supported secret types | ~10 | ≥20 |

---

## 7. Appendix: Methodology Notes

### Dataset
- 60 labeled cases (20 typo, 20 secret, 20 SQLi)
- Balanced: 50% vulnerable, 50% safe
- All synthetic/placeholder values (no real secrets)

### Metrics
- Standard precision/recall/F1
- Per-category breakdown
- Latency measured per case

### Limitations
- Small dataset (N=60) – results are directional
- LLM responses may vary between runs
- Does not test full pipeline integration

---

*Generated as part of Week 5 deliverables – MIT Blended AI+X PBL*
