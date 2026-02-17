---
aliases:
- null
category: DE
date modified: 27-09-2025
tags:
- database
- programming
- SQL
---
Lightweight [[Database Management System (DBMS)|DBMS]] used in various applications (phone apps, desktop apps, websites).

Note [[SQLite Studio]] exists

To get in terminal enter: sqlite3 database.db

SQLite—and by extension SQLiteStudio—==operates on a local database file==. There is no built-in client–server protocol, network listener, or authentication layer. SQLiteStudio can only open a .db file that is accessible via the local filesystem.
### Why this limitation exists

SQLite is an embedded database engine. Its execution model assumes:

- The database is a file on disk.
- The process accessing it has direct filesystem access.
- [[Concurrency]] is handled via file locks, not network coordination.
    
Because of this, SQLite has no concept of:

- Remote connections
- Hosts, ports, or users
- Network latency or access control

SQLiteStudio is simply a GUI wrapper around this model.
### What is possible (practical options)

#### Copy the database file back and forth

Manual or scripted transfer:

- scp, rsync, shared folder
- Open locally in SQLiteStudio on each machine
- Safe, simple, but not real-time.
#### 3. Run a thin service on top of SQLite (recommended pattern)

If you need remote access:

- Keep SQLite local to Laptop A
- Expose access via:
- A small REST API (e.g. [[FastAPI]], Flask)
- A CLI tool callable over SSH
- Laptop B queries the service, not the database file
- This preserves SQLite’s strengths and avoids corruption.

#### 4. Switch to a client–server database

If remote GUI access is a requirement, SQLite is the wrong tool.

Alternatives:

- [[PostgreSQL]]
- [[MySQL]] / [[MariaDB]]

SQLiteStudio will not help here, but tools like:

- [[pgAdmin]]
- DBeaver
- DataGrip

are designed for this model.

Related notes:
- [[Querying]]
- [[Concurrency]]
- [[SQL]]
- [[Trigger]]