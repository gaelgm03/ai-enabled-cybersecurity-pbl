# AI-Enabled Cybersecurity (PBL)

## MIT Blended AI+X Program  
**Project-Based Learning: AI in Cybersecurity – Anthropic Project**  
**Track 3: AI-Enabled Cybersecurity**

---

## 📌 Project Overview

This repository contains the work for the **AI in Cybersecurity Project-Based Learning (PBL)** as part of the **MIT Blended AI+X Program**.

The project explores how **Large Language Models (LLMs)** can be used to **assist defensive cybersecurity tasks**, such as identifying software vulnerabilities, supporting security audits, and automating parts of penetration testing workflows—while carefully considering the **risks, limitations, and ethical concerns** introduced by AI systems.

---

## 🎯 Project Goals

- Understand how LLMs introduce **new security risks and attack surfaces**
- Explore how AI can support **defensive cybersecurity workflows**
- Identify common **software vulnerabilities** and how AI may assist in detecting or explaining them
- Design and prototype a **lightweight AI-assisted cybersecurity tool**
- Apply **responsible AI principles**, including human-in-the-loop validation

---

## 🧭 Track Information

**Track:** Track 3 – AI-Enabled Cybersecurity  

**Track Focus Areas:**
- Foundations of penetration testing and vulnerability research  
- AI-assisted security audits and system testing  
- Identifying code vulnerabilities with LLMs  
- Prompt engineering and scaffolding for security use cases  
- Proofs-of-concept for AI-enabled cybersecurity workflows  

---

## 🗂️ Repository Structure

```
ai-enabled-cybersecurity-pbl/
│
├── docs/                    # References, diagrams, and documentation
├── notes/                   # Weekly reflections, findings, and discussions
├── experiments/             # Vulnerability examples and prompt experiments
├── src/
│   └── pipeline/            # Week 2: Security scanning pipeline
│       ├── detectors/       # Typo, secret, dependency detectors
│       ├── reporters/       # JSON and Markdown report generators
│       ├── main.py          # Pipeline entrypoint
│       ├── schema.py        # Unified finding schema
│       ├── redaction.py     # Secret redaction layer
│       └── llm_remediation.py  # LLM-based fix instructions
├── reports/                 # Generated scan reports
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

## 🚀 Next Steps

- Integrate pipeline into CI/CD (GitHub Actions)
- Add custom ignore lists for false positives
- Explore SARIF output for IDE integration
- Week 3: Deeper vulnerability analysis

---

## 👥 Team

- **Gael Guzmán**  
- *Additional team members to be added*

---

## 📎 License & Usage

This repository is intended for **academic use** within the MIT Blended AI+X Program.  
No content should be used for malicious or unauthorized security activities.
