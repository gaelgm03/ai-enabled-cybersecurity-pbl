# Week 5: Evaluation Plan & Direction Decision

**MIT Blended AI+X PBL – AI-Enabled Cybersecurity (Anthropic Project)**  
**Date:** January 2026

---

## 1. Direction Decision

### Options Considered

| Option | Description | Pros | Cons |
|--------|-------------|------|------|
| **(A) Engineering Robustness** | Reduce false positives, improve reliability | Immediate value, measurable | Less novel/publishable |
| **(B) Scientific PoC** | Discover complex real-world vulns | More ambitious, research value | Higher risk, harder to evaluate |
| **(C) Hybrid** | 70% robustness + 30% PoC exploration | Balanced, hedges risk | Split focus |

### **Decision: Option C – Hybrid (70/30 split)**

**Justification:**
1. **Engineering value is immediate:** Our pipeline has known false positive issues (typos in identifiers, placeholder secrets). AI-assisted filtering is low-risk, high-impact.
2. **Scientific exploration keeps us ambitious:** Exploring path traversal/command injection patterns prepares us for Week 6+ without derailing Week 5.
3. **Eval framework serves both:** The harness we build validates robustness improvements AND can benchmark future vuln classes.
4. **Time-boxed:** 70% of Week 5 on robustness evals, 30% on documenting next-level vuln classes.

---

## 2. Week 5 Objectives

### Primary Objectives (70% effort)
1. ✅ Create evaluation harness for comparing deterministic vs AI-assisted detection
2. ✅ Build ground-truth dataset (50+ labeled cases)
3. ✅ Run baseline + Ollama model comparisons
4. ✅ Measure precision/recall/F1 per category
5. ✅ Document where AI helps vs fails

### Secondary Objectives (30% effort)
1. ✅ Document taxonomy of advanced vuln classes (path traversal, command injection)
2. ✅ Identify 2-3 candidate repos for Week 6 scientific exploration
3. ✅ Outline what "success" looks like for discovering real-world vulns

---

## 3. Success Metrics & Acceptance Criteria

### 3.1 Quantitative Metrics

| Metric | Baseline Target | AI-Assisted Target | Measurement |
|--------|-----------------|-------------------|-------------|
| **Overall F1** | ≥0.60 | ≥0.75 | Eval harness output |
| **Typo FP Rate** | Establish baseline | Reduce by ≥20% | Negative control cases |
| **Secret FP Rate** | Establish baseline | Reduce by ≥30% | Placeholder detection |
| **SQLi Precision** | ≥0.70 | ≥0.85 | Parameterized query cases |
| **Latency** | N/A (instant) | <2s per case | Timer in harness |

### 3.2 Qualitative Criteria

| Criterion | Acceptance |
|-----------|------------|
| **Reproducibility** | Single command runs full eval |
| **Dataset quality** | Each case has rationale + ground truth |
| **No unsafe content** | Zero real secrets; no exploit code |
| **Clear documentation** | Non-team-member can understand methodology |

### 3.3 Deliverables Checklist

- [ ] `docs/week5-evals.md` – Research summary
- [ ] `docs/week5-eval-plan.md` – This document
- [ ] `evals/run_eval.py` – Evaluation harness
- [ ] `evals/metrics.py` – Metric computation
- [ ] `evals/datasets/week5_cases.jsonl` – Labeled dataset
- [ ] `evals/model_adapters/` – Ollama/Anthropic adapters
- [ ] `evals/README.md` – How to run
- [ ] `reports/week5/eval_results.json` – Raw results
- [ ] `reports/week5/eval_results.md` – Formatted report
- [ ] `docs/week5-recommendations.md` – Findings + next steps

---

## 4. Evaluation Methodology

### 4.1 Dataset Design

**Categories:**
| Category | Positive Cases | Negative Cases | Total |
|----------|---------------|----------------|-------|
| Typos | 10 real typos | 10 valid identifiers | 20 |
| Secrets | 10 real-looking fakes | 10 placeholders | 20 |
| SQLi | 10 unsafe patterns | 10 safe patterns | 20 |
| **Total** | 30 | 30 | 60 |

**Case Schema:**
```json
{
  "id": "typo-001",
  "category": "typo",
  "label": "vulnerable",
  "language": "python",
  "snippet": "# This is a teh documentation comment",
  "rationale": "Typo 'teh' should be 'the'",
  "expected_detector": true
}
```

### 4.2 Model Comparison Design

| Model | Type | Purpose |
|-------|------|---------|
| `baseline` | Deterministic only | Establish baseline metrics |
| `ollama:llama3.1:8b` | Local LLM | Primary AI comparison |
| `ollama:mistral:7b` | Local LLM | Secondary comparison |
| `anthropic:claude-3-haiku` | API (optional) | Reference if key exists |

### 4.3 Prompting Strategy

**Classification prompt template:**
```
You are a security code reviewer. Analyze this code snippet and determine if it contains a real security vulnerability or is a false positive.

Category: {category}
Snippet:
```{language}
{snippet}
```

Respond with ONLY one of:
- VULNERABLE: Real security issue requiring fix
- SAFE: False positive, benign pattern, or intentional test/example

Then provide a one-sentence rationale.
```

---

## 5. Risk Mitigation

| Risk | Mitigation |
|------|------------|
| Ollama not installed locally | Graceful fallback; clear error message |
| LLM responses inconsistent | Run 3x, majority vote (optional) |
| Dataset too small for significance | Acknowledge limitation; focus on directional insights |
| Anthropic key not available | Optional; skip gracefully |

---

## 6. Timeline (Week 5)

| Day | Task |
|-----|------|
| 1 | Complete docs, create harness structure |
| 2 | Build dataset (60 cases) |
| 3 | Implement adapters, run baseline eval |
| 4 | Run Ollama comparisons, collect metrics |
| 5 | Write recommendations, finalize reports |
