---
tags: 
aliases: 
category: 
phase: 
topic: 
filename:
---
### **`@patch` (from `unittest.mock`) Explanation**

`@patch` is used to replace objects/functions with mock versions during tests. It is part of Python’s `unittest.mock` module.

#### **Example & Usage**

python

Copy code

`from unittest.mock import patch  def fetch_data():     """Simulated function that fetches data from an API"""     return "Real Data"  @patch("__main__.fetch_data", return_value="Mocked Data") def test_fetch_data(mock_fetch):     assert fetch_data() == "Mocked Data"`

🔹 **How it works:**

- `@patch("__main__.fetch_data", return_value="Mocked Data")` replaces `fetch_data()` with a mocked version returning `"Mocked Data"`.
- Inside the test, `fetch_data()` will **always** return `"Mocked Data"` instead of calling the real function.

#### **Why use `@patch`?**

- Prevents tests from making actual API/database calls.
- Speeds up testing by mocking expensive operations.
- Allows control over return values and side effects.

---

### **Your Case:**

- **`@pytest.fixture`** is used to provide reusable test data (`mock_files`).
- **`@patch`** is used to:
    - Mock file operations (`builtins.open`, `os.walk`).
    - Mock function calls (`process_file`, `log_action`, `write_updated_file`).
    - Prevent real file modifications while testing.