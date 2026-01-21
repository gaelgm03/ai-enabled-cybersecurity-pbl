---
layout: default
title: Security Scan Pipeline
nav_order: 3
---

# Security Scan Pipeline

The core of our project is a modular security scanning pipeline that detects common vulnerabilities in codebases using deterministic tools, with optional LLM-powered remediation guidance.

---

## Overview

The pipeline detects four categories of security issues:

| Detector | Tool | Purpose |
|----------|------|---------|
| **TypoDetector** | codespell | Spelling errors in code and documentation |
| **SecretDetector** | gitleaks/regex | Accidentally committed credentials |
| **DependencyDetector** | pip-audit/npm audit | Known vulnerable packages |
| **SQLiDetector** | YAML patterns | SQL injection vulnerabilities |

---

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Pipeline Entry                        │
│                  (python -m pipeline.main)               │
└─────────────────────────┬───────────────────────────────┘
                          │
          ┌───────────────┼───────────────┐
          ▼               ▼               ▼
    ┌──────────┐   ┌──────────┐   ┌──────────────┐
    │  Typo    │   │  Secret  │   │  Dependency  │
    │ Detector │   │ Detector │   │   Detector   │
    │(codespell│   │(gitleaks/│   │ (pip-audit/  │
    │          │   │  regex)  │   │  npm audit)  │
    └────┬─────┘   └────┬─────┘   └──────┬───────┘
         │              │                │
         └──────────────┼────────────────┘
                        ▼
              ┌─────────────────┐
              │   Redaction     │
              │     Layer       │
              └────────┬────────┘
                       ▼
              ┌─────────────────┐
              │  Unified Schema │
              │   (Finding)     │
              └────────┬────────┘
                       ▼
              ┌─────────────────┐
              │ LLM Remediation │
              │   (Optional)    │
              └────────┬────────┘
                       ▼
         ┌─────────────┴─────────────┐
         ▼                           ▼
   ┌───────────┐              ┌────────────┐
   │   JSON    │              │  Markdown  │
   │  Report   │              │   Report   │
   └───────────┘              └────────────┘
```

---

## Key Design Decisions

### 1. Deterministic Detection

All scanning uses established tools and patterns—**not LLM inference**. This ensures:
- Consistent, reproducible results
- Auditable detection behavior
- No hallucination risk in vulnerability identification

### 2. Redaction Layer

**Critical safety feature:** Secrets are never stored or displayed in full.

```
Original:  sk-abc123xyz789abcdef
Redacted:  sk-a********cdef
```

The `Redactor` class ensures that:
- All secrets pass through redaction before storage
- LLM prompts never contain actual credential values
- Reports show only partial, redacted values

### 3. LLM for Remediation Only

LLMs generate human-readable fix instructions from **redacted context**:

| LLM Receives | LLM Does NOT Receive |
|--------------|---------------------|
| Finding type and severity | Raw secret values |
| File path and line number | Full file contents |
| Redacted match value | Actual credentials |
| Package names/versions | Repository access tokens |

### 4. Multiple LLM Backends

| Provider | Cost | Requirements | Best For |
|----------|------|--------------|----------|
| `anthropic` | Paid | `ANTHROPIC_API_KEY` | Production, high quality |
| `ollama` | Free | Ollama running locally | Development, offline use |
| `none` | Free | None | Quick scans, CI/CD |

**Auto-selection priority:** anthropic → ollama → templates

---

## Unified Finding Schema

All detectors produce findings in a common format:

```json
{
  "finding_type": "secret | typo | dependency | sqli",
  "severity": "low | medium | high | critical",
  "title": "Human-readable title",
  "description": "Detailed description of the issue",
  "file_path": "/path/to/file",
  "line_number": 42,
  "detector": "codespell | gitleaks | pip-audit | sqli",
  "raw_match": "[REDACTED]",
  "redacted_match": "sk-a****789",
  "remediation": "LLM-generated fix instructions",
  "prevention": "LLM-generated prevention guidance",
  "metadata": { ... }
}
```

### Severity Levels

| Level | Description | Examples |
|-------|-------------|----------|
| **Critical** | Immediate action required | Exposed AWS keys, private keys |
| **High** | Serious security risk | API keys, vulnerable deps with exploits |
| **Medium** | Moderate risk | JWT tokens, outdated packages |
| **Low** | Minor issues | Typos, informational findings |

---

## Usage

### Basic Usage

```bash
# From the project root
cd ai-enabled-cybersecurity-pbl

# Install dependencies
pip install -r requirements.txt

# Run the pipeline
cd src
python -m pipeline.main ..
```

### Command-Line Options

```bash
python -m pipeline.main [target] [options]

Arguments:
  target              Directory to scan (default: current directory)

Options:
  --output-dir, -o    Output directory for reports
  --llm-provider      LLM provider: auto, anthropic, ollama, none
  --no-llm            Disable LLM remediation (use templates)
  --api-key           Anthropic API key
  --check-tools       Check available scanning tools
  --quiet, -q         Suppress progress output
```

### Examples

```bash
# Scan current directory (auto-selects LLM provider)
python -m pipeline.main .

# Scan a specific project
python -m pipeline.main ./my-project --output-dir reports/my-project

# Use local Ollama for remediation
python -m pipeline.main . --llm-provider ollama

# Quick scan without LLM (templates only)
python -m pipeline.main . --no-llm

# Check tool availability
python -m pipeline.main --check-tools
```

---

## GitHub Agent (Week 4 Extension)

The pipeline was extended to scan GitHub repositories directly:

```bash
# Scan a GitHub repository
python -m pipeline.github_agent pallets/flask

# Scan by URL
python -m pipeline.github_agent https://github.com/psf/requests

# Scan a local directory
python -m pipeline.github_agent --local ./my-project

# Batch scan from config file
python -m pipeline.github_agent --config ../configs/targets.yaml
```

### Output Files

```
reports/week4/<owner>__<repo>/
├── findings.json        # Machine-readable findings
├── report.md            # Standard markdown report
└── security_report.md   # Developer-friendly security report
```

### Security Report Contents

The `security_report.md` includes:
- **Executive Summary** with risk level and category breakdown
- **Detailed Findings** with:
  - Intent: What the code is trying to do
  - Attack Surface: Where user input flows
  - Risk Assessment: Impact and likelihood
  - Recommended Fix: Concrete remediation steps
  - Verification: How to confirm the fix

---

## Local LLM via Ollama (Free)

Ollama allows running LLMs locally without API keys or cloud costs.

### Setup

```bash
# Install Ollama from ollama.com

# Pull a model
ollama pull llama3.1:8b

# Verify Ollama is running
ollama list
```

### Recommended Models

| Model | Size | Speed | Quality |
|-------|------|-------|---------|
| `llama3.1:8b` | ~4.7GB | Fast | Good (default) |
| `llama3.1:70b` | ~40GB | Slow | Excellent |
| `mistral:7b` | ~4.1GB | Fast | Good |
| `codellama:7b` | ~3.8GB | Fast | Good for code |

---

## Output Examples

### Check Tools Output

```
[*] Checking available tools...

  Detectors:
    [OK] codespell
    [--] gitleaks (will use regex fallback)
    [OK] pip-audit
    [--] npm (not installed)

  LLM Providers:
    [--] anthropic (no ANTHROPIC_API_KEY)
    [OK] ollama (running at localhost:11434)

    Auto-selected provider: ollama
```

### Markdown Report Example

```markdown
# Security Scan Report

## Summary
- **Total Findings:** 5
- **Critical:** 1 | **High:** 2 | **Medium:** 1 | **Low:** 1

## Findings

### 🔐 Secret Exposure (HIGH)
**File:** src/config.py:42
**Match:** `sk-a****789`

**Remediation:**
1. Immediately rotate the exposed credential
2. Remove from source code
3. Use environment variables instead
...
```

---

## Limitations

1. **Detection Coverage:** Regex patterns may miss novel secret formats
2. **False Positives:** Some matches may be test data or placeholders
3. **Transitive Dependencies:** pip-audit may not catch all transitive vulnerabilities
4. **LLM Accuracy:** Remediation instructions should be reviewed by a human
5. **Training Data Cutoff:** LLM may not know about very recent CVEs
6. **No Runtime Analysis:** This is static analysis only

---

## Source Code

- **Main Pipeline:** [`src/pipeline/main.py`](https://github.com/YOUR_USERNAME/ai-enabled-cybersecurity-pbl/blob/main/src/pipeline/main.py)
- **GitHub Agent:** [`src/pipeline/github_agent.py`](https://github.com/YOUR_USERNAME/ai-enabled-cybersecurity-pbl/blob/main/src/pipeline/github_agent.py)
- **Detectors:** [`src/pipeline/detectors/`](https://github.com/YOUR_USERNAME/ai-enabled-cybersecurity-pbl/tree/main/src/pipeline/detectors)
- **Reporters:** [`src/pipeline/reporters/`](https://github.com/YOUR_USERNAME/ai-enabled-cybersecurity-pbl/tree/main/src/pipeline/reporters)

---

*MIT Blended AI+X PBL - Track 3: AI-Enabled Cybersecurity*
