# AI-Enabled Cybersecurity (PBL)

## MIT Blended AI+X Program  
**Project-Based Learning: AI in Cybersecurity – Anthropic Project**  
**Track 3: AI-Enabled Cybersecurity**

---

## Project Overview

This repository contains the work for the **AI in Cybersecurity Project-Based Learning (PBL)** as part of the **MIT Blended AI+X Program**.

The project explores how **Large Language Models (LLMs)** can be used to **assist defensive cybersecurity tasks**, such as identifying software vulnerabilities, supporting security audits, and automating parts of penetration testing workflows—while carefully considering the **risks, limitations, and ethical concerns** introduced by AI systems.

---

## Key Deliverables

| Document | Description |
|----------|-------------|
| **[Final Paper](docs/final-paper.md)** | Academic-style paper presenting our hybrid detection approach |
| **[Evaluation Results](reports/week5/eval_results.md)** | Quantitative comparison of baseline vs. LLM detection |
| **[Responsible Innovation](docs/responsible-innovation.md)** | Ethical considerations for security tooling |
| **[Validation Results](docs/validation-results.md)** | Real-world validation summary on 5 open-source repositories |

---

## Key Findings

- **Deterministic detection outperforms LLMs:** Baseline detectors achieved F1=0.77 (91% precision, 67% recall) vs. F1=0.54 for the best LLM configuration
- **LLMs add value in specific contexts:** SQL injection detection showed LLM advantage (F1=0.86 vs 0.75); remediation generation benefits from AI assistance
- **Hybrid architectures are the pragmatic path forward:** Separate detection (deterministic) from explanation (LLM-assisted) to capture benefits of both approaches

---

## Project Goals

- Understand how LLMs introduce **new security risks and attack surfaces**
- Explore how AI can support **defensive cybersecurity workflows**
- Identify common **software vulnerabilities** and how AI may assist in detecting or explaining them
- Design and prototype a **lightweight AI-assisted cybersecurity tool**
- Apply **responsible AI principles**, including human-in-the-loop validation  

---

## Repository Structure

```
ai-enabled-cybersecurity-pbl/
│
├── .github/workflows/       # CI/CD workflows
│   └── security-scan.yml    # Week 4: Self-scan on PRs
├── configs/                 # Configuration files
│   └── targets.yaml         # Week 4: Target repos for batch scanning
├── docs/                    # Final-facing documentation
│   ├── final-paper.md
│   ├── publication-readiness.md
│   ├── responsible-innovation.md
│   ├── validation-results.md
│   └── archive/
│       └── reports/         # Historical scan outputs (non-primary)
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
├── reports/                 # Final evaluation outputs
│   └── week5/
├── requirements.txt         # Python dependencies
├── README.md                # Project overview and documentation
└── .gitignore
```

---

## Ethical & Security Considerations

This project is conducted strictly for **educational and defensive purposes**.  
All experiments and tools developed will:
- Avoid unauthorized or unethical security testing
- Respect data privacy and confidentiality
- Include human oversight for AI-generated outputs
- Align with responsible AI and cybersecurity best practices

---

## Reproducing Results

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
```

## Quick Start

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

---

## Responsible Use

This project is conducted strictly for **educational and defensive purposes**. The tools and techniques documented here:

- Are designed for **defensive security analysis only**
- Include **mandatory secret redaction** before any storage or LLM transmission
- Provide **no exploitation capabilities**
- Follow **responsible disclosure principles**

See [docs/responsible-innovation.md](docs/responsible-innovation.md) for detailed ethical considerations.

---

## Contributors / Team

- **Gael Guzmán**  

---

## License & Usage

This repository is intended for **academic use** within the MIT Blended AI+X Program.  
No content should be used for malicious or unauthorized security activities.
