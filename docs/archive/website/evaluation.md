---
layout: default
title: LLM Evaluation
nav_order: 7
---

# LLM Evaluation Framework

A systematic evaluation comparing AI (LLM) methods versus deterministic approaches for vulnerability classification, measuring precision, recall, and false positive rates.

---

## Research Question

**Can LLMs improve vulnerability detection accuracy compared to deterministic (regex-based) methods?**

Specifically, we investigated whether LLMs can:
- Reduce false positive rates by understanding context
- Distinguish real vulnerabilities from benign patterns
- Provide value beyond pattern matching alone

---

## Evaluation Categories

### Cybersecurity-Relevant LLM Eval Taxonomy

| Category | What It Measures | Relevance |
|----------|------------------|-----------|
| **Code Vulnerability Detection** | Identifying security vulnerabilities | High - Core function |
| **Secure Coding Remediation** | Quality of fix suggestions | High - LLM remediation |
| **False Positive Discrimination** | Real vuln vs. benign pattern | Critical - Main value-add |
| **Prompt Injection Robustness** | Resistance to adversarial inputs | Medium |
| **Policy Compliance** | Consistent severity ratings | Medium |

### False Positive Discrimination (Focus Area)

Our primary focus was on whether LLMs can reduce false positives:

| Sub-category | Example | Challenge |
|--------------|---------|-----------|
| **Typo vs Identifier** | "teh" typo vs `teh` variable name | Requires semantic understanding |
| **Secret vs Placeholder** | Real API key vs `YOUR_API_KEY_HERE` | Requires pattern recognition |
| **Unsafe SQL vs Safe ORM** | String concat vs parameterized query | Requires code analysis |
| **Test/Doc Context** | Vuln in test file vs production code | Requires file context |

---

## Methodology

### Dataset

We created a labeled dataset with **60 test cases**:

- **Balanced:** ~50% positive (real vulns), ~50% negative (false positives/safe patterns)
- **Multi-category:** Typos, secrets, SQLi patterns
- **Multi-language:** Python, JavaScript, PHP
- **Labeled:** Ground truth with rationale for each case
- **Safe:** No real secrets; synthetic/placeholder values only

### Dataset Format

```json
{
  "id": "typo-001",
  "category": "typo",
  "label": "vulnerable",
  "language": "python",
  "snippet": "# This is teh main function",
  "rationale": "Typo 'teh' should be 'the'",
  "expected_detector": true
}
```

### Models Compared

| Model | Type | Cost | Notes |
|-------|------|------|-------|
| **Baseline** | Deterministic (regex) | Free | No AI, pattern matching only |
| **Ollama llama3.1:8b** | Local LLM | Free | Reproducible, offline |
| **Anthropic Claude** | API LLM | Paid | Reference point (when available) |

### Metrics

| Metric | Definition | Why It Matters |
|--------|------------|----------------|
| **Precision** | TP / (TP + FP) | Reduces developer alert fatigue |
| **Recall** | TP / (TP + FN) | Ensures real vulns aren't missed |
| **F1 Score** | Harmonic mean of P & R | Balanced overall performance |
| **False Positive Rate** | FP / (FP + TN) | Critical for adoption |
| **Latency** | Time per classification | Practical deployment |

---

## Results

### Overall Comparison

| Model | Precision | Recall | F1 | FPR | Accuracy | Latency |
|-------|-----------|--------|-----|-----|----------|---------|
| **Baseline** | **0.91** | **0.67** | **0.77** | **0.07** | **0.80** | <1ms |
| Ollama llama3.1:8b | 0.72 | 0.43 | 0.54 | 0.17 | 0.60 | ~54s |

### Per-Category Results

#### SECRET Detection

| Model | Precision | Recall | F1 | FPR |
|-------|-----------|--------|-----|-----|
| Baseline | 0.86 | 0.60 | 0.71 | 0.10 |

#### SQLI Detection

| Model | Precision | Recall | F1 | FPR |
|-------|-----------|--------|-----|-----|
| Baseline | 1.00 | 0.60 | 0.75 | 0.00 |

#### TYPO Detection

| Model | Precision | Recall | F1 | FPR |
|-------|-----------|--------|-----|-----|
| Baseline | 0.89 | 0.80 | 0.84 | 0.10 |

---

## Analysis

### Key Findings

#### 1. Deterministic Methods Outperform Overall

The baseline (regex-based) detector achieved:
- **Higher precision** (91% vs 72%)
- **Higher recall** (67% vs 43%)
- **Better F1 score** (0.77 vs 0.54)
- **Lower false positive rate** (7% vs 17%)
- **Dramatically faster** (<1ms vs ~54s)

#### 2. LLMs Show Promise in Specific Areas

While overall performance was lower, LLMs demonstrated potential for:
- **Contextual understanding** of placeholder values
- **Semantic analysis** of variable names
- **Nuanced classification** in ambiguous cases

#### 3. Latency is a Significant Factor

LLM classification is **~54,000x slower** than regex matching:
- Baseline: <1ms per case
- Ollama: ~54s per case

For large codebases, this latency is prohibitive for primary detection.

### Where AI Helps

- **False positive reduction:** AI can potentially distinguish real vulnerabilities from benign patterns
- **Context awareness:** AI understands that placeholder values like `YOUR_API_KEY` are not real secrets
- **Semantic understanding:** AI can identify that variable names like `teh` may be intentional identifiers

### Where AI May Fail

- **Inconsistent responses:** Same input may get different classifications across runs
- **Hallucination risk:** AI may invent rationales not supported by the code
- **Latency cost:** AI classification is significantly slower than regex matching
- **Reliability:** Lower overall accuracy than deterministic methods

---

## Recommendations

### Hybrid Approach

Based on our findings, we recommend a **hybrid architecture**:

```
┌─────────────────┐
│  Deterministic  │ ← Primary detection (fast, reliable)
│    Detectors    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   LLM Filter    │ ← Secondary FP reduction (optional)
│   (Optional)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Human Review   │ ← Final validation (required)
└─────────────────┘
```

### Use LLMs For:

1. **Remediation guidance** - Generating human-readable fix instructions
2. **Explanation** - Describing why a pattern is vulnerable
3. **Secondary filtering** - Reducing false positives on high-confidence findings
4. **Complex cases** - When semantic understanding provides clear value

### Use Deterministic Methods For:

1. **Primary detection** - All initial vulnerability identification
2. **High-volume scanning** - CI/CD integration, large codebases
3. **Reproducibility** - Consistent results across runs
4. **Speed-critical applications** - Real-time scanning

---

## Evaluation Framework Usage

### Running Evaluations

```bash
# Basic (baseline only)
python -m evals.run_eval --models baseline

# With Ollama models
python -m evals.run_eval --models baseline,ollama:llama3.1:8b

# With Anthropic (if key available)
python -m evals.run_eval --models baseline,anthropic --api-key YOUR_KEY

# All options
python -m evals.run_eval \
  --dataset evals/datasets/week5_cases.jsonl \
  --models baseline,ollama:llama3.1:8b \
  --out reports/week5 \
  --quiet
```

### Output Files

- `eval_results.json` - Full results with per-case details
- `eval_results.md` - Markdown summary with tables

---

## Framework Structure

```
evals/
├── __init__.py
├── run_eval.py          # Main harness entry point
├── metrics.py           # Metric computation
├── model_adapters/
│   ├── __init__.py
│   ├── base_adapter.py       # Abstract base class
│   ├── baseline_adapter.py   # Regex-only implementation
│   ├── ollama_adapter.py     # Local LLM implementation
│   └── anthropic_adapter.py  # API LLM implementation
├── datasets/
│   └── week5_cases.jsonl     # Test cases
└── README.md
```

---

## Limitations

1. **Small dataset** (N=60) - Results are directional, not statistically rigorous
2. **LLM variability** - Responses may vary between runs (temperature, model version)
3. **Latency approximation** - Actual latency depends on hardware and network
4. **Classification focus** - Tests classification, not end-to-end discovery
5. **Limited models** - Only tested subset of available LLMs

---

## Future Work

1. **Larger dataset** - Expand to 500+ cases for statistical significance
2. **More models** - Test Claude, GPT-4, Gemini, and specialized security models
3. **Prompt engineering** - Optimize prompts for better classification
4. **Fine-tuning** - Train specialized models on security data
5. **Hybrid evaluation** - Measure combined deterministic + LLM performance

---

## References

- Meta CyberSecEval: [github.com/meta-llama/PurpleLlama](https://github.com/meta-llama/PurpleLlama)
- OWASP Benchmark: [owasp.org/www-project-benchmark](https://owasp.org/www-project-benchmark/)
- Our Detectors: [`src/pipeline/detectors/`](https://github.com/YOUR_USERNAME/ai-enabled-cybersecurity-pbl/tree/main/src/pipeline/detectors)

---

## Source Code

- **Evaluation Framework:** [`evals/`](https://github.com/YOUR_USERNAME/ai-enabled-cybersecurity-pbl/tree/main/evals)
- **Results:** [`reports/week5/`](https://github.com/YOUR_USERNAME/ai-enabled-cybersecurity-pbl/tree/main/reports/week5)
- **Documentation:** [`docs/week5-evals.md`](https://github.com/YOUR_USERNAME/ai-enabled-cybersecurity-pbl/blob/main/docs/week5-evals.md)

---

*MIT Blended AI+X PBL - Track 3: AI-Enabled Cybersecurity*
