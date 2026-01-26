# Week 1 Notes — Git & Software Vulnerabilities

> **Week 1 Learning Journal**  
> MIT Blended AI+X Program — Track 3: AI-Enabled Cybersecurity

---

## Git Workflow Practice

### Commands and Concepts Practiced
- **Cloning:** `git clone` to create local repository copies
- **Branching:** `git branch` and `git checkout -b` for feature isolation
- **Committing:** `git add` and `git commit` with descriptive messages
- **Pushing:** `git push` to sync with remote repository
- **Pull Requests:** Collaborative code review before merging

### Key Takeaways
- Feature branches (e.g., `week1/gael-git-setup`) isolate changes and reduce merge conflicts
- Descriptive commit messages help collaborators understand changes
- Pull requests enable code review and discussion before integration
- A clean commit history aids debugging and project maintenance

### Security Relevance
- Git history provides an audit trail of all changes
- Branch protection rules can enforce code review before merging to main
- Secrets should never be committed (use `.gitignore` and environment variables)

---

## Software Vulnerabilities Overview

This week introduced foundational vulnerability categories. Detailed documentation is available in [`docs/software-vulnerabilities.md`](../docs/software-vulnerabilities.md).

### Categories Studied
1. **Injection Vulnerabilities** — Untrusted input executed as code/commands
2. **Broken Access Control** — Users accessing unauthorized resources
3. **Security Misconfiguration** — Improper security settings
4. **Vulnerable Components** — Outdated dependencies with known CVEs

### Personal Observations
- Many vulnerabilities stem from trusting user input without validation
- Defense in depth: multiple layers of protection are better than one
- Automation can help detect known patterns, but context matters

---

## AI + Cybersecurity Reflections

Detailed analysis is available in [`docs/llm-in-cybersecurity.md`](../docs/llm-in-cybersecurity.md).

### How LLMs Can Help
- Explain vulnerabilities in accessible language
- Identify common vulnerability patterns during code review
- Generate security documentation and training materials
- Summarize CVE reports and threat intelligence

### Risks to Consider
- **Hallucinations:** AI may generate incorrect but confident-sounding advice
- **Outdated knowledge:** Training data cutoffs mean missing recent CVEs
- **Prompt injection:** Malicious inputs can manipulate AI behavior
- **Over-trust:** Humans may defer critical decisions to AI without verification

### Personal Takeaway
LLMs are powerful *assistants* but should not replace human judgment in security decisions. Every AI output needs verification against authoritative sources.

---

## Week 1 Completion Checklist

- [x] Repository initialized and structured
- [x] Git workflow practiced (branch, commit, PR, merge)
- [x] Common vulnerability types documented
- [x] LLM assistance and risks reflected upon
- [x] Documentation suitable for mentor review

---

## Looking Ahead (Deferred to Week 2+)

*The following are noted for future work, not implemented this week:*

- Narrowing vulnerability scope for prototype focus
- Designing AI-assisted security workflow
- Evaluating LLM outputs for specific vulnerability detection
- Defining success metrics and acceptance criteria

---

*Last updated: Week 1*
