# Hybrid Vulnerability Detection: Combining Deterministic Scanners with LLM-Assisted Remediation

**MIT Blended AI+X PBL – AI-Enabled Cybersecurity (Anthropic Project)**  
**Draft Paper – Week 7**  
**January 2026**

---

## Abstract

Automated vulnerability detection tools face a fundamental tension: broad pattern matching catches more issues but generates excessive false positives, while narrow rules miss edge cases. This paper presents a hybrid architecture that separates detection from explanation—using deterministic scanners for reliable vulnerability identification and Large Language Models (LLMs) exclusively for generating remediation guidance. We evaluate our approach on a curated dataset of 60 labeled cases across three vulnerability categories (secrets, SQL injection, typos) and validate against five production open-source repositories totaling over 109,000 GitHub stars. Our baseline deterministic detectors achieve 91% precision and 67% recall, significantly outperforming LLM-based classification (72% precision, 43% recall) while maintaining sub-millisecond latency. We discuss the responsible innovation considerations essential for security tooling, including mandatory secret redaction, separation of detection from exploitation, and ethical scanning practices. Our findings suggest that AI assistance in vulnerability detection is most valuable for explanation and remediation rather than primary detection, and that hybrid architectures can capture the benefits of both approaches while mitigating their respective weaknesses.

---

## 1. Introduction

Software vulnerabilities remain one of the most persistent challenges in cybersecurity. Exposed API keys, SQL injection flaws, and outdated dependencies create attack surfaces that adversaries routinely exploit. The 2023 Verizon Data Breach Investigations Report found that web application attacks account for a significant portion of breaches, with credential theft and injection attacks among the top vectors.

Automated scanning tools help development teams identify these issues before they reach production. However, existing approaches face significant limitations:

- **Pattern-based scanners** (regex, static rules) are fast and consistent but generate high false positive rates and miss context-dependent vulnerabilities
- **AI-based classifiers** can understand context but introduce latency, inconsistency, and reliability concerns
- **Commercial solutions** often operate as black boxes, making it difficult to understand or extend their detection logic

This paper presents a hybrid architecture developed as part of the MIT Blended AI+X Program that addresses these limitations by strictly separating detection from explanation:

1. **Deterministic detection:** All vulnerability identification uses established tools and explicit patterns—regex for secrets, codespell for typos, pip-audit for dependencies, and custom patterns for SQL injection
2. **LLM-assisted remediation:** Large Language Models generate human-readable fix instructions and prevention guidance, but only from redacted context—never seeing raw secrets or performing detection

This separation provides the reliability and auditability of traditional tools while leveraging AI capabilities where they add genuine value.

### Contributions

This paper makes the following contributions:

- **Hybrid architecture design:** A modular pipeline that combines deterministic detection with LLM-assisted remediation, supporting multiple backends (Anthropic Claude, Ollama local models, template fallback)

- **Empirical evaluation:** Quantitative comparison of baseline detectors vs. LLM-based classification across three vulnerability categories, demonstrating that deterministic methods outperform LLMs for primary detection

- **Real-world validation:** Testing against five production open-source repositories, demonstrating practical applicability beyond synthetic benchmarks

- **Responsible innovation framework:** Concrete design patterns for building security tools ethically, including mandatory redaction, separation of detection from exploitation, and responsible disclosure guidance

---

## 2. Background and Related Work

### 2.1 The Vulnerability Detection Landscape

Vulnerability detection tools span a spectrum from simple pattern matching to sophisticated semantic analysis:

**Static Analysis Tools.** Tools like Semgrep, CodeQL, and Bandit analyze source code without execution, identifying potential issues through pattern matching and data flow analysis. These tools excel at consistency and speed but often lack the contextual understanding to distinguish real vulnerabilities from benign patterns.

**Secret Scanners.** Specialized tools like Gitleaks, TruffleHog, and GitHub's native secret scanning focus on detecting accidentally committed credentials. These typically use regex patterns matched against known vendor formats (AWS keys, GitHub tokens, etc.) combined with entropy analysis for unknown patterns.

**Dependency Analyzers.** Tools like npm audit, pip-audit, and Dependabot check package manifests against vulnerability databases (CVE, OSV). These are highly reliable for known vulnerabilities but cannot detect zero-days or custom code issues.

**AI-Assisted Analysis.** Recent work has explored using LLMs for vulnerability detection, including Meta's CyberSecEval benchmark and various academic papers on LLM-based code analysis. Results are mixed: LLMs show promise for understanding context but struggle with reliability and consistency.

### 2.2 The False Positive Problem

False positives are the primary barrier to adoption for automated security tools. When scanners generate too many spurious alerts, developers experience "alert fatigue" and begin ignoring findings—including real vulnerabilities.

Our Week 4 validation scans illustrate this challenge. Scanning five popular open-source repositories produced 908 total findings, of which:
- **91% were typos**, many of which were intentional naming choices or technical terms
- **9% were potential secrets**, predominantly test fixtures and documentation examples
- **Estimated 70-95% false positive rate** depending on category

This highlights a fundamental tension: tools must be sensitive enough to catch real issues but precise enough that developers trust the results.

### 2.3 AI in Security: Opportunities and Risks

Large Language Models offer compelling capabilities for security applications:

- **Context understanding:** LLMs can distinguish between `password = "changeme"` in a test file vs. production code
- **Explanation generation:** LLMs can produce human-readable remediation guidance tailored to specific findings
- **Pattern generalization:** LLMs may recognize vulnerability patterns not explicitly encoded in rules

However, AI-based detection introduces significant concerns:

- **Inconsistency:** The same input may produce different outputs across runs
- **Hallucination:** Models may invent rationales not supported by the code
- **Latency:** LLM inference is orders of magnitude slower than regex matching
- **Dual-use risk:** Powerful analysis capabilities could assist attackers as well as defenders

### 2.4 Design Philosophy: Separation of Concerns

Our architecture is guided by a core principle: **use the right tool for each job**.

| Task | Approach | Rationale |
|------|----------|-----------|
| **Detection** | Deterministic (regex, tools) | Consistent, auditable, fast |
| **Redaction** | Rule-based patterns | Must be 100% reliable |
| **Remediation** | LLM-assisted | Benefits from context understanding |
| **Reporting** | Templates + LLM enhancement | Structured format with optional enrichment |

This separation ensures that the most critical function—identifying what is and is not a vulnerability—remains predictable and verifiable, while AI assistance enhances the developer experience without compromising detection reliability.

---

## 3. System Design

*[To be completed: Architecture diagram and component descriptions]*

- **3.1 Detection Layer:** TypoDetector, SecretDetector, DependencyDetector, SQLiDetector
- **3.2 Redaction Layer:** Mandatory secret sanitization before storage or LLM transmission
- **3.3 LLM Remediation Layer:** Multi-provider support (Anthropic, Ollama, templates)
- **3.4 Reporting Layer:** JSON, Markdown, and Security Report formats
- **3.5 GitHub Integration:** Repository cloning, batch scanning, rate limiting

---

## 4. Evaluation Methodology

*[To be completed]*

- **4.1 Dataset Construction:** 60 labeled cases across three categories
- **4.2 Metrics:** Precision, Recall, F1, False Positive Rate, Latency
- **4.3 Baseline vs. LLM Comparison:** Deterministic detectors vs. AI classification
- **4.4 Real-World Validation:** Scans against production OSS repositories

---

## 5. Results

*[To be completed: Full results tables and analysis]*

### 5.1 Summary Results

| Model | Precision | Recall | F1 | FPR | Latency |
|-------|-----------|--------|-----|-----|---------|
| Baseline (deterministic) | 0.91 | 0.67 | 0.77 | 0.07 | <1ms |
| LLM (llama3.1:8b) | 0.72 | 0.43 | 0.54 | — | ~54s |

### 5.2 Per-Category Analysis

| Category | Baseline F1 | Notes |
|----------|-------------|-------|
| Secrets | 0.71 | High precision, moderate recall |
| SQL Injection | 0.75 | Perfect precision, limited recall |
| Typos | 0.84 | Best overall performance |

### 5.3 Real-World Validation

- 5 repositories scanned (pallets/click, httpie/cli, django-rest-framework, bottle, aiohttp)
- 109,000+ combined GitHub stars
- 908 findings generated; high false positive rate as expected for pattern-based detection
- Zero critical vulnerabilities found (expected for well-maintained projects)

---

## 6. Discussion

*[To be completed]*

- **6.1 When AI Helps:** Reducing false positives, context-aware filtering, remediation generation
- **6.2 When AI Fails:** Inconsistency, latency, hallucination risk
- **6.3 Responsible Innovation:** Redaction, separation of detection/exploitation, disclosure ethics
- **6.4 Practical Implications:** Hybrid architectures as the pragmatic path forward

---

## 7. Limitations and Future Work

*[To be completed]*

- Small evaluation dataset (N=60)
- Limited language coverage (Python, JavaScript, PHP)
- LLM variability across runs
- Future: Confidence scoring, expanded patterns, IDE integration

---

## 8. Conclusion

*[To be completed]*

This paper demonstrates that hybrid vulnerability detection—combining deterministic scanners with LLM-assisted remediation—captures the benefits of both approaches while mitigating their respective weaknesses. Our evaluation shows that deterministic methods significantly outperform LLMs for primary detection (F1 0.77 vs 0.54), while LLMs provide valuable assistance for explanation and remediation. We present concrete design patterns for responsible security tooling and validate our approach on real-world open-source repositories.

---

## References

*[To be completed with full citations]*

1. GitHub Secret Scanning Documentation
2. OWASP Top 10 Web Application Security Risks
3. Meta CyberSecEval Benchmark
4. Gitleaks Project
5. CERT Guide to Coordinated Vulnerability Disclosure

---

*Draft paper prepared as part of Week 7 deliverables – MIT Blended AI+X PBL*
