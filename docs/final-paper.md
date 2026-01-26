# Hybrid Vulnerability Detection: Combining Deterministic Scanners with LLM-Assisted Remediation

**MIT Blended AI+X PBL – AI-Enabled Cybersecurity (Anthropic Project)**  
**Track 3: AI-Enabled Cybersecurity**  
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

Our real-world validation scans illustrate this challenge. Scanning five popular open-source repositories produced 908 total findings, of which:
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

Our hybrid vulnerability detection system consists of five primary layers, each with well-defined responsibilities.

### 3.1 Detection Layer

The detection layer implements four specialized detectors, each targeting a specific vulnerability category:

**TypoDetector.** Integrates with codespell to identify spelling errors in code and documentation. Typos in security-critical contexts (e.g., variable names, configuration keys) can lead to subtle bugs or misconfigurations. The detector parses codespell output and normalizes findings to our unified schema.

**SecretDetector.** Identifies accidentally committed credentials using a two-tier approach: (1) integration with gitleaks for comprehensive pattern coverage when available, and (2) fallback to custom regex patterns covering 30+ provider formats (AWS, GitHub, Stripe, Slack, database URLs, etc.). High-entropy string detection supplements explicit patterns.

**DependencyDetector.** Checks package manifests against vulnerability databases using pip-audit for Python projects. Findings include CVE identifiers, severity scores, and affected version ranges (this detector is part of the system but is not included in the 60-case labeled dataset).

**SQLiDetector.** Pattern-based detection for SQL injection vulnerabilities across Python, JavaScript, and PHP. Identifies string concatenation and format string patterns in database query construction while attempting to exclude safe patterns (parameterized queries, ORM usage).

All detectors inherit from a common `BaseDetector` interface, producing findings in a unified schema that includes: finding type, severity, file path, line number, raw match (for internal use), redacted match (for display/LLM), and confidence score.

### 3.2 Redaction Layer

A mandatory redaction layer sanitizes all secrets before storage, display, or transmission to any external service (including LLMs). The `Redactor` class implements pattern-specific masking:

- API keys are truncated to show only prefix and last four characters (e.g., `sk-a********9789`)
- Passwords are fully masked
- Database URLs preserve structure but mask credentials

This design ensures that even if scan results are inadvertently exposed, actual credential values remain protected. The redaction layer operates synchronously in the detection pipeline—findings are never stored or processed in unredacted form.

### 3.3 LLM Remediation Layer

The LLM remediation layer generates human-readable fix instructions from redacted finding context. It supports multiple backends:

- **Anthropic Claude:** High-quality remediation via API (requires API key)
- **Ollama:** Free, local inference using open models (llama3.1, mistral)
- **Template Fallback:** Pre-written remediation templates when no LLM is available

The remediation prompt includes: finding type, severity, redacted code snippet, and file context. The LLM is instructed to provide: (1) explanation of the vulnerability, (2) concrete fix with code example, (3) prevention guidance, and (4) verification steps.

Critically, the LLM is never used for detection decisions—only for enhancing developer understanding of findings already identified by deterministic methods.

### 3.4 Reporting Layer

The reporting layer produces outputs in multiple formats:

- **JSON:** Machine-readable findings for CI/CD integration
- **Markdown:** Human-readable reports with findings grouped by severity and category
- **Security Report:** Developer-friendly format with executive summary, risk assessment, and actionable remediation guidance

Reports include metadata (scan timestamp, target path, detector versions) and explicit limitations sections acknowledging false positive potential.

### 3.5 GitHub Integration

The GitHub agent extends the pipeline for repository scanning:

- Clone public repositories by URL or owner/repo format
- Shallow clones (depth=1) minimize bandwidth and storage
- Rate limiting and configurable delays for ethical scanning
- Batch scanning from configuration files
- Automatic cleanup of temporary directories

---

## 4. Evaluation Methodology

### 4.1 Dataset Construction

We constructed a labeled evaluation dataset of 60 cases across three vulnerability categories:

| Category | Positive Cases | Negative Cases | Total |
|----------|---------------|----------------|-------|
| Typos | 10 real typos | 10 valid identifiers | 20 |
| Secrets | 10 realistic fake secrets | 10 placeholders | 20 |
| SQL Injection | 10 unsafe patterns | 10 safe patterns | 20 |
| **Total** | 30 | 30 | 60 |

**Dataset design principles:**
- **Balanced:** 50% positive (real vulnerabilities), 50% negative (false positives or safe patterns)
- **Multi-language:** Python, JavaScript, PHP samples matching our detector coverage
- **Labeled with rationale:** Each case includes ground truth classification and explanation
- **Safe:** All secrets are synthetic/placeholder values—no real credentials

Negative cases specifically target known false positive patterns:
- Typos: Variable names that resemble typos (e.g., `teh` as identifier)
- Secrets: Placeholder patterns (e.g., `YOUR_API_KEY_HERE`, `changeme`)
- SQLi: Parameterized queries and ORM patterns that superficially resemble injection

### 4.2 Metrics

We evaluate using standard classification metrics:

| Metric | Definition | Interpretation |
|--------|------------|----------------|
| **Precision** | TP / (TP + FP) | Proportion of flagged items that are real vulnerabilities |
| **Recall** | TP / (TP + FN) | Proportion of real vulnerabilities that are flagged |
| **F1 Score** | 2 × (P × R) / (P + R) | Harmonic mean balancing precision and recall |
| **False Positive Rate** | FP / (FP + TN) | Proportion of safe items incorrectly flagged |
| **Latency** | Mean end-to-end time per case | Practical deployment consideration |

### 4.3 Baseline vs. LLM Comparison

We compare three configurations:

1. **Baseline:** Deterministic detectors only (regex patterns, codespell, pip-audit; dependency vulnerabilities were not included in the 60-case labeled dataset)
2. **Ollama llama3.1:8b:** Local LLM classification using 8-billion parameter model
3. **Ollama mistral:7b:** Local LLM classification using 7-billion parameter model

For LLM configurations, we use a classification prompt asking the model to categorize each snippet as VULNERABLE or SAFE with a one-sentence rationale.

### 4.4 Real-World Validation

Beyond synthetic benchmarks, we validated on five production open-source repositories:

| Repository | Stars | Language | Selection Rationale |
|------------|-------|----------|---------------------|
| pallets/click | 17,099 | Python | Popular CLI toolkit |
| httpie/cli | 37,306 | Python | HTTP client utility |
| encode/django-rest-framework | 29,794 | Python | Major Django extension |
| bottlepy/bottle | 8,725 | Python | Micro web framework |
| aio-libs/aiohttp | 16,182 | Python | Async HTTP library |

**Total: 109,106 GitHub stars across well-maintained, non-security-focused projects.**

---

## 5. Results

LLM remediation quality is discussed qualitatively and was not quantitatively evaluated in this study.

### 5.1 Summary Results

| Model | Precision | Recall | F1 | FPR | Latency |
|-------|-----------|--------|-----|-----|---------|
| Baseline (deterministic) | 0.91 | 0.67 | 0.77 | 0.07 | <1ms |
| LLM (llama3.1:8b) | 0.72 | 0.43 | 0.54 | 0.17 | ~54s |
| LLM (mistral:7b) | 0.50 | 0.03 | 0.06 | 0.03 | ~58s |

**Key finding: The baseline deterministic approach significantly outperforms both LLM configurations**, achieving F1 of 0.77 compared to 0.54 (llama3.1) and 0.06 (mistral).

### 5.2 Per-Category Analysis

| Category | Baseline P | Baseline R | Baseline F1 | LLM (llama3.1) F1 |
|----------|------------|------------|-------------|-------------------|
| Secrets | 0.86 | 0.60 | 0.71 | 0.40 |
| SQL Injection | 1.00 | 0.60 | 0.75 | 0.86 |
| Typos | 0.89 | 0.80 | 0.84 | 0.17 |

For brevity, we report only per-category F1 for the LLM (llama3.1), since F1 is the primary summary metric used for cross-model comparison.

**Notable observations:**

- **Typos:** Baseline excels (F1=0.84); LLMs perform poorly (F1=0.17) because they do not recognize typos as security-relevant
- **Secrets:** Baseline achieves high precision (0.86) but moderate recall (0.60); LLMs are overly conservative
- **SQL Injection:** LLM (llama3.1) outperforms baseline (F1=0.86 vs 0.75), achieving higher recall (0.90 vs 0.60) at the cost of some false positives

SQL injection detection is the **only category where LLMs demonstrated an advantage**, suggesting that context-dependent vulnerability patterns may benefit from AI assistance while simpler pattern-matching tasks do not.

### 5.3 Latency Analysis

| Method | Per-Case Latency | Implication |
|--------|------------------|-------------|
| Baseline | <1ms | Suitable for CI/CD, IDE integration, large codebases |
| LLM (local) | 54-58s | Impractical for primary detection; viable for selective enhancement |

Latency is reported as the mean per-case end-to-end classification time measured around the model `classify(...)` call.

The 50,000x latency differential makes LLM-based primary detection impractical for real-world deployment. However, LLMs remain viable for post-detection enhancement (e.g., remediation generation, false positive filtering on flagged items).

### 5.4 Real-World Validation Results

Scanning five production repositories produced:

| Repository | Total Findings | Critical | High | Low |
|------------|----------------|----------|------|-----|
| pallets/click | 48 | 0 | 1 | 47 |
| httpie/cli | 17 | 0 | 11 | 6 |
| django-rest-framework | 493 | 0 | 41 | 452 |
| bottlepy/bottle | 311 | 0 | 11 | 300 |
| aio-libs/aiohttp | 39 | 0 | 16 | 23 |

**Key observations:**
- **Zero critical vulnerabilities:** Expected for well-maintained projects
- **High false positive rate:** 70-95% of findings are benign (intentional names, test fixtures, documentation)
- **No SQL injection findings:** These libraries use ORMs or parameterized queries
- **Scanner validated on real code:** Qualitatively consistent with observed trends from the synthetic evaluation

---

## 6. Discussion

### 6.1 When Deterministic Methods Excel

Our results demonstrate that deterministic detection significantly outperforms LLM-based classification for primary vulnerability identification. This finding has important implications:

**Consistency and auditability.** Regex patterns produce identical results across runs. Security teams can audit, extend, and version-control detection rules. LLM outputs vary between runs and model versions, complicating reproducibility.

**Performance at scale.** Sub-millisecond latency enables integration into CI/CD pipelines, IDE plugins, and large-scale repository scanning. LLM inference costs (54+ seconds per case) make primary detection impractical.

**Predictable coverage.** Deterministic rules have explicit scope—teams know exactly what patterns are and are not detected. LLM coverage is opaque and may vary unpredictably.

### 6.2 When AI Assistance Adds Value

Despite overall LLM underperformance, our evaluation identified specific contexts where AI assistance provides benefit:

**SQL injection detection.** LLM (llama3.1) achieved F1=0.86 vs baseline F1=0.75 for SQLi, demonstrating that context-dependent vulnerabilities may benefit from semantic understanding. The LLM recognized unsafe patterns that escaped regex rules while tolerating some false positives.

**Remediation generation.** While not quantitatively evaluated, qualitative assessment suggests LLM-generated fix instructions are more detailed and context-aware than template-based alternatives.

**False positive filtering.** LLMs can potentially reduce alert burden by reviewing flagged items and filtering benign patterns—though this introduces the 54-second latency cost per item.

### 6.3 The Hybrid Architecture Advantage

Our separation of detection and remediation captures the best of both approaches:

- **Detection reliability:** Deterministic methods provide the consistency and speed required for security tooling
- **Remediation quality:** LLMs enhance developer experience without compromising detection accuracy
- **Graceful degradation:** Template fallback ensures functionality without LLM access
- **Safety by design:** Mandatory redaction prevents secret exposure to external services

This architecture suggests a general pattern for AI-assisted security tooling: use AI where it adds value (explanation, enhancement) while preserving deterministic foundations for critical decisions.

### 6.4 Responsible Innovation Considerations

Building security tools requires careful attention to dual-use potential and ethical implications:

**Mandatory secret redaction.** Our architecture ensures credentials are never stored, displayed, or transmitted in raw form. This protects against inadvertent exposure through scan results.

**Separation of detection from exploitation.** The tool identifies potential vulnerabilities but includes no capability to exploit them. Detection and exploitation are deliberately kept separate.

**Responsible disclosure guidance.** Generated reports include reminders about ethical scanning practices and proper disclosure procedures for third-party code.

**Transparency about limitations.** Reports explicitly acknowledge false positive rates and recommend human review. Findings are presented as potential issues requiring verification, not definitive verdicts.

---

## 7. Limitations

### 7.1 Evaluation Limitations

**Small dataset.** Our evaluation uses 60 labeled cases—sufficient for directional insights but not statistically robust benchmarks. Results should be interpreted as indicative rather than definitive.

**Limited language coverage.** Detectors currently support Python, JavaScript, and PHP. Many vulnerability patterns are language-specific and may not generalize.

**LLM variability.** LLM responses can vary between runs due to temperature settings and model updates. Our evaluation represents a single point-in-time snapshot.

**Synthetic vs. real vulnerabilities.** Our labeled dataset uses synthetic examples. Performance on novel, real-world vulnerabilities may differ.

### 7.2 System Limitations

**Pattern coverage gaps.** Deterministic detectors only find patterns explicitly encoded in rules. Novel secret formats, obfuscated credentials, and context-dependent vulnerabilities may be missed.

**High false positive rate.** Real-world validation showed 70-95% false positive rates depending on category. Practical deployment requires allowlists, context filtering, or human triage.

**No semantic analysis.** Pattern matching cannot understand code semantics. Whether a flagged pattern is actually exploitable requires deeper analysis.

**Single-language focus.** Current implementation focuses on Python ecosystem tooling. Extension to other languages requires additional detector development.

### 7.3 Scope Limitations

**Detection only.** We evaluate classification accuracy, not end-to-end vulnerability discovery or remediation effectiveness.

**Public repositories only.** Validation used public open-source projects. Private enterprise codebases may exhibit different patterns.

**No adversarial evaluation.** We did not test detector evasion through obfuscation or adversarial inputs.

---

## 8. Conclusion

This paper demonstrates that hybrid vulnerability detection—combining deterministic scanners with LLM-assisted remediation—captures the benefits of both approaches while mitigating their respective weaknesses.

**Key findings:**

1. **Deterministic methods outperform LLMs for primary detection.** Baseline detectors achieved F1=0.77 compared to F1=0.54 for the best LLM configuration, with 50,000x faster latency.

2. **LLMs add value in specific contexts.** SQL injection detection and remediation generation benefit from AI assistance, while simpler pattern-matching tasks do not.

3. **Hybrid architectures offer a pragmatic path forward.** Separating detection from explanation preserves reliability while leveraging AI capabilities where they genuinely help.

4. **Responsible innovation requires deliberate design.** Mandatory redaction, separation of detection from exploitation, and transparency about limitations are essential for ethical security tooling.

Our evaluation validates these findings on both synthetic benchmarks and production open-source repositories, demonstrating practical applicability beyond controlled experiments.

**Future work** includes: confidence scoring for finding triage, expanded pattern libraries, IDE integration, and quantitative evaluation of LLM-generated remediation quality.

The tension between detection breadth and precision will persist as software systems grow more complex. Hybrid architectures that combine the reliability of deterministic methods with the contextual understanding of AI systems offer a promising direction for addressing this challenge responsibly.

---

## References

1. **GitHub.** "Secret scanning." GitHub Docs. https://docs.github.com/en/code-security/secret-scanning

2. **OWASP Foundation.** "OWASP Top Ten Web Application Security Risks." https://owasp.org/www-project-top-ten/

3. **Meta AI.** "CyberSecEval: A Benchmark for Evaluating LLMs on Cybersecurity Tasks." https://github.com/meta-llama/PurpleLlama

4. **Gitleaks.** "Protect and discover secrets using Gitleaks." https://github.com/gitleaks/gitleaks

5. **CERT Coordination Center.** "CERT Guide to Coordinated Vulnerability Disclosure." Carnegie Mellon University. https://certcc.github.io/CERT-Guide-to-CVD/

6. **NIST.** "Secure Software Development Framework (SSDF), SP 800-218." National Institute of Standards and Technology. https://csrc.nist.gov/publications/detail/sp/800-218/final

7. **OWASP Foundation.** "OWASP Secure Coding Practices Quick Reference Guide." https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/

8. **Verizon.** "2023 Data Breach Investigations Report." https://www.verizon.com/business/resources/reports/dbir/

---

*Paper prepared as part of the MIT Blended AI+X Program – Track 3: AI-Enabled Cybersecurity (Anthropic Project)*
