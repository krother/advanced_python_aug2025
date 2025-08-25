
# Test Automation

## 1. Automated Tests

In [test_words.py](test_words.py) you find an examples of:

- a simple test with pytest
- a test against an Exception
- a test with a fixture
- a parametrized test

Run the tests with

  uv run pytest

Make the tests work by implementing a `word_count()` function.

## 2. Write Tests

Write a test function `test_eat()` in a file `test_pac_game.py` against the following scenario:

- there is a small level with lots of empty space.
- the pac is in the top left corner (0/0)
- the pac is facing right
- the pac moves
- check the new position of the pac, it should now be (1/0) 

Run the test with:

    uv run pytest

Make sure the test works.

## 3. Eating Dots

Write another test against this scenario:

- there is a small level full of dots.
- the pac is in the top left corner
- the pac is facing right
- the pac moves
- it eats a dot and gets a point
- the dot disappears from the map

## 4. Test options

Run the tests with the following command:

  uv run pytest -v -x -s --cov

Explain the options.

## 5. Fixture

Move the creation of the game data for testing into a fixture.

## 6. Conftest

Move the fixture in `test_pac_game.py` to a file `conftest.py`.
Discuss the scope of fixtures (session, module, class, test).

## 7. Mocking

Also compare the code in [mock_example.py](mock_example.py)
Discuss what a **context manager** is.


## Links

- [Test Automation](https://python-basics-tutorial.readthedocs.io/en/latest/test/index.html)
- [Pytest usage guide](https://python-basics-tutorial.readthedocs.io/en/latest/test/pytest/index.html)
- [Pytest library](https://docs.pytest.org)
- [Tutorial by Kristian](https://www.academis.eu/python_testing/)
- [Playwright](https://playwright.dev/python/)
