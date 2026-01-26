# Week 2: Security Scanning Pipeline

**MIT Blended AI+X PBL - AI-Enabled Cybersecurity (Track 3)**

---

## Overview

This document describes the Week 2 security scanning pipeline, which detects common security issues in codebases:

1. **Typos** - Spelling errors that could affect code quality or documentation
2. **Secrets** - Accidentally committed API keys, tokens, and credentials
3. **Vulnerable Dependencies** - Outdated packages with known CVEs

The pipeline uses **deterministic detection** with industry-standard tools, and optionally leverages an **LLM for generating remediation instructions** from redacted context.

**Supported LLM Providers:**
- **Anthropic Claude** - Cloud API (requires API key)
- **Ollama** - Local LLM (free, no API key required)
- **Templates** - Built-in fallback (always available)

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

## Tools Used

| Tool | Purpose | Installation |
|------|---------|--------------|
| **codespell** | Typo detection | `pip install codespell` |
| **gitleaks** | Secret detection | [GitHub Releases](https://github.com/gitleaks/gitleaks) |
| **pip-audit** | Python dependency vulnerabilities | `pip install pip-audit` |
| **npm audit** | Node.js dependency vulnerabilities | Included with npm |
| **anthropic** | Cloud LLM remediation | `pip install anthropic` |
| **Ollama** | Local LLM remediation (free) | [ollama.com](https://ollama.com) |

### Fallback Behavior

- If **gitleaks** is not installed, the pipeline uses built-in regex patterns for secret detection
- LLM provider auto-selection: `anthropic` (if API key) → `ollama` (if running) → `templates`

---

## Unified Finding Schema

All detectors produce findings in a unified format:

```json
{
  "finding_type": "secret | typo | dependency",
  "severity": "low | medium | high | critical",
  "title": "Human-readable title",
  "description": "Detailed description of the issue",
  "file_path": "/path/to/file",
  "line_number": 42,
  "detector": "codespell | gitleaks | pip-audit | ...",
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

## Redaction Layer

**CRITICAL**: The pipeline never stores or displays full secrets.

### Redaction Strategy

1. Secrets are detected by gitleaks or regex patterns
2. Before storage, secrets are passed through `Redactor.redact_secret()`
3. Only redacted values appear in:
   - Finding objects
   - JSON reports
   - Markdown reports
   - LLM prompts

### Example

```
Original:  sk-abc123xyz789abcdef
Redacted:  sk-a********cdef
```

### Secret Type Detection

The redactor can identify common secret types:
- OpenAI API Keys (`sk-...`)
- GitHub PATs (`ghp_...`, `github_pat_...`)
- AWS Access Keys (`AKIA...`)
- Slack Tokens (`xox...`)
- Private Keys (`-----BEGIN...`)
- And more...

---

## LLM Integration

The LLM is used **ONLY** for generating human-readable remediation instructions from **redacted context**.

### Safety Guarantees

1. **No raw secrets** are ever sent to the LLM
2. LLM receives only:
   - Finding type and severity
   - File path and line number
   - Redacted match value
   - Package names and versions (for dependencies)
3. LLM does **NOT** perform detection (deterministic tools do)

### LLM Provider Selection

The pipeline supports multiple LLM backends:

| Provider | Cost | Requirements | Best For |
|----------|------|--------------|----------|
| `anthropic` | Paid | `ANTHROPIC_API_KEY` | Production, high quality |
| `ollama` | Free | Ollama running locally | Development, offline use |
| `none` | Free | None | Quick scans, CI/CD |

**Auto-selection priority:** `anthropic` → `ollama` → `templates`

### Anthropic Claude Configuration

```bash
# Set environment variable
export ANTHROPIC_API_KEY=your-api-key

# Or pass directly
python -m pipeline.main . --api-key your-api-key
```

---

## Local LLM via Ollama (Free)

Ollama allows you to run LLMs locally without any API keys or cloud costs.

### Setup

1. **Install Ollama** from [ollama.com](https://ollama.com)

2. **Pull the model:**
   ```bash
   ollama pull llama3.1:8b
   ```

3. **Verify Ollama is running:**
   ```bash
   ollama list
   ```

### Usage

```bash
# Auto-detect (uses Ollama if running and no Anthropic key)
python -m pipeline.main .

# Explicitly use Ollama
python -m pipeline.main . --llm-provider ollama

# Check if Ollama is detected
python -m pipeline.main --check-tools
```

### Configuration

| Environment Variable | Default | Description |
|---------------------|---------|-------------|
| `OLLAMA_BASE_URL` | `http://localhost:11434` | Ollama API endpoint |
| `OLLAMA_MODEL` | `llama3.1:8b` | Model to use for remediation |

```bash
# Use a different model
export OLLAMA_MODEL=mistral:7b
python -m pipeline.main . --llm-provider ollama

# Use a remote Ollama instance
export OLLAMA_BASE_URL=http://192.168.1.100:11434
python -m pipeline.main . --llm-provider ollama
```

### Recommended Models

| Model | Size | Speed | Quality |
|-------|------|-------|--------|
| `llama3.1:8b` | ~4.7GB | Fast | Good (default) |
| `llama3.1:70b` | ~40GB | Slow | Excellent |
| `mistral:7b` | ~4.1GB | Fast | Good |
| `codellama:7b` | ~3.8GB | Fast | Good for code |

### Troubleshooting

- **"Ollama connection failed"**: Ensure Ollama is running (`ollama serve`)
- **Slow responses**: Try a smaller model or increase timeout
- **Out of memory**: Use a smaller model (7B instead of 70B)

---

### Template Fallback

If no LLM provider is available, the pipeline uses built-in templates:

```python
# Secret template example
"""
1. Immediately rotate the exposed credential
2. Review git history to ensure the secret is not in previous commits
3. Remove the hardcoded secret from the code
4. Use environment variables or a secrets manager instead
"""
```

---

## Usage

### Basic Usage

```bash
# From the project root
cd ai-enabled-cybersecurity-pbl

# Install dependencies
pip install -r requirements.txt

# Run the pipeline
python -m pipeline.main .
```

### Command-Line Options

```bash
python -m pipeline.main [target] [options]

Arguments:
  target              Directory to scan (default: current directory)

Options:
  --output-dir, -o    Output directory for reports (default: reports/week2)
  --llm-provider      LLM provider: auto, anthropic, ollama, none (default: auto)
  --no-llm            Disable LLM remediation (use templates)
  --api-key           Anthropic API key (or use ANTHROPIC_API_KEY env var)
  --check-tools       Check which scanning tools are available
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

# Check tool and LLM provider availability
python -m pipeline.main --check-tools
```

---

## Output

The pipeline generates two reports:

### 1. JSON Report (`findings.json`)

Machine-readable format for integration with other tools:

```json
{
  "scan_id": "scan-20241224-123456-abc123",
  "timestamp": "2024-12-24T12:34:56Z",
  "target_path": "/path/to/project",
  "summary": {
    "total_findings": 5,
    "by_type": {"secret": 2, "dependency": 2, "typo": 1},
    "by_severity": {"critical": 1, "high": 2, "medium": 1, "low": 1}
  },
  "findings": [...]
}
```

### 2. Markdown Report (`report.md`)

Human-readable format for review and presentation:

- Summary statistics with severity breakdown
- Detailed findings grouped by type
- Remediation and prevention guidance
- Visual indicators (emoji) for severity levels

---

## Limitations

1. **Detection Coverage**: Regex patterns may miss novel secret formats
2. **False Positives**: Some matches may be test data or placeholders
3. **Transitive Dependencies**: pip-audit may not catch all transitive vulnerabilities
4. **LLM Accuracy**: Remediation instructions should be reviewed by a human
5. **Training Data Cutoff**: LLM may not know about very recent CVEs
6. **No Runtime Analysis**: This is static analysis only

---

## Security Considerations

- **Never commit real secrets** to test the secret detector
- The pipeline is for **educational and defensive purposes only**
- All findings should be **validated by a human** before action
- API keys for the LLM should be stored securely (env vars, not in code)

---

## Next Steps

1. **CI/CD Integration**: Add pipeline to GitHub Actions
2. **Custom Rules**: Support custom secret patterns
3. **Ignore Lists**: Allow excluding known false positives
4. **SARIF Output**: Standard format for IDE integration
5. **Historical Scanning**: Scan git history for past secrets

---

## Testing

### Smoke Tests

```bash
# Test with templates (always works)
python -m pipeline.main . --no-llm

# Test with Ollama (if installed)
python -m pipeline.main . --llm-provider ollama

# Test tool detection
python -m pipeline.main --check-tools
```

### Expected Output

With `--check-tools`:
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

---

## References

- [codespell](https://github.com/codespell-project/codespell)
- [gitleaks](https://github.com/gitleaks/gitleaks)
- [pip-audit](https://github.com/pypa/pip-audit)
- [Ollama](https://ollama.com)
- [OWASP Dependency Check](https://owasp.org/www-project-dependency-check/)
- [Anthropic Claude API](https://docs.anthropic.com/)

---

*Week 2 - MIT Blended AI+X PBL - AI-Enabled Cybersecurity*
