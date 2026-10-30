# Static Code Analysis – Issue Documentation

## Identified Issues

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| SQL Injection Risk | Security – Medium | 8 | SQL query uses an f-string to insert user-provided values directly into the query. | Replace string formatting with parameterized SQL queries using placeholders. |
| Unsafe eval() Usage | Security – Medium | 14 | eval() executes dynamically supplied Python expressions and may execute malicious code. | Replace eval() with a safer method for processing the salary rule. |
| Silent Exception Handling | Security – Low | 28–29 | A broad exception is caught and ignored using pass, hiding potential errors. | Catch specific exceptions and handle or report them appropriately. |
| Missing Module and Function Docstrings | Code Quality | 1, 7, 12, 24, 31, 38 | The module and functions lack documentation explaining their purpose. | Add meaningful module and function docstrings. |
| Invalid Function Naming | Code Style | 7, 24, 31, 38 | Function names use camelCase instead of Python's snake_case convention. | Rename functions using snake_case. |
| Unused Variable | Code Quality | 15 | total_seen is assigned a value but never used. | Remove the unused variable. |
| Long Lines | Code Style | 4, 8, 13, 26, 39 | Several lines exceed the recommended line length. | Break long statements into multiple readable lines. |
| Trailing Whitespace | Code Style | 15 | Unnecessary whitespace exists at the end of a line. | Remove trailing whitespace. |
| Inconsistent Return Statements | Code Quality | 12 | A function has inconsistent return statements. | Ensure all return paths follow a consistent return pattern. |
| Broad Exception Handling | Code Quality | 28 | The code catches the general Exception class instead of handling specific errors. | Catch only the relevant exception types. |
| Unspecified File Encoding | Code Quality | 32 | The open() call does not explicitly specify a file encoding. | Specify encoding="utf-8". |
| Improper File Resource Management | Code Quality | 32 | The file is opened without a context manager. | Use a with open() statement to manage the file resource safely. |
| Missing Blank Lines | Code Style | 31 | A function definition does not have the required two preceding blank lines. | Follow PEP 8 spacing conventions. |

## Summary

The static analysis tools identified security, code quality, and formatting issues in the original recruitment tracker program.

The issues will be fixed while preserving the original functionality. All three tools will be executed again after modifications to verify the improvements.