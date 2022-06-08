# Testing Phase

## Python App

- Use an appropriate testing framework (e.g., `pytest`).
- Use a recommended directory hierarchy for organizing tests. For example:
  - A separate directory `tests` with subdirectories for `unit` or `functional` tests, etc.
  - Add an `__init__` script to the directory (even if empty) to avoid unintended code execution when importing the test module.
  - A manager script in `tests` to conveniently run test suites.
- Document tests using the common GIVEN-WHEN-THEN scheme.

### Notes:

- Since the application is small, there is no room for using extra capabilities, however it’s worth mentioning:
  - **Fixtures:** help initialize the state for the test functions to avoid duplicating initialization code for each test.
  - **Code coverage:** a popular metric for testing quality that measures the number of lines validated by tests.



## NodeJS App

- Use an appropriate testing framework (e.g., Jest).
- 

