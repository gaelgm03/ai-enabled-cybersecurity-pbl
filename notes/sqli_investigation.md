# SQL Injection

## ¿What is SQLi?
A Structured Query Language injection is a type of cybernetic attack which exploits a lack of validation of user imputs. Then, when the application executes a query to its database, the attacker can interfere with it and access information that should not be accessible to them, sometimes even allowing them to modify the data.

## Impacts of a successful SQLi attack
- Leakage of sensitive data
  - Usernames, passwords, addresses, contact information, financial information, etc.
- General access to the database by the attacker
  - Loss of information, denial-of-service attacks

## Types of SQLi attacks

### In-band SQLi
The attacker uses the same channel for the attack and to retrieve results
- **Error-based SQLi:** The attacker uses an SQL command to purposefully cause an error message from the data server. These messages often expose information about the database that is useful to the attackers. This only works if the application shows raw database error messages.
  - Example: In an application, there is a login form that builds a query using this code: `SELECT * FROM users WHERE id = 'USER_INPUT';`.
  - Then, an attacker could input something like `' AND 1 = CAST((SELECT database()) AS INT)--`.
  - The first " ' " closes the original string in the query, so now the attacker can inject SQL logic. In the next part, the "AND" adds a condition to the WHERE clause in the original query. Then the "(SELECT database())" returns the name of the database, and when the "CAST" command tries to convert it into an integer, the error occurs, because database names are not integers. Finally, the "--" ensures that the query executes correctly by commenting out the rest of the original SQL query. The 1=... condition is only there so that the error occurs in the CAST command and not before, since the WHERE requires a valid boolean statement to execute.
  - The resulting, injected query would look like this: `SELECT * FROM users WHERE id = '' AND 1 = CAST((SELECT database()) AS INT)--';`.
  - This causes the database to try to convert a string to an integer, causing a conversion error message that can include the name of the database.
  - This attack can also be used to extract table names, column names, or even concrete data.
- **Union-based SQLi:** The attacker uses the UNION SQL command to combine multiple statements and return a single HTTP response, allowing the attacker to extract information from the database. This is the most common type of SQL injection, and it works when the application displays query results and the attacker can match the number and types of columns.
  - Example: In an application, the app gets product data from the database using this prompt: `SELECT name, price FROM products WHERE category = 'USER_INPUT';`
  - Then the attacker can input: `' UNION SELECT username, password FROM users--`.
  - Again, the " ' " closes the original string, and the rest of the injected query pulls the usernames and passwords of the users. However, for this to work the number of columns and data types have to match in the result. If they don't, the attacker can use explicit conversions to work around it (for instance, they may ask the database for the user's password in ASCII).
  - The resulting query would be: `SELECT name, price FROM products WHERE category = '' UNION SELECT username, password FROM users--';`
  - This would return a table of information.

### Inferencial SQLi
It is also called blind SQLi because there is no explicit data transfer from the database to the attacker. Instead, the attacker uses these methods to learn about the structure of the database by observing its response. Inferencial SQLi attacks are less common than In-band SQLi because they take longer to complete.
- **Boolean injection:** The attacker sends a query designed to force the application to return a true or false result. Then, the content of the HTTP response will change, allowing the attacker to know if the query returned true or false. These attacks are usually very slow because the attacker needs to reconstruct the database character by character.
  - Example: An app checks whether a user exists using: `SELECT * FROM users WHERE username = 'USER_INPUT';`
  - The application returns "user exists" if there is at least one result, and "user not found" if there is not.
  - An attacker might test different inputs. For instance, `' AND 1 = 1--`
  - The resulting query would be `SELECT * FROM users WHERE username = '' AND 1 = 1--';`
  - Knowing the original query, this input will not change anything: 1 = 1 is always true, so the query will behave normally.
  - Now the attacker could test `' AND 1 = 2--`
  - The resulting query would be `SELECT * FROM users WHERE username = '' AND 1 = 2--';`
  - 1 = 2 is always false, so the query will not return anything, meaning the page behavior will change. Now, knowing how the behavior of the application changes with injections of logic, the attacker can test for different conditions.
  - For example, the attacker could prompt `' AND (SELECT LENGTH(database())) > 5--`
  - If the page behaves normally, it means that the response is true, so the attacker now knows that the length of the database name is greater than 5. This can be done many times to find out numbers of columns and rows, their names, and characters at specific positions, allowing the attacker to reconstruct the entire database through iteration.
- **Time-based injection:** The attacker sends a query instructing the database to wait a specified amount of time before responding, but with a specific condition. For instance, the attacker could force the database to wait only if the response is true. Then, the attacker can infer the boolean value of the response by whether or not there is a delay in the HTTP response. This method is extremely reliable, but also very slow, because, just like the boolean injection, the attacker is required to reconstruct the database one character at a time.
  - Example: Again, an application checks whether a user exists using: `SELECT * FROM users WHERE username = 'USER_INPUT';`.
  - The attacker could inject the input: `' AND IF(LENGTH(database()) > 5, SLEEP(3), 0)--`
  - Resulting query: `SELECT * FROM users WHERE username = '' AND IF(LENGTH(database()) > 5, SLEEP(3), 0)--';`
  - This line establishes a condition in which, if the name of the database is greater than 5, the database waits 3 seconds before returning the information. This will not change the behavior of the application whatsoever, it will simply change the response time of the database. By timing those responses, the attacker can learn whether the condition was true or false.

## References
1. Dougherty, C. (2012). Practical Identification of SQL Injection Vulnerabilities. CISA; United States Computer Emergency Readiness Team. [https://www.cisa.gov/sites/default/files/publications/Practical-SQLi-Identification.pdf](https://www.cisa.gov/sites/default/files/publications/Practical-SQLi-Identification.pdf)

1. Microsoft Learn. (2025, November 18). SQL injection - SQL Server. Microsoft.com; Microsoft. [https://learn.microsoft.com/en-us/sql/relational-databases/security/sql-injection?view=sql-server-ver17](https://learn.microsoft.com/en-us/sql/relational-databases/security/sql-injection?view=sql-server-ver17)

1. OWASP. (n.d.). Testing for SQL injection. OWASP; Open Worldwide Application Security Project. Retrieved December 19, 2025, from [https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/05-Testing_for_SQL_Injection](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/05-Testing_for_SQL_Injection)

1. PortSwigger. (2024). SQL injection. Portswigger; Portswigger. [https://portswigger.net/web-security/sql-injection](https://portswigger.net/web-security/sql-injection)
