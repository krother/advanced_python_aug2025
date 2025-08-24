
# Testing

## 1. Running Tests

Run the tests for the `space_game` package:

  uv run pytest -v -x -s --cov

Explain the options.

if the gui tests do not work, use

  uv run pytest --ignore tests/test_space.py

## 2. Pytest

Examine the tests in `test_space.py`

## 3. Unittest

Compare the test in `test_pi.py`

## 4. Mocking

Examine the test in `test_cli.py` and how the keyboard input is avoided.

Also compare the code in `mock_example.py`
Both tests contain a **context manager**.

## 5. Test Parametrization

In `test_words.py` you find an example of test parameterization and testing against an error.
Make the tests work.

## 6. Fixtures

Move the fixture in `space_game.py` to a file `conftest.py`.
Discuss the scope of fixtures (session, module, class, test).

## 7. Test data

Examine the folder structure in `tests/test_data/` . Discuss pros and cons.

# 8. Playwright: Web front-end testing

Remote-control your browser. Run from the command line:

    pip install playwright
    playwright install

Generate test code with

    playwright codegen www.wikipedia.org

Before closing the browser, copy the generated code.
To run it, add imports:

    import playwright
    from playwright.sync_api import sync_playwright, Playwright

before closing the context, add:

    page.screenshot(path="screenshot.png")

Execute the code with Python.

## Links

- [Test Automation](https://python-basics-tutorial.readthedocs.io/en/latest/test/index.html)
- [Pytest usage guide](https://python-basics-tutorial.readthedocs.io/en/latest/test/pytest/index.html)
- [Pytest library](https://docs.pytest.org)
- [Tutorial by Kristian](https://www.academis.eu/python_testing/)
- [Playwright](https://playwright.dev/python/)
