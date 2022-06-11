# Testing Phase

## Goal

- Write sample automated tests for usage in CI/CD processes.
- Write a **functional test** for the Python app and **integration tests** for to NodeJS app.

## Python App

- Use an appropriate testing framework (e.g., `pytest`).
- Use a recommended directory hierarchy for organizing tests. For example:
  - A separate directory `tests` with subdirectories for `unit` or `functional` tests, etc.
  - Add an `__init__` script to the directory (even if empty) to mark it as a module and to avoid unintended code execution when importing the test module.
  - You can use manager script in `tests` to conveniently run test suites.
- Document tests using the common GIVEN-WHEN-THEN scheme.

### Notes:

- Since the application is small, there is no room for using extra capabilities, however it’s worth mentioning:
  - **Fixtures:** help initialize the state for the test functions to avoid duplicating initialization code for each test.
  - **Code coverage:** a popular metric for testing quality that measures the number of lines validated by tests.

## NodeJS App

- Use an appropriate testing framework (e.g., Jest).
  - To configure IDE support for Jest types, install `@types/jest`
  - To use TypeScript with Jest, install `ts-jest`
  - Testing dependencies should be installed as dev dependencies.

- Set up the testing server before running any test and close it after running all of them to avoid code duplication.
  - Make sure the server is running before starting tests, this can be achieved by using callbacks or a package like `start-server-and-test` 

- Use a recommended directory hierarchy and file naming for tests.
  - Tests in NodeJS can be stored in a separate `tests` directory or along with code with the suffix `.test.ts` or `.spec.ts` 

- Organize tests into logical test suites and make sure they don’t depend on each other and don’t change application state.

