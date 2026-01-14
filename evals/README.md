# Week 5 Evaluation Framework

**MIT Blended AI+X PBL – AI-Enabled Cybersecurity**

Lightweight evaluation harness for measuring LLM ability to classify security vulnerabilities and reduce false positives.

---

## Quick Start

```bash
# From repository root
python -m evals.run_eval --dataset evals/datasets/week5_cases.jsonl --models baseline,ollama:llama3.1:8b --out reports/week5
```

## Requirements

- Python 3.8+
- **Optional:** Ollama (for local LLM evaluation)
- **Optional:** `anthropic` package + API key (for Claude evaluation)

### Install Ollama (optional)

```bash
# macOS/Linux
curl -fsSL https://ollama.com/install.sh | sh

# Pull a model
ollama pull llama3.1:8b
ollama pull mistral:7b  # alternative
```

### Install Anthropic SDK (optional)

```bash
pip install anthropic
export ANTHROPIC_API_KEY="your-key-here"
```

---

## Usage

### Basic (baseline only)

```bash
python -m evals.run_eval --models baseline
```

### With Ollama models

```bash
python -m evals.run_eval --models baseline,ollama:llama3.1:8b,ollama:mistral:7b
```

### With Anthropic (if key available)

```bash
python -m evals.run_eval --models baseline,ollama:llama3.1:8b,anthropic --api-key YOUR_KEY
```

### All options

```bash
python -m evals.run_eval \
  --dataset evals/datasets/week5_cases.jsonl \
  --models baseline,ollama:llama3.1:8b \
  --out reports/week5 \
  --quiet
```

---

## Dataset Format

Test cases are stored in JSONL format (`evals/datasets/week5_cases.jsonl`):

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

### Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique case identifier |
| `category` | string | One of: `typo`, `secret`, `sqli` |
| `label` | string | Ground truth: `vulnerable` or `safe` |
| `language` | string | Programming language |
| `snippet` | string | Code snippet to classify |
| `rationale` | string | Why this label is correct |
| `expected_detector` | bool | Whether baseline should flag this |

---

## Output

Results are written to the output directory:

- `eval_results.json` - Full results with per-case details
- `eval_results.md` - Markdown summary with tables

### Metrics

| Metric | Definition |
|--------|------------|
| **Precision** | TP / (TP + FP) |
| **Recall** | TP / (TP + FN) |
| **F1** | 2 × (P × R) / (P + R) |
| **FPR** | FP / (FP + TN) |
| **Accuracy** | (TP + TN) / Total |

---

## Model Adapters

| Adapter | Model Spec | Notes |
|---------|------------|-------|
| Baseline | `baseline` | Regex-only, no AI |
| Ollama | `ollama:MODEL` | Local LLM (e.g., `ollama:llama3.1:8b`) |
| Anthropic | `anthropic` or `anthropic:MODEL` | API-based (requires key) |

---

## Directory Structure

```
evals/
├── __init__.py
├── run_eval.py          # Main harness entry point
├── metrics.py           # Metric computation
├── model_adapters/
│   ├── __init__.py
│   ├── base_adapter.py
│   ├── baseline_adapter.py
│   ├── ollama_adapter.py
│   └── anthropic_adapter.py
├── datasets/
│   └── week5_cases.jsonl
└── README.md
```

---

## Limitations

- Small dataset (~60 cases) - results are directional, not statistically rigorous
- LLM responses may vary between runs (temperature, model version)
- Latency/cost metrics are approximate
- Does not test end-to-end pipeline integration

---

## Adding New Test Cases

1. Add cases to `datasets/week5_cases.jsonl`
2. Follow the schema above
3. Use synthetic/placeholder secrets only (no real credentials)
4. Include clear rationale for ground truth label

---

*MIT Blended AI+X PBL - Week 5*
