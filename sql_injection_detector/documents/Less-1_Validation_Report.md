# SQL Injection Detector - Validation Report: Less-1

## Overview

| Item | Value |
|------|-------|
| Target | sqli-labs/Less-1 (Error-based SQL Injection) |
| Expected Vulnerability | SQL query with variable interpolation |
| Test Date | 2026-01-07 |

---

## 1. Initial Scan Result

```
============================================================
SQL INJECTION DETECTOR REPORT
SCAN SUMMARY
Timestamp:       2026-01-07T15:52:27.519478
Files Scanned:   1
Total Findings:  26
Detectors Run:   classic, blind, oob, stacked
============================================================
RESULTS BY FILE

[VULNERABLE] test\sqli-labs\Less-1\index.php
  Finding #1
    Detector:    classic
    Type:        string_concat
    Severity:    HIGH
    Location:    Line 29, Column 6
    Pattern:     double_quote_sql_variable
    Description: SQL query in double quotes with variable interpolation
    Code:        $sql="SELECT * FROM users WHERE id='$id' LIMIT 0,1";
  Finding #2
    Detector:    classic
    Type:        unsafe_execute
    Severity:    MEDIUM
    Location:    Line 30, Column 9
    Pattern:     mysql_query_usage
    Description: mysql_query() is deprecated - use mysqli or PDO with prepared statements
    Code:        $result=mysql_query($sql);
  Finding #3
    Detector:    oob
    Type:        dns_exfiltration
    Severity:    HIGH
    Location:    Line 1, Column 25
    Pattern:     mysql_load_file_unc
    Description: LOAD_FILE() with UNC path (MySQL) - DNS exfiltration
    Code:        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
  Finding #4
    Detector:    oob
    Type:        dns_exfiltration
    Severity:    HIGH
    Location:    Line 2, Column 19
    Pattern:     mysql_load_file_unc
    Description: LOAD_FILE() with UNC path (MySQL) - DNS exfiltration
    Code:        <html xmlns="http://www.w3.org/1999/xhtml">

... (22 similar false positive findings omitted) ...

  Finding #26
    Detector:    oob
    Type:        dns_exfiltration
    Severity:    HIGH
    Location:    Line 26, Column 1
    Pattern:     mssql_xp_subdirs
    Description: xp_subdirs with UNC path (MSSQL) - DNS exfiltration
    Code:        // connectivity
============================================================
```

### Analysis

| Category | Count |
|----------|-------|
| True Positive | 2 |
| False Positive | 24 |

**True Positives (Correct):**
- Line 29: `$sql="SELECT * FROM users WHERE id='$id' LIMIT 0,1";`
- Line 30: `mysql_query($sql);`

**False Positives (Incorrect):**
- 24 OOB findings triggered by `//` in HTML comments and URLs

---

## 2. Root Cause

Regex OR operator grouping bug in `patterns/common/oob.yaml`:

```yaml
# Before (buggy)
regex: "\\bxp_dirtree\\s*['\"]\\\\\\\\|//"
# Interpreted as: (xp_dirtree...) OR (//)

# After (fixed)
regex: "\\bxp_dirtree\\s*['\"](?:\\\\\\\\|//)"
# Interpreted as: xp_dirtree... followed by (\\\\ OR //)
```

This bug affected 4 patterns: `mysql_load_file_unc`, `mssql_xp_dirtree`, `mssql_xp_fileexist`, `mssql_xp_subdirs`

---

## 3. Post-Fix Scan Result

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

[VULNERABLE] test\sqli-labs\Less-1\index.php
  Finding #1
    Detector:    classic
    Type:        string_concat
    Severity:    HIGH
    Location:    Line 29, Column 6
    Pattern:     double_quote_sql_variable
    Description: SQL query in double quotes with variable interpolation
    Code:        $sql="SELECT * FROM users WHERE id='$id' LIMIT 0,1";
  Finding #2
    Detector:    classic
    Type:        unsafe_execute
    Severity:    MEDIUM
    Location:    Line 30, Column 9
    Pattern:     mysql_query_usage
    Description: mysql_query() is deprecated - use mysqli or PDO with prepared statements
    Code:        $result=mysql_query($sql);
============================================================
```

### Verification

| Metric | Before | After |
|--------|--------|-------|
| Total Findings | 26 | 2 |
| True Positives | 2 | 2 |
| False Positives | 24 | 0 |

---

## Conclusion

- ✓ Primary vulnerability correctly detected (Line 29)
- ✓ False positives eliminated after regex fix
- ✓ No detection loss from the fix