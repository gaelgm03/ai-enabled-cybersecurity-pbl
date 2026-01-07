# sqli-labs Test Dataset

## Overview

This directory contains [sqli-labs-php7](https://github.com/skyblueee/sqli-labs-php7), a PHP7-compatible fork of the original [Audi-1/sqli-labs](https://github.com/Audi-1/sqli-labs).

sqli-labs is a learning platform for SQL injection techniques, containing intentionally vulnerable PHP applications organized into 65 lessons.

## Purpose

Used as a test dataset to validate the SQL Injection Detector's detection capabilities against known vulnerable code.

## Source

| Item | Value |
|------|-------|
| Repository | https://github.com/skyblueee/sqli-labs-php7 |
| Original | https://github.com/Audi-1/sqli-labs |
| Lessons | 65 (Less-1 through Less-65) |
| Language | PHP |

## Directory Structure

```
sqli-labs/
├── Less-1/           # Lesson 1: Error-based (String)
├── Less-2/           # Lesson 2: Error-based (Integer)
├── ...
├── Less-65/          # Lesson 65: Advanced techniques
├── sql-connections/  # Database configuration
└── images/           # Static assets
```

## SQL Injection Types Covered

| Category | Lessons | Description |
|----------|---------|-------------|
| Error-based | Less-1 to Less-4 | Exploits error messages to extract data |
| Double Injection | Less-5 to Less-6 | Nested query injection |
| Blind (Boolean) | Less-8, Less-14 | Infers data via true/false responses |
| Blind (Time-based) | Less-9, Less-10 | Infers data via response delays |
| UNION-based | Various | Combines results with injected SELECT |
| Stacked Queries | Less-38 to Less-45 | Executes multiple statements |
| Header Injection | Less-17 to Less-22 | Injection via HTTP headers |
| Second-order | Less-24 | Stored injection triggered later |
| WAF Bypass | Less-23, Less-25 to Less-28 | Techniques to bypass filters |

## Lesson Overview (from Mind Map)

| Lesson | Type | Details |
|--------|------|---------|
| Less-1 | GET - Error based | Single quotes - String |
| Less-2 | GET - Error based | Integer based |
| Less-3 | GET - Error based | Single quotes with twist - String |
| Less-4 | GET - Error based | Double quotes - String |
| Less-5 | GET - Double Injection | Single quotes - String |
| Less-6 | GET - Double Injection | Double quotes - String |
| Less-7 | GET - Dump into outfile | String |
| Less-8 | GET - Blind | Boolean based - Single quotes |
| Less-9 | GET - Blind | Time based - Single quotes |
| Less-10 | GET - Blind | Time based - Double quotes |
| Less-11 | POST - Error based | Single quotes - String |
| Less-12 | POST - Error based | Double quotes - String |
| Less-17 | POST - Update Query | Error based - String |
| Less-18 | Header Injection | User-Agent field |
| Less-19 | Header Injection | Referer field |
| Less-20 | Header Injection | Cookie field |
| Less-23 | GET - Error based | Strip comments |
| Less-25 | GET - Error based | Strip OR & AND |
| Less-26 | GET - Error based | Strip spaces and comments |
| Less-38 | GET - Stacked Queries | String |
| Less-39 | GET - Stacked Queries | Integer |
| Less-46 | GET - ORDER BY | Error based |
| Less-54 | Challenge | 10 attempts allowed |
| Less-65 | Challenge | Double quotes - Dump into file |

## Ground Truth

**No explicit ground truth file exists.**

sqli-labs is designed as a learning platform, not a benchmark dataset. Available documentation includes:
- `SQL Injections.mm` - FreeMind mind map with lesson overview
- Folder naming conventions (Less-1 through Less-65)
- README with general category classification

### Validation Approach

Since each lesson intentionally contains at least one vulnerability:
- **Expected**: Every lesson should produce at least one finding
- **Verification**: Sample lessons manually reviewed against detector output

## Representative Lessons for Testing

| Lesson | Injection Type | Expected Detector |
|--------|----------------|-------------------|
| Less-1 | Error-based (String) | classic |
| Less-2 | Error-based (Integer) | classic |
| Less-8 | Blind (Boolean-based) | classic, blind |
| Less-9 | Blind (Time-based) | classic, blind |
| Less-38 | Stacked Queries | classic, stacked |

## Running Detector on sqli-labs

```bash
# Scan all lessons
python -m sql_injection_detector.runner --path ./test/sqli-labs --format text

# Scan specific lesson
python -m sql_injection_detector.runner --path ./test/sqli-labs/Less-1 --format text

# Save report with timestamp
python -m sql_injection_detector.runner --path ./test/sqli-labs --output-dir ./reports
```

## Local Demo Setup (Optional)

To run sqli-labs locally and demonstrate actual attacks:

1. Install [XAMPP](https://www.apachefriends.org/)
2. Copy sqli-labs to `C:\xampp\htdocs\sqli-labs`
3. Start Apache and MySQL from XAMPP Control Panel
4. Access `http://localhost/sqli-labs/` and click "Setup/reset Database"
5. Navigate to individual lessons (e.g., `http://localhost/sqli-labs/Less-1/`)

See `less1_validation_report.md` for a detailed attack demonstration.