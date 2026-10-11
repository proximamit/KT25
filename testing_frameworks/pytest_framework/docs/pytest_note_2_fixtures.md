### fixtures in pytest

Fixtures are especially useful when tests need common objects or resources.

- Pytest runs the fixture when a test requests it.
- fixtures are functions that provide reusable setup or test data to our tests.
- They help us avoid repeating code and make tests easier to maintain.
- For example, instead of creating a user object inside every test, we can create it once as a fixture and ask pytest to provide it wherever needed.

## Fixture scope: how often does it run?

Pytest supports different fixture scopes that determine how long a fixture is reused.

| Scope | Fixture runs |
| --- | --- |
| `function` | Once per test function (default) |
| `class` | Once per test class |
| `module` | Once per Python test module |
| `package` | Once per package, subject to package boundaries |
| `session` | Once per test session |