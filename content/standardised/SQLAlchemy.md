---
aliases: 
category: DE
date modified: 1-08-2025
tags:
  - python
  - database
  - SQL
---
SQLAlchemy is a Python SQL toolkit and ==[[Object Relational Mapper]]== (ORM) that provides tools to interact with databases in a more Pythonic way. It allows you to work with relational databases such as MySQL, PostgreSQL, SQLite, and others without writing raw [[SQL]] queries manually.

Related:
- [[SQLAlchemy vs. sqlite3]]

In [[DE_Tools]] see:
- https://github.com/rhyslwells/DE_Tools/blob/main/Explorations/SQLAlchemy/sql_alchemy.ipynb

### Why Use SQLAlchemy?

- Reduces SQL complexity: Write Python code instead of SQL queries.
- Prevents [[SQL Injection]]: ORM prevents unsafe queries.
- Improves [[Maintainability]]: Easier to refactor code.
- Handles connection pooling: Manages database connections efficiently.
- Works with Pandas: Can load and save data directly to databases.
### Key Features of SQLAlchemy

1. Database Connectivity
    - Provides a unified interface to connect to different databases.
      
2. SQL Query Execution
    - Allows execution of raw SQL queries using [[Pandas]]
      
3. ORM (Object Relational Mapping)
    - Converts database tables into Python objects (classes).
    - Eliminates the need to write SQL [[Querying|Queries]] manually.
    - Example:
        ```python
        from sqlalchemy.orm import declarative_base
        from sqlalchemy import Column, Integer, String
        
        Base = declarative_base()
        
        class Customer(Base):
            __tablename__ = 'customers'
            id = Column(Integer, primary_key=True)
            name = Column(String)
            phone_number = Column(String)
        ```
4. Transaction Management
    - Provides robust control over commit and rollback operations.
    - Ensures data integrity by handling failures safely.
      
5. Efficient Query Building
    - Allows writing Pythonic queries instead of raw SQL.
    - Example:
        
        ```python
        from sqlalchemy.orm import sessionmaker
        
        Session = sessionmaker(bind=engine)
        session = Session()
        
        customers = session.query(Customer).filter_by(name="John Doe").all()
        ```
        
6. Supports Multiple Databases
    - Works with [[MySql]] ,[[PostgreSQL]], [[SQLite]], etc.
    - Easily switch databases without changing the core logic.
