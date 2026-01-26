# AI-Enabled Cybersecurity (PBL)

## MIT Blended AI+X Program  
**Project-Based Learning: AI in Cybersecurity – Anthropic Project**  
**Track 3: AI-Enabled Cybersecurity**

---

## 📌 Project Overview

This repository contains the work for the **AI in Cybersecurity Project-Based Learning (PBL)** as part of the **MIT Blended AI+X Program**.

The project explores how **Large Language Models (LLMs)** can be used to **assist defensive cybersecurity tasks**, such as identifying software vulnerabilities, supporting security audits, and automating parts of penetration testing workflows—while carefully considering the **risks, limitations, and ethical concerns** introduced by AI systems.

---

## 📄 Key Deliverables

| Document | Description |
|----------|-------------|
| **[Final Paper](docs/final-paper.md)** | Academic-style paper presenting our hybrid detection approach |
| **[Evaluation Results](reports/week5/eval_results.md)** | Quantitative comparison of baseline vs. LLM detection |
| **[Responsible Innovation Essay](docs/week6-responsible-innovation-essay.md)** | Ethical considerations for security tooling |

---

## 🔬 Key Findings

- **Deterministic detection outperforms LLMs:** Baseline detectors achieved F1=0.77 (91% precision, 67% recall) vs. F1=0.54 for the best LLM configuration
- **LLMs add value in specific contexts:** SQL injection detection showed LLM advantage (F1=0.86 vs 0.75); remediation generation benefits from AI assistance
- **Hybrid architectures are the pragmatic path forward:** Separate detection (deterministic) from explanation (LLM-assisted) to capture benefits of both approaches

---

## 🎯 Project Goals

- Understand how LLMs introduce **new security risks and attack surfaces**
- Explore how AI can support **defensive cybersecurity workflows**
- Identify common **software vulnerabilities** and how AI may assist in detecting or explaining them
- Design and prototype a **lightweight AI-assisted cybersecurity tool**
- Apply **responsible AI principles**, including human-in-the-loop validation  

---

## 🗂️ Repository Structure

```
ai-enabled-cybersecurity-pbl/
│
├── .github/workflows/       # CI/CD workflows
│   └── security-scan.yml    # Week 4: Self-scan on PRs
├── configs/                 # Configuration files
│   └── targets.yaml         # Week 4: Target repos for batch scanning
├── docs/                    # References, diagrams, and documentation
│   ├── week4-agent.md       # Week 4: GitHub agent documentation
│   └── week4-results.md     # Week 4: Validation scan results
├── notes/                   # Weekly reflections, findings, and discussions
├── experiments/             # Vulnerability examples and prompt experiments
├── src/
│   └── pipeline/            # Security scanning pipeline
│       ├── detectors/       # Typo, secret, dependency, SQLi detectors
│       ├── reporters/       # JSON, Markdown, and Security reporters
│       ├── main.py          # Week 2: Pipeline entrypoint
│       ├── github_agent.py  # Week 4: GitHub repo scanner
│       ├── schema.py        # Unified finding schema
│       ├── redaction.py     # Secret redaction layer
│       └── llm_remediation.py  # LLM-based fix instructions
├── reports/                 # Generated scan reports
│   ├── week2/               # Week 2 scan outputs
│   └── week4/               # Week 4 GitHub repo scans
├── requirements.txt         # Python dependencies
├── README.md                # Project overview and documentation
└── .gitignore
```

---

## 📅 Week 1 Focus

**Week 1 Objectives (Track 3):**
- Gain familiarity with **Git** and collaborative workflows
- Build foundational understanding of **software vulnerabilities**
- Frame vulnerabilities in the context of **AI-assisted security analysis**

**Week 1 Progress:**
- Repository setup and team collaboration established  
- Core Git workflows practiced (branching, commits, pull requests)  
- Review of common vulnerability types (e.g., injection, access control, misconfiguration)  
- Initial discussion on how LLMs can assist or introduce risks in cybersecurity  

---

## ⚠️ Ethical & Security Considerations

This project is conducted strictly for **educational and defensive purposes**.  
All experiments and tools developed will:
- Avoid unauthorized or unethical security testing
- Respect data privacy and confidentiality
- Include human oversight for AI-generated outputs
- Align with responsible AI and cybersecurity best practices

---

## � Week 2 Focus

**Week 2 Topic:** Basic issues—typos, accidentally committed API keys, outdated dependencies.

**Week 2 Deliverable:** A security scanning pipeline that detects common issues and generates remediation guidance.

### Pipeline Features

| Detector | Tool | Purpose |
|----------|------|---------|
| **Typos** | codespell | Spelling errors in code and docs |
| **Secrets** | gitleaks/regex | Accidentally committed credentials |
| **Dependencies** | pip-audit/npm audit | Known vulnerable packages |

### Key Design Decisions

- **Deterministic detection**: All scanning uses established tools, not LLM inference
- **Redaction layer**: Secrets are **never** stored or displayed in full
- **LLM for remediation only**: LLM generates fix instructions from redacted context
- **Unified schema**: All findings use a common format for easy processing
- **Multiple LLM backends**: Anthropic Claude, Ollama (free/local), or templates

### Running the Pipeline

```bash
# Install dependencies
pip install -r requirements.txt

# Run the scan (auto-selects LLM provider)
cd src
python -m pipeline.main ..

# Use local Ollama for free LLM remediation
python -m pipeline.main .. --llm-provider ollama

# Quick scan with templates only (no LLM)
python -m pipeline.main .. --no-llm

# Check available tools and LLM providers
python -m pipeline.main --check-tools

# Output will be in reports/week2/
```

### Output Files

- `reports/week2/findings.json` — Machine-readable scan results
- `reports/week2/report.md` — Human-readable report with remediation guidance

See [docs/week2-pipeline.md](docs/week2-pipeline.md) for full documentation.

---

## � Week 4 Focus

**Week 4 Topic:** Building an agent to find software vulnerabilities in open-source software.

**Week 4 Deliverable:** Automated GitHub repository security scanner with developer-friendly reports.

### New Features (Week 4)

| Feature | Description |
|---------|-------------|
| **GitHub Agent** | Scan any GitHub repo by URL or owner/name |
| **SQL Injection Detection** | Pattern-based detection for Python, JS, PHP |
| **Expanded Secrets** | 30+ provider patterns (AWS, Stripe, Slack, etc.) |
| **Security Reports** | Developer-friendly reports with intent/risk analysis |
| **Batch Scanning** | Scan multiple repos from config file |

### Running the GitHub Scanner

```bash
cd src

# Scan a GitHub repository
python -m pipeline.github_agent pallets/flask

# Scan by URL
python -m pipeline.github_agent https://github.com/psf/requests

# Scan a local directory
python -m pipeline.github_agent --local ./my-project

# Batch scan from config file
python -m pipeline.github_agent --config ../configs/targets.yaml

# With LLM remediation
python -m pipeline.github_agent owner/repo --use-llm --llm-provider ollama
```

### Output Files (Week 4)

```
reports/week4/<owner>__<repo>/
├── findings.json        # Machine-readable findings
├── report.md            # Standard markdown report
└── security_report.md   # Developer-friendly security report (NEW)
```

### Security Report Contents

The new `security_report.md` includes:
- **Executive Summary** with risk level and category breakdown
- **Detailed Findings** with:
  - Intent: What the code is trying to do
  - Attack Surface: Where user input flows
  - Risk Assessment: Impact and likelihood
  - Recommended Fix: Concrete remediation steps
  - Verification: How to confirm the fix

### Validation Results

Scanned 5 real-world Python projects (109,000+ combined GitHub stars):
- pallets/click, httpie/cli, encode/django-rest-framework, bottlepy/bottle, aio-libs/aiohttp

See [docs/week4-results.md](docs/week4-results.md) for full results and analysis.

### Documentation

- [docs/week4-agent.md](docs/week4-agent.md) — Full GitHub agent documentation
- [docs/week4-results.md](docs/week4-results.md) — Validation scan results
- [configs/targets.yaml](configs/targets.yaml) — Target repository configuration

---

## 📝 Week 6 Focus

**Week 6 Topic:** Responsible Innovation

**Week 6 Deliverable:** Essay on developing and sharing vulnerability detection tools responsibly.

- [docs/week6-responsible-innovation-essay.md](docs/week6-responsible-innovation-essay.md) — Responsible innovation essay covering dual-use concerns, ethical scanning, redaction practices, and a practical responsibility checklist

---

## 🚀 Quick Start

```bash
# Clone and install
git clone https://github.com/YOUR_USERNAME/ai-enabled-cybersecurity-pbl.git
cd ai-enabled-cybersecurity-pbl
pip install -r requirements.txt

# Run the scanner on a local directory
cd src
python -m pipeline.main ../path/to/scan

# Run the evaluation harness
cd ../evals
python run_eval.py --model baseline
```

See [docs/week2-pipeline.md](docs/week2-pipeline.md) for full usage documentation.

---

## 📄 Final Deliverable

**[Final Paper: Hybrid Vulnerability Detection](docs/final-paper.md)**

A structured academic-style paper presenting:
- Problem motivation and background
- Hybrid architecture design (deterministic detection + LLM remediation)
- Evaluation methodology and results
- Responsible innovation considerations
- Limitations and future work

### Supporting Documentation

| Document | Description |
|----------|-------------|
| [docs/week7-research-directions.md](docs/week7-research-directions.md) | Research questions and future work roadmap |
| [reports/week5/eval_results.md](reports/week5/eval_results.md) | Detailed evaluation metrics |
| [docs/week4-results.md](docs/week4-results.md) | Real-world validation on 5 OSS repositories |

---

## ⚠️ Responsible Use

This project is conducted strictly for **educational and defensive purposes**. The tools and techniques documented here:

- Are designed for **defensive security analysis only**
- Include **mandatory secret redaction** before any storage or LLM transmission
- Provide **no exploitation capabilities**
- Follow **responsible disclosure principles**

See [docs/week6-responsible-innovation-essay.md](docs/week6-responsible-innovation-essay.md) for detailed ethical considerations.

---

## 👥 Team

- **Gael Guzmán**  

---

## 📎 License & Usage

This repository is intended for **academic use** within the MIT Blended AI+X Program.  
No content should be used for malicious or unauthorized security activities.
