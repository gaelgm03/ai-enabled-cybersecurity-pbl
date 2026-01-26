---
layout: default
title: Home
nav_order: 1
---

# AI-Enabled Cybersecurity

**MIT Blended AI+X PBL - Track 3: AI-Enabled Cybersecurity (Anthropic Project)**

---

## Project Overview

This project explores how **Large Language Models (LLMs)** can assist defensive cybersecurity tasks, with a focus on **automated vulnerability detection** in source code. We developed tools that identify security issues such as typos, exposed secrets, vulnerable dependencies, and SQL injection patterns—while carefully considering the **ethical implications** of dual-use security tools.

### Key Achievements

| Metric | Value |
|--------|-------|
| **Lines of Code** | 6,149+ |
| **Detection Patterns** | 96 SQL injection patterns |
| **OSS Projects Validated** | 5 repositories (109K+ GitHub stars) |
| **Vulnerabilities Detected** | 908 findings |
| **Evaluation Cases** | 60 labeled test cases |

---

## Project Components

### [Background Knowledge](background.md)
Foundational research on software vulnerabilities, LLMs in cybersecurity, and SQL injection techniques.

### [Security Scan Pipeline](pipeline.md)
A modular scanning pipeline with 4 detectors (typos, secrets, dependencies, SQLi) and LLM-powered remediation guidance.

### [SQL Injection Detector](sqli-detector.md)
A specialized static analysis tool with 96 detection patterns for multiple SQL injection attack types.

### [Educational Demos](demos.md)
Hands-on demonstrations of SQL injection and credential exposure vulnerabilities with secure alternatives.

### [Validation Results](results.md)
Real-world validation against 5 major open-source Python projects.

### [LLM Evaluation](evaluation.md)
Evaluation framework comparing AI vs. deterministic methods for vulnerability classification.

### [Ethics & Responsibility](ethics.md)
Ethical analysis and responsible innovation principles for dual-use security tools.

---

## Technical Highlights

### Architecture

```
┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│     Typo     │  │    Secret    │  │  Dependency  │  │     SQLi     │
│   Detector   │  │   Detector   │  │   Detector   │  │   Detector   │
└──────┬───────┘  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘
       └─────────────────┴─────────────────┴─────────────────┘
                                   │
                         ┌─────────▼─────────┐
                         │  Redaction Layer  │
                         │  (Secret Safety)  │
                         └─────────┬─────────┘
                                   │
                         ┌─────────▼─────────┐
                         │  LLM Remediation  │
                         │    (Optional)     │
                         └─────────┬─────────┘
                                   │
                    ┌──────────────┴──────────────┐
                    ▼                              ▼
             ┌────────────┐                ┌────────────┐
             │   JSON     │                │  Markdown  │
             │  Report    │                │   Report   │
             └────────────┘                └────────────┘
```

### Key Design Decisions

- **Deterministic Detection**: All vulnerability scanning uses established tools (codespell, gitleaks, pip-audit) and regex patterns—not LLM inference
- **Redaction Layer**: Secrets are **never** stored or displayed in full; all sensitive values are immediately redacted
- **LLM for Remediation Only**: LLMs generate fix instructions from redacted context, not for primary detection
- **Multiple LLM Backends**: Supports Anthropic Claude, Ollama (local/free), or templates (no LLM)

---

## Quick Start

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/ai-enabled-cybersecurity-pbl.git
cd ai-enabled-cybersecurity-pbl

# Install dependencies
pip install -r requirements.txt

# Run the security scan pipeline
cd src
python -m pipeline.main ..

# Run the SQL injection detector
python -m sql_injection_detector.runner --path ../test

# Run the evaluation framework
python -m evals.run_eval --models baseline
```

---

## Project Timeline

| Week | Focus | Deliverable |
|------|-------|-------------|
| Week 1 | Foundations | Git workflows, vulnerability understanding |
| Week 2 | Pipeline | Security scanning pipeline with 4 detectors |
| Week 3 | Deep Dive | SQL injection & secret exposure demonstrations |
| Week 4 | Validation | GitHub scanner, 5 OSS project analysis |
| Week 5 | Evaluation | LLM evaluation framework and comparison |
| Week 6 | Ethics | Responsible innovation essay |

---

## Team

- **Gael Guzmán**
- **Diego Ulises**
- **Yangingyi**
- **Sekito Shinjo**

---

## Ethical Notice

This project is conducted strictly for **educational and defensive purposes**. All tools developed:

- Avoid unauthorized or unethical security testing
- Respect data privacy and confidentiality
- Include human oversight for AI-generated outputs
- Align with responsible AI and cybersecurity best practices

---

## License & Usage

This repository is intended for **academic use** within the MIT Blended AI+X Program.
No content should be used for malicious or unauthorized security activities.

---

*MIT Blended AI+X Program - Track 3: AI-Enabled Cybersecurity*
