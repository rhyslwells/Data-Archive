### **`@pytest.fixture` Explanation**

`@pytest.fixture` is a decorator in `pytest` used to define reusable test setup functions. It allows tests to use shared resources without redundant code.

#### **Example & Usage**

python

Copy code

`import pytest  @pytest.fixture def sample_data():     return {"name": "John Doe", "age": 30}      def test_example(sample_data):     assert sample_data["name"] == "John Doe"     assert sample_data["age"] == 30`

🔹 **How it works:**

- The function `sample_data()` is decorated with `@pytest.fixture`, making it a fixture.
- The test function `test_example()` receives `sample_data` as an argument.
- `pytest` automatically provides the fixture data when running the test.

#### **Why use fixtures?**

- Avoids repetitive setup code.
- Ensures clean test environments.
- Can handle resource management (e.g., opening/closing database connections, creating temporary files).