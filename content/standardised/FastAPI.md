---
aliases: 
category: 
date modified: 27-07-2025
tags:
  - frontend
  - devops
---
**FastAPI** is a modern web framework for building APIs with Python. It is designed to be fast and easy to use, leveraging Python's type hints to provide features like:

1. Automatic generation of OpenAPI documentation.
2. Input data validation based on Python's type annotations.
3. Asynchronous request handling with native support for `asyncio`.
4. High performance, as it is built on Starlette and [[Pydantic]].
### Key Features

- **Automatic validation:** Based on type hints and Pydantic models.
- **Interactive API docs:** Automatically generated Swagger UI and ReDoc.
- **Asynchronous support:** Full support for async functions.
- **Dependency injection:** Built-in support for dependencies.

### How to Run

==In [[ML_Tools]] see: [[FastAPI_Example.py]]== <- see this

1. Save the script as `main.py`.
2. Install FastAPI and Uvicorn:
    `pip install fastapi uvicorn`
    
3. Run the server:  
	```cmd
	ren FastAPI_Example.py main.py # possibly change to
	uvicorn FastAPI_Example:app --reload
	```
    
4. Open the browser and navigate to:
    - **API documentation (Swagger UI):** `http://127.0.0.1:8000/docs`
    - **ReDoc documentation:** `http://127.0.0.1:8000/redoc`