---
aliases: []
category:
date modified: 27-07-2025
tags: []
---
### How to Add a Database to PostgreSQL  

### Using pgAdmin (GUI)  

1. Open pgAdmin and log in.  
2. In the Object Explorer, right-click Databases → Create → Database.  
3. Enter Database Name (e.g., `mydatabase`).  
4. Choose an Owner (optional).  
5. Click Save.  
### Using Python (`psycopg2`)  

If you're using Python (e.g., in a Jupyter Notebook), install the `psycopg2` package if needed:  

```python
!pip install psycopg2-binary
```

Then, run this script to create a PostgreSQL database:  

```python
import psycopg2

# Connect to the PostgreSQL server (default 'postgres' database)
conn = psycopg2.connect(
    dbname="postgres",  # Default DB to connect before creating a new one
    user="postgres",
    password="your_password",
    host="localhost"
)
conn.autocommit = True  # Required for CREATE DATABASE
cursor = conn.cursor()

# Create a new database
cursor.execute("CREATE DATABASE mydatabase;")

# Close connection
cursor.close()
conn.close()
print("Database 'mydatabase' created successfully!")
```