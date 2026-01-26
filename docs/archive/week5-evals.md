# Week 5: Cybersecurity-Relevant LLM Evaluations Research

**MIT Blended AI+X PBL – AI-Enabled Cybersecurity (Anthropic Project)**  
**Date:** January 2026

---

## 1. Taxonomy of Cybersecurity-Relevant LLM Eval Categories

### 1.1 Code Vulnerability Detection
**Description:** Ability to identify security vulnerabilities in source code.

| Sub-category | What it measures | Relevance to our pipeline |
|--------------|------------------|---------------------------|
| SQL Injection Detection | Identifying unsafe query construction | **High** - Core detector |
| Secret/Credential Exposure | Finding hardcoded secrets, API keys | **High** - Core detector |
| Command Injection | Detecting unsafe shell command construction | Medium - Future work |
| Path Traversal | Identifying file path manipulation risks | Medium - Future work |
| XSS Patterns | Cross-site scripting in web code | Low - Not current focus |

### 1.2 Secure Coding Remediation
**Description:** Quality of fix suggestions and secure alternatives.

| Sub-category | What it measures | Relevance to our pipeline |
|--------------|------------------|---------------------------|
| Fix Correctness | Whether suggested fix actually resolves issue | **High** - LLM remediation |
| Fix Completeness | Covers edge cases, doesn't introduce new vulns | **High** - LLM remediation |
| Developer Usability | Clear, actionable, copy-pasteable | Medium |

### 1.3 False Positive Discrimination
**Description:** Ability to distinguish real vulnerabilities from benign patterns.

| Sub-category | What it measures | Relevance to our pipeline |
|--------------|------------------|---------------------------|
| Typo vs Identifier | "teh" typo vs `teh` variable name | **Critical** - Known FP source |
| Secret vs Placeholder | Real API key vs `YOUR_API_KEY_HERE` | **Critical** - Known FP source |
| Unsafe SQL vs Safe ORM | String concat vs parameterized query | **High** - SQLi detector |
| Test/Doc context | Vuln in test file vs production code | **High** - Context awareness |

### 1.4 Prompt Injection Robustness
**Description:** Resistance to adversarial inputs attempting to manipulate LLM behavior.

| Sub-category | What it measures | Relevance to our pipeline |
|--------------|------------------|---------------------------|
| Jailbreak resistance | Ignoring malicious instructions in code | Low - Not user-facing |
| Output consistency | Same input → same classification | Medium |

### 1.5 Policy Compliance
**Description:** Adherence to organizational security policies.

| Sub-category | What it measures | Relevance to our pipeline |
|--------------|------------------|---------------------------|
| Severity calibration | Consistent HIGH/MEDIUM/LOW ratings | Medium |
| No exploitation details | Avoids providing attack code | **High** - Ethics constraint |

---

## 2. Existing Evals vs. Evals We Must Create

### 2.1 Existing Public Benchmarks

| Benchmark | What it tests | Usable for us? | Limitations |
|-----------|---------------|----------------|-------------|
| **CyberSecEval** (Meta) | LLM security across domains | Partially | Focuses on LLM safety, not vuln detection |
| **SecEval** (academic) | Code security understanding | Partially | Limited labeled datasets |
| **CodeXGLUE** | Code understanding tasks | No | Not security-focused |
| **HumanEval** | Code generation correctness | No | Not security-focused |
| **OWASP Benchmark** | SAST tool comparison | Partially | Java-focused, heavy setup |

### 2.2 Evals We Must Create for Our Pipeline

| Eval Name | Purpose | Priority | Status |
|-----------|---------|----------|--------|
| **FP-Discrimination-Typos** | Typo vs variable name classification | P0 | **Creating** |
| **FP-Discrimination-Secrets** | Real secret vs placeholder classification | P0 | **Creating** |
| **FP-Discrimination-SQLi** | Unsafe concat vs safe parameterized | P0 | **Creating** |
| **Context-Awareness** | Test/doc file vs production code | P1 | Future |
| **Remediation-Quality** | Fix correctness evaluation | P1 | Future |
| **Severity-Consistency** | Same pattern → same severity | P2 | Future |

---

## 3. Which Evals Best Measure Vulnerability-Finding Ability

### 3.1 Primary Metrics

| Metric | Definition | Why it matters |
|--------|------------|----------------|
| **Precision** | TP / (TP + FP) | Reduces developer alert fatigue |
| **Recall** | TP / (TP + FN) | Ensures real vulns aren't missed |
| **F1 Score** | Harmonic mean of P & R | Balanced overall performance |
| **False Positive Rate** | FP / (FP + TN) | Critical for adoption |

### 3.2 Secondary Metrics

| Metric | Definition | Why it matters |
|--------|------------|----------------|
| **Latency** | Time per classification | Practical deployment |
| **Cost** | Tokens/API calls per scan | Budget constraints |
| **Consistency** | Same input → same output | Reproducibility |

### 3.3 Recommended Eval Strategy for Our Pipeline

**Ground-truth approach:**
1. Curate labeled dataset with known vulnerable/safe examples
2. Run deterministic detectors (baseline)
3. Run AI-assisted classification (filter FPs)
4. Compare precision/recall/F1 per category

**Why this works for us:**
- We already have deterministic detectors with known FP patterns
- AI value-add is in *filtering* false positives, not primary detection
- Small, curated dataset (50-80 cases) sufficient for comparative eval
- Reproducible without external dependencies

---

## 4. Eval Design Decisions

### 4.1 Dataset Requirements
- **Balanced:** ~50% positive (real vulns), ~50% negative (FPs/safe patterns)
- **Multi-category:** Typos, secrets, SQLi patterns
- **Multi-language:** Python, JavaScript, PHP (matching our detectors)
- **Labeled:** Ground truth with rationale for each case
- **Safe:** No real secrets; synthetic/placeholder values only

### 4.2 Model Comparison Approach
1. **Baseline:** Deterministic detectors only (no AI)
2. **Ollama local:** llama3.1:8b, mistral:7b (free, reproducible)
3. **Anthropic:** Claude (if API key available, reference point)

### 4.3 Limitations to Acknowledge
- Small dataset may not generalize to all codebases
- LLM responses can vary (temperature, version drift)
- Latency/cost will differ between local and API models
- We test classification, not end-to-end vuln discovery

---

## 5. References

- Meta CyberSecEval: https://github.com/meta-llama/PurpleLlama
- OWASP Benchmark: https://owasp.org/www-project-benchmark/
- Our Week 2-4 detectors: `src/pipeline/detectors/`
