# Testing

## Table of Contents

1. [Goal](#1-Goal)

2. [Steps](#2-Steps)

   2.1. [Python App](#21-Python-App)

   2.2. [NodeJS App](#22-NodeJS-App)

3. [Best Practices](#3-Best-Practices)

   3.1. [Python App](#31-Python-App)

   3.2. [NodeJS App](#32-NodeJS-App)

## 1. Goal

- Write sample automated tests for usage in CI.
- Write a **functional test** for the Python app and **integration tests** for the NodeJS app.

## 2. Steps

### 2.1. Python App

- Add `pytest` to project dependencies and freeze the environment.
- Create [tests](../app_python/tests) module with a `test_<unit>.py` file for each test unit.
- Run `python -m pytest` to verify tests are working.
- Add testing instructions to README.

### 2.2. NodeJS App

- Install `jest` as a dev dependency with `npm install --save-dev`
- Install `@types/jest` to configure IDE support for jest.
- Install `ts-jest` to use TypeScript with jest.
- Write [test suites](../app_nodejs/tests) and run `jest` to verify that tests are working.
- Add script to `package.json` to quickly run tests for CI/CD.  
- Add testing instructions to README.

## 3. Best Practices

### 3.1. Python App

- Use an appropriate testing framework (e.g., `pytest`).
- Use a recommended directory hierarchy for organizing tests.
- Add an `__init__` script to the directory (even if empty) to mark it as a module and to avoid unintended code execution when importing the test module.
- Document tests using the common GIVEN-WHEN-THEN scheme.
- **Note:** since the application is small, there is no room for using extra capabilities, however it’s worth mentioning:

  - **Fixtures:** help initialize the state for the test functions to avoid duplicating initialization code for each test.

  - **Code coverage:** a popular metric for testing quality that measures the number of lines validated by tests.

### 3.2. NodeJS App

- Use an appropriate testing framework (e.g., Jest).
- Testing dependencies should be installed as dev dependencies.
- Set up the testing server before running any test and close it after running all of them to avoid code duplication.
  - Make sure the server is running before starting tests, this can be achieved by using callbacks or a package like `start-server-and-test`
- Use a recommended directory hierarchy and file naming for tests.
  - Tests in NodeJS can be stored in a separate `tests` directory or along with code with the suffix `.test.ts` or `.spec.ts`
- Organize tests into logical test suites and make sure they don’t depend on each other and don’t change application state.
