# Week 4: GitHub Repository Security Scanner

**MIT Blended AI+X Program - Track 3: AI-Enabled Cybersecurity**

---

## Overview

The Week 4 GitHub Repository Security Scanner extends the Week 2 pipeline with:
- **GitHub API integration** for fetching repository metadata
- **Automated cloning/downloading** of repositories for analysis
- **Expanded detection patterns** for SQL injection and secrets
- **Developer-friendly security reports** with intent, attack surface, and risk analysis

## Installation

### Prerequisites

```bash
# Core dependencies
pip install -r requirements.txt

# Optional: requests for GitHub API
pip install requests

# Optional: PyYAML for config file parsing (or use JSON)
pip install pyyaml
```

### Optional Tools

- **gitleaks**: For enhanced secret detection ([install guide](https://github.com/gitleaks/gitleaks#installing))
- **git**: For cloning repositories (falls back to zip download if not available)

## Usage

### Basic Commands

```bash
cd src

# Scan a GitHub repository by owner/name
python -m pipeline.github_agent pallets/flask

# Scan by full URL
python -m pipeline.github_agent https://github.com/psf/requests

# Scan a local directory
python -m pipeline.github_agent --local ./my-project

# Scan all targets from config file
python -m pipeline.github_agent --config ../configs/targets.yaml
```

### Command Line Options

| Option | Description |
|--------|-------------|
| `target` | GitHub repo (owner/repo or URL) or local path with --local |
| `--local`, `-l` | Treat target as a local path instead of GitHub repo |
| `--config`, `-c` | Path to targets config file (YAML/JSON) |
| `--output-dir`, `-o` | Output directory for reports |
| `--use-llm` | Enable LLM for remediation suggestions |
| `--llm-provider` | LLM provider: auto, anthropic, ollama, none (default: none) |
| `--keep-clone` | Keep cloned repository after scanning |
| `--quiet`, `-q` | Suppress progress output |

### Examples

```bash
# Scan Flask with custom output directory
python -m pipeline.github_agent pallets/flask -o ../reports/week4/flask

# Scan with LLM remediation (requires Ollama running)
python -m pipeline.github_agent pallets/click --use-llm --llm-provider ollama

# Batch scan from config
python -m pipeline.github_agent --config ../configs/targets.yaml

# Keep the cloned repo for manual inspection
python -m pipeline.github_agent tiangolo/fastapi --keep-clone
```

## Configuration

### Environment Variables

| Variable | Description |
|----------|-------------|
| `GITHUB_TOKEN` | GitHub Personal Access Token (optional, raises rate limits) |
| `ANTHROPIC_API_KEY` | Anthropic API key for LLM remediation (optional) |

### Target Configuration File

Create a `configs/targets.yaml` or `configs/targets.json`:

**YAML Format:**
```yaml
targets:
  - repo: pallets/flask
    description: Python micro web framework
    language: python
    reason: Popular web framework
    
  - repo: expressjs/express
    description: Node.js web framework
    language: javascript
```

**JSON Format:**
```json
{
  "targets": [
    {"repo": "pallets/flask", "language": "python"},
    {"repo": "expressjs/express", "language": "javascript"}
  ]
}
```

**Simple text format (one repo per line):**
```
pallets/flask
expressjs/express
psf/requests
```

## Output Files

For each scanned repository, the following files are generated:

```
reports/week4/<owner>__<repo>/
├── findings.json       # Machine-readable findings
├── report.md           # Standard markdown report
└── security_report.md  # Developer-friendly security report (NEW)
```

### Security Report Contents

The `security_report.md` includes:

1. **Executive Summary**
   - Overall risk level
   - Findings by severity
   - Findings by category

2. **Severity Guide**
   - Explanation of severity levels
   - Response time recommendations

3. **Findings Overview**
   - Quick-reference table of all findings

4. **Detailed Findings**
   - For each finding:
     - **Intent**: What the code appears to be doing
     - **Attack Surface**: Where user input enters and flows
     - **Risk Assessment**: Impact and likelihood
     - **Recommended Fix**: Concrete remediation steps
     - **Verification**: How to confirm the fix

5. **General Recommendations**
   - Immediate actions
   - Preventive measures

## Detection Capabilities

### SQL Injection Patterns

| Language | Patterns Detected |
|----------|-------------------|
| Python | `cursor.execute()` with string concatenation, f-strings, `.format()`, SQLAlchemy `text()`, Django `raw()` |
| JavaScript | Template literals with `${...}`, string concatenation, Sequelize raw queries, Knex raw |
| PHP | `mysql_query()`, `mysqli_query()`, PDO queries with concatenation |

### Secret Detection

| Provider | Pattern Types |
|----------|---------------|
| GitHub | PAT, Fine-grained PAT, OAuth tokens |
| AWS | Access Key ID, Secret Key, STS tokens |
| OpenAI | API keys (sk-*) |
| Slack | Bot tokens, webhooks |
| Stripe | Live/test keys |
| Google Cloud | API keys |
| Twilio | API keys, Account SID |
| Database | Connection strings (MongoDB, PostgreSQL, MySQL, Redis) |
| Generic | Private keys, JWT tokens, passwords |

## Rate Limiting

### GitHub API Limits

| Authentication | Rate Limit |
|----------------|------------|
| Unauthenticated | 60 requests/hour |
| With `GITHUB_TOKEN` | 5,000 requests/hour |

The scanner handles rate limits gracefully:
- Displays warning when rate limited
- Falls back to direct clone/download without metadata
- Adds small delays between batch scans

### Recommended Setup

For batch scanning, set up a GitHub token:

```bash
# Create a token at https://github.com/settings/tokens
# Only need public_repo scope for public repositories
export GITHUB_TOKEN=ghp_yourtoken

# Or on Windows PowerShell
$env:GITHUB_TOKEN = "ghp_yourtoken"
```

## Ethical Guidelines

This tool is designed for **defensive security analysis only**:

- ✅ Static code analysis
- ✅ Pattern identification
- ✅ Documentation review
- ❌ Runtime exploitation
- ❌ Automated PR submissions
- ❌ Public disclosure without coordination

### If You Find Real Vulnerabilities

1. **Do NOT** publicly disclose specific details
2. **Contact** the maintainers privately
3. **Follow** their security policy (often in SECURITY.md)
4. **Allow** reasonable time for patches
5. **Report** responsibly per project guidelines

## Troubleshooting

### Common Issues

**"requests library not available"**
```bash
pip install requests
```

**"git not found"**
- The scanner will fall back to zip download
- Install git for faster cloning: [git-scm.com](https://git-scm.com/)

**Rate limit exceeded**
- Set `GITHUB_TOKEN` environment variable
- Reduce batch size
- Wait for rate limit reset

**Clone timeout**
- Large repos may timeout (5 min limit)
- Use `--keep-clone` to inspect partial results
- Consider scanning a specific branch

**False positives**
- Review findings manually
- Many patterns are intentionally sensitive
- Check if matches are in test/example code

---

*Week 4 - MIT Blended AI+X PBL - AI-Enabled Cybersecurity*
