"""
SQL Injection - Secure Implementation
======================================
MIT Blended AI+X Program - Week 3

PURPOSE: Demonstrate secure coding patterns that prevent SQL injection.

This module shows the CORRECT way to handle user input in database queries:
1. Parameterized queries (prepared statements)
2. Input validation
3. Defense in depth
"""

import sqlite3
import re
from typing import Optional, List, Tuple


def create_demo_database() -> sqlite3.Connection:
    """Create an in-memory SQLite database with sample data."""
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT,
            role TEXT DEFAULT 'user'
        )
    """)
    
    cursor.execute("""
        CREATE TABLE products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL,
            category TEXT
        )
    """)
    
    sample_users = [
        ("alice", "hashed_password_1", "alice@example.com", "admin"),
        ("bob", "hashed_password_2", "bob@example.com", "user"),
        ("charlie", "hashed_password_3", "charlie@example.com", "user"),
    ]
    cursor.executemany(
        "INSERT INTO users (username, password, email, role) VALUES (?, ?, ?, ?)",
        sample_users
    )
    
    sample_products = [
        ("Laptop", 999.99, "Electronics"),
        ("Book", 19.99, "Education"),
        ("Headphones", 149.99, "Electronics"),
    ]
    cursor.executemany(
        "INSERT INTO products (name, price, category) VALUES (?, ?, ?)",
        sample_products
    )
    
    conn.commit()
    return conn


# =============================================================================
# SECURE PATTERN 1: Parameterized Queries
# =============================================================================

def secure_login(conn: sqlite3.Connection, username: str, password: str) -> Optional[dict]:
    """
    SECURE: Login function using parameterized queries.
    
    The ? placeholders are replaced by the database driver with properly
    escaped values. The user input is NEVER directly interpolated into
    the SQL string.
    
    This prevents SQL injection because:
    - Input is treated as DATA, not as SQL code
    - Special characters are automatically escaped
    - The query structure cannot be altered by user input
    """
    cursor = conn.cursor()
    
    # SECURE: Parameterized query with ? placeholders
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    
    print(f"[SECURE] Executing parameterized query")
    print(f"[SECURE] Parameters: username={repr(username)}, password=***")
    
    try:
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        if result:
            return {
                "id": result[0],
                "username": result[1],
                "email": result[3],
                "role": result[4]
            }
    except sqlite3.Error as e:
        print(f"[ERROR] Database error: {e}")
    
    return None


def secure_search_products(conn: sqlite3.Connection, category: str) -> List[Tuple]:
    """
    SECURE: Product search using parameterized query.
    
    Even with malicious input like:
    "' UNION SELECT username, password FROM users --"
    
    The query treats this entire string as a literal category value,
    not as SQL code. No results will be returned because no category
    matches that exact string.
    """
    cursor = conn.cursor()
    
    # SECURE: Parameterized query
    query = "SELECT name, price FROM products WHERE category = ?"
    
    print(f"[SECURE] Executing parameterized query")
    print(f"[SECURE] Parameter: category={repr(category)}")
    
    try:
        cursor.execute(query, (category,))
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"[ERROR] Database error: {e}")
        return []


# =============================================================================
# SECURE PATTERN 2: Input Validation (Defense in Depth)
# =============================================================================

def validate_username(username: str) -> bool:
    """
    Validate username format before using in queries.
    
    Even with parameterized queries, input validation provides
    defense in depth and catches invalid data early.
    """
    if not username:
        return False
    if len(username) < 3 or len(username) > 50:
        return False
    # Allow only alphanumeric characters and underscores
    if not re.match(r'^[a-zA-Z0-9_]+$', username):
        return False
    return True


def validate_category(category: str) -> bool:
    """
    Validate category against an allowlist.
    
    For fields with known valid values, allowlisting is the
    strongest form of validation.
    """
    valid_categories = {"Electronics", "Education", "Books", "Clothing"}
    return category in valid_categories


def secure_login_with_validation(
    conn: sqlite3.Connection, 
    username: str, 
    password: str
) -> Optional[dict]:
    """
    SECURE: Login with input validation + parameterized query.
    
    This demonstrates defense in depth:
    1. First validate input format
    2. Then use parameterized query
    
    Even if validation is bypassed, parameterization prevents injection.
    """
    # Layer 1: Input validation
    if not validate_username(username):
        print(f"[SECURE] Invalid username format rejected: {repr(username)}")
        return None
    
    if not password or len(password) < 1:
        print("[SECURE] Invalid password rejected")
        return None
    
    # Layer 2: Parameterized query
    return secure_login(conn, username, password)


# =============================================================================
# DEMONSTRATION
# =============================================================================

def demonstrate_secure_patterns():
    """
    Demonstrate that secure patterns prevent SQL injection.
    """
    print("=" * 70)
    print("SECURE SQL PATTERNS DEMONSTRATION")
    print("Educational purposes - MIT Blended AI+X Program")
    print("=" * 70)
    print()
    
    conn = create_demo_database()
    
    # --- Test 1: Normal Usage ---
    print("-" * 70)
    print("TEST 1: Normal Login (Secure)")
    print("-" * 70)
    result = secure_login(conn, "alice", "hashed_password_1")
    print(f"Result: {result}")
    print()
    
    # --- Test 2: Attempted Attack - Blocked ---
    print("-" * 70)
    print("TEST 2: Attempted SQL Injection (Blocked)")
    print("-" * 70)
    print("Malicious input: ' OR '1'='1' --")
    result = secure_login(conn, "' OR '1'='1' --", "anything")
    print(f"Result: {result}")
    print("Attack blocked! The malicious string was treated as a literal username.")
    print()
    
    # --- Test 3: Union Attack - Blocked ---
    print("-" * 70)
    print("TEST 3: Attempted Union Attack (Blocked)")
    print("-" * 70)
    print("Malicious category: ' UNION SELECT username, password FROM users --")
    products = secure_search_products(
        conn, 
        "' UNION SELECT username, password FROM users --"
    )
    print(f"Results: {products}")
    print("Attack blocked! No data leaked because input was treated as literal value.")
    print()
    
    # --- Test 4: Validation + Parameterization ---
    print("-" * 70)
    print("TEST 4: Defense in Depth (Validation + Parameterization)")
    print("-" * 70)
    print("Attempting login with malicious username:")
    result = secure_login_with_validation(conn, "' OR '1'='1' --", "anything")
    print(f"Result: {result}")
    print("Rejected at validation layer before reaching database!")
    print()
    
    conn.close()
    
    print("-" * 70)
    print("WHY THESE PATTERNS ARE SECURE:")
    print("-" * 70)
    print("1. Parameterized queries separate SQL code from data")
    print("2. The database driver handles escaping automatically")
    print("3. Query structure cannot be altered by user input")
    print("4. Input validation provides additional protection")
    print("5. Defense in depth: multiple layers of security")
    print()
    print("-" * 70)
    print("BEST PRACTICES SUMMARY:")
    print("-" * 70)
    print("- ALWAYS use parameterized queries (?, :name, or %s placeholders)")
    print("- NEVER concatenate user input into SQL strings")
    print("- Validate input format and length")
    print("- Use allowlists for fields with known valid values")
    print("- Apply principle of least privilege to database accounts")
    print("- Use an ORM with built-in protections when possible")
    print()


if __name__ == "__main__":
    demonstrate_secure_patterns()
