"""
SQL Injection Vulnerability Demonstration
==========================================
MIT Blended AI+X Program - Week 3

PURPOSE: Educational demonstration of SQL injection vulnerabilities.
WARNING: This code is intentionally vulnerable. NEVER use in production.

This module demonstrates:
1. A VULNERABLE pattern using string concatenation
2. Why it is dangerous (with safe simulation)
3. The attack vector explanation
"""

import sqlite3
from typing import Optional, List, Tuple


def create_demo_database() -> sqlite3.Connection:
    """
    Create an in-memory SQLite database with sample data.
    This is a controlled, local-only demonstration.
    """
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
    
    # Insert sample data (passwords are hashed in real systems)
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
# VULNERABLE PATTERN - DO NOT USE IN PRODUCTION
# =============================================================================

def vulnerable_login(conn: sqlite3.Connection, username: str, password: str) -> Optional[dict]:
    """
    VULNERABLE: Login function using string concatenation.
    
    This pattern is dangerous because user input is directly interpolated
    into the SQL query without any sanitization or parameterization.
    
    Attack vectors:
    - username: ' OR '1'='1' --
    - username: ' UNION SELECT * FROM users --
    - username: '; DROP TABLE users; --
    """
    cursor = conn.cursor()
    
    # VULNERABLE: String concatenation allows SQL injection
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    
    print(f"[VULNERABLE] Executing query: {query}")
    
    try:
        cursor.execute(query)
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


def vulnerable_search_products(conn: sqlite3.Connection, category: str) -> List[Tuple]:
    """
    VULNERABLE: Product search using string formatting.
    
    Even simple search functionality can be exploited when user input
    is directly embedded in queries.
    """
    cursor = conn.cursor()
    
    # VULNERABLE: f-string interpolation of user input
    query = f"SELECT name, price FROM products WHERE category = '{category}'"
    
    print(f"[VULNERABLE] Executing query: {query}")
    
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"[ERROR] Database error: {e}")
        return []


# =============================================================================
# DEMONSTRATION OF ATTACK PATTERNS
# =============================================================================

def demonstrate_attacks():
    """
    Demonstrate various SQL injection attack patterns.
    All attacks are performed against a local, in-memory database.
    """
    print("=" * 70)
    print("SQL INJECTION VULNERABILITY DEMONSTRATION")
    print("Educational purposes only - MIT Blended AI+X Program")
    print("=" * 70)
    print()
    
    conn = create_demo_database()
    
    # --- Attack 1: Authentication Bypass ---
    print("-" * 70)
    print("ATTACK 1: Authentication Bypass")
    print("-" * 70)
    print("Normal login attempt:")
    result = vulnerable_login(conn, "alice", "wrong_password")
    print(f"Result: {result}")
    print()
    
    print("Malicious input - bypassing authentication:")
    print("Username: ' OR '1'='1' --")
    print("Password: anything")
    # The injected query becomes:
    # SELECT * FROM users WHERE username = '' OR '1'='1' --' AND password = 'anything'
    # The condition '1'='1' is always true, and -- comments out the rest
    result = vulnerable_login(conn, "' OR '1'='1' --", "anything")
    print(f"Result: {result}")
    print()
    
    # --- Attack 2: Union-Based Data Extraction ---
    print("-" * 70)
    print("ATTACK 2: Union-Based Data Extraction")
    print("-" * 70)
    print("Normal product search:")
    products = vulnerable_search_products(conn, "Electronics")
    print(f"Results: {products}")
    print()
    
    print("Malicious input - extracting user data via UNION:")
    print("Category: ' UNION SELECT username, password FROM users --")
    # The injected query becomes:
    # SELECT name, price FROM products WHERE category = '' UNION SELECT username, password FROM users --'
    products = vulnerable_search_products(conn, "' UNION SELECT username, password FROM users --")
    print(f"Results: {products}")
    print("Note: User credentials leaked through product search!")
    print()
    
    # --- Attack 3: Boolean-Based Inference ---
    print("-" * 70)
    print("ATTACK 3: Boolean-Based Inference (Conceptual)")
    print("-" * 70)
    print("An attacker can extract data one character at a time:")
    print("Input: ' AND (SELECT SUBSTR(password,1,1) FROM users WHERE username='alice')='h' --")
    print("If the query returns results, the first character of alice's password is 'h'")
    print("This is repeated to extract entire secrets character by character.")
    print()
    
    conn.close()
    
    print("-" * 70)
    print("WHY THIS IS DANGEROUS:")
    print("-" * 70)
    print("1. Authentication bypass: Attackers gain unauthorized access")
    print("2. Data extraction: Sensitive data from any table can be leaked")
    print("3. Data modification: INSERT/UPDATE/DELETE can modify data")
    print("4. Denial of service: DROP TABLE can destroy data")
    print("5. Privilege escalation: Attackers may gain admin access")
    print()


if __name__ == "__main__":
    demonstrate_attacks()
