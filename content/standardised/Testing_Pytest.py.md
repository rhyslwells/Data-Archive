https://github.com/rhyslwells/ML_Tools/tree/main/Explorations\Deployment\Testing_Pytest.py

In [[ML_Tools]] see: [[Testing_Pytest.py]]

The `pytest` example script demonstrates several key features of the [[Pytest]] testing framework:

1. **Fixtures**: The script uses a fixture named `sample_data` to provide common test data that can be reused across multiple test functions. This helps reduce code duplication and enhances test maintainability.

2. **Parametrization**: The script employs the `@pytest.mark.parametrize` decorator to run a test function with multiple sets of arguments. This allows for testing a function with various inputs without writing separate test cases for each scenario.

3. **Custom Markers**: A custom marker `@pytest.mark.slow` is used to categorize tests. This enables selective test execution based on markers, allowing you to run specific groups of tests using the `-m` option.

4. **Mocking**: The script demonstrates how to use `unittest.mock.patch` with `pytest` to replace a function with a mock. This allows for controlling the behavior of the function during the test, facilitating isolated testing of units.


