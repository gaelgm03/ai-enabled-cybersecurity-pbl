# Scripts Directory

This directory contains utility scripts for running the security scanning pipeline against test projects.

---

## Available Scripts

### scan-test-labs.ps1 (Windows PowerShell)

**Purpose:** Run the vulnerability detection pipeline against the `test/sqli-labs/` directory.

**What it does:**
1. Runs TypoDetector (codespell) to find spelling errors
2. Runs SecretDetector (gitleaks/regex) to find hardcoded credentials
3. Runs DependencyDetector (pip-audit/npm audit) to find vulnerable dependencies
4. Generates reports in JSON and Markdown formats

**Usage:**
```powershell
# Basic execution (with LLM remediation)
.\scripts\scan-test-labs.ps1

# Fast execution without LLM (uses template-based remediation)
.\scripts\scan-test-labs.ps1 -NoLLM

# Suppress progress output
.\scripts\scan-test-labs.ps1 -Quiet
```

**Options:**
| Parameter | Description |
|-----------|-------------|
| `-NoLLM` | Disable LLM-based remediation (faster) |
| `-Quiet` | Suppress progress messages |

---

### scan-test-labs.sh (Linux/Mac Bash)

**Purpose:** Provides the same functionality as the Windows version for Linux/Mac environments.

**Usage:**
```bash
# Grant execute permission (first time only)
chmod +x scripts/scan-test-labs.sh

# Basic execution
./scripts/scan-test-labs.sh

# Fast execution without LLM
./scripts/scan-test-labs.sh --no-llm

# Suppress progress output
./scripts/scan-test-labs.sh --quiet
```

**Options:**
| Parameter | Description |
|-----------|-------------|
| `--no-llm` | Disable LLM-based remediation |
| `--quiet` | Suppress progress messages |

---

## Output Files

After running the scripts, the following files are generated:

| File | Format | Purpose |
|------|--------|---------|
| `reports/test-sqli-labs/findings.json` | JSON | Machine-readable, for tool integration |
| `reports/test-sqli-labs/report.md` | Markdown | Human-readable, for review |

---

## Prerequisites

### Required
- Python 3.8 or higher
- Dependencies installed via `pip install -r requirements.txt`

### Recommended (for better accuracy)
- **codespell**: Required for typo detection (`pip install codespell`)
- **gitleaks**: Improves secret detection accuracy ([installation guide](https://github.com/gitleaks/gitleaks#installing))

### Optional (for LLM remediation)
- **Anthropic API**: Set `ANTHROPIC_API_KEY` environment variable
- **Ollama**: Local LLM, free ([ollama.com](https://ollama.com))

---

## Related Documentation

- [Pipeline Documentation](../docs/week2-pipeline.md)
- [Project README](../README.md)
