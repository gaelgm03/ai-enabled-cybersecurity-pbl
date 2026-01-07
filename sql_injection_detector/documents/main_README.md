# SQL Injection Detector

A static analysis tool for detecting SQL injection vulnerabilities in source code.

## Features

- **Multi-language support**: Python, PHP (extensible to Java, Node.js, etc.)
- **4 Detection types**: Classic, Blind, Out-of-Band (OOB), Stacked Queries (extensible)
- **96 Detection patterns**: 57 common SQL patterns + 39 language-specific patterns (extensible)
- **Multiple output formats**: Text, JSON
- **Auto-save reports**: Timestamped report files

## Supported SQL Injection Types

| Detector | Description | Pattern Examples |
|----------|-------------|------------------|
| **Classic** | Error-based and UNION-based injection | EXTRACTVALUE, UPDATEXML, UNION SELECT |
| **Blind** | Boolean-based and Time-based injection | OR 1=1, SLEEP(), WAITFOR DELAY |
| **OOB** | Out-of-Band data exfiltration | LOAD_FILE, UTL_HTTP, xp_dirtree |
| **Stacked** | Multiple query execution | Semicolon-prefixed statements |

## Installation

### Requirements

- Python 3.8+
- PyYAML

### Setup

```bash
pip install pyyaml
```

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

## Pattern Distribution

### By Category

| Category | Patterns | Location |
|----------|----------|----------|
| Common (SQL syntax) | 57 | patterns/common/ |
| Python-specific | 19 | patterns/python/ |
| PHP-specific | 20 | patterns/php/ |
| **Total** | **96** | |

### By Detector

| Detector | Common | Python | PHP | Total |
|----------|--------|--------|-----|-------|
| classic | 8 | 11 | 16 | 35 |
| blind | 15 | 2 | 2 | 19 |
| oob | 18 | 2 | 0 | 20 |
| stacked | 16 | 4 | 2 | 22 |

## Output Example

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
