SQL injection is a code injection technique that targets applications using SQL databases. It occurs when a malicious user injects harmful SQL code into a query, potentially compromising the security of the database. 

### How SQL Injection Works

Consider a scenario where a website prompts users to log in with their username and password. The application might execute a query like this:

```sql
SELECT `id` FROM `users`
WHERE `user` = 'Carter' AND `password` = 'password';
```

If the user named Carter enters their credentials correctly, the query functions as intended. However, a malicious user could input a different string, such as:

```
password' OR '1' = '1
```

This alters the query to:

```sql
SELECT `id` FROM `users`
WHERE `user` = 'Carter' AND `password` = 'password' OR '1' = '1';
```

As a result, the attacker could gain unauthorized access to the database.

### Example of Vulnerable Code

The following Python function demonstrates how SQL injection can occur due to unsafe query construction:

```python
import sqlite3

def unsafe_query(user_input):
    query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    conn = sqlite3.connect('example.db')
    conn.execute(query)
```

In this example, the `unsafe_query` function constructs SQL queries using string concatenation, making it vulnerable if user input is not properly sanitized.

### Preventing SQL Injection

To mitigate the risk of SQL injection, it is essential to use prepared statements or parameterized queries. For example, consider an SQL injection attack that aims to display all user accounts from the `accounts` table:

```sql
SELECT * FROM `accounts`
WHERE `id` = 1 UNION SELECT * FROM `accounts`;
```

Using a prepared statement, we can safeguard against such attacks:

```sql
PREPARE `balance_check`
FROM 'SELECT * FROM `accounts`
WHERE `id` = ?';
```

In this statement, the question mark acts as a placeholder for user input, preventing the execution of unintended SQL code.

### Executing the Prepared Statement

To execute the prepared statement and check a user’s balance, we can set a variable for the user ID:

```sql
SET @id = 1;
EXECUTE `balance_check` USING @id;
```

Here, the `SET` statement simulates obtaining the user’s ID through the application, with the `@` symbol denoting a variable in MySQL.

### Testing with Malicious Input

If we attempt to run the same statements with a malicious ID:

```sql
SET @id = '1 UNION SELECT * FROM `accounts`';
EXECUTE `balance_check` USING @id;
```

The output will still reflect the balance of the user with ID 1, without exposing any additional data. This demonstrates that prepared statements effectively prevent SQL injection attacks.

### Mitigation Strategies

- **Use Parameterized Queries**: Always use parameterized queries or prepared statements to prevent SQL injection.
- **Validate and Sanitize Inputs**: Ensure user inputs are validated and sanitized before being processed.
