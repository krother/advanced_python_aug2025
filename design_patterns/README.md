
# Design Patterns

**A design pattern is a solution to a recurring problem.**

## Origin

The term **Design Pattern** appeared in the book *"The Timeless Way of Building"* by Christopher Alexander. It is a book about architecture from 1979.

The term was adopted by the **Gang of Four** (Gamma, Helm, Johnson and Vlissides) who described 23 software design patterns in the book **Design Patterns** in 1994. Many people referring to patterns today, refer to this catalog of patterns, although most of them do appear in a very different form today.

Here we will cover some examples. See [sourcemaking.com/design_patterns](https://sourcemaking.com/design_patterns) for a longer list.

## The Strategy Pattern

The Strategy Pattern makes an algorithmic component interchangeable.
We can use the pattern to implement **ghost movement**.

1. Write a generator function `random_moves()` that produces an endless sequence of random directions using `yield`. Use the code in [ghost_move.py](ghost_move.py) work. (**The lines are complete and correct, but the order is wrong and indentation is missing.**)
2. Integrate the code into your game.
3. Add another move generator that moves 5 times left, then 5 times right and then repeats.
4. Add a `Callable` attribute to the `Ghost` class and assign one or the other function to it.
5. Draw ghosts in the `draw()` function.
6. Create two different ghosts.

## The Factory Pattern

Isolate how tile graphics are loaded and looked up. We will use the [FactoryMethod](https://sourcemaking.com/design_patterns/factory_method):

- create a new module `tiles.py`
- create a new class `TileFactory` that takes an file name as an initialization parameter.
- move `read_images`, `TILE_SIZE` and the tile dictionary to the new module
- call `read_images` in the constructor `__init__`
- add a method `get_tile()` that returns a tile image.
- create a `TileFactory` object in the main program.
- call `get_tile()` in the `draw()` function.

    class TileFactory:

        def __init__(self, filename: str):
            ...

        def __getitem__(self, name: str) -> np.ndarray:
            ...

Having the factory opens up more flexible options like adding synonyms for the tiles
or reading the tile definitions from a file.

## The Repository Pattern

Add a save/load functionality to the game by implementing the Repository Pattern.
The purpose of the pattern is to isolate data persistence, so that the rest of the program does not have to know whether we are using a database or a JSON file.

- create a new module for the repository
- create a `Repository` class
- create two methods `load` and `save` (could be many more specific methods in a bigger repo, e.g. search)
- only one saved game should exist at any given time
- none of the code outside the repository should know what is used to store the game
- call the load/save functions from within the main program if the "l" or "s" keys are pressed.

Consider the following signature:

    class Repository:

        def __init__(self):
            ...

        def save(self, game: PacGame) -> None:
            ...

        def load(self) -> DungeonGame:
            ...

To implement the Repository, pick one of the following libraries:

- [json](https://github.com/krother/Python3_Package_Examples/blob/master/json/example_json.py)
- [pickle](https://python-basics-tutorial.readthedocs.io/en/latest/save-data/pickle.html)


## The Facade Pattern

The Facade Pattern uses a single class as a contact point with a program component.
It hides the implementation details away.

- separate the graphics and game logic into separate modules.
- look where the classes `Pac`, `Ghost`, `Level` and `Vector` are used in the graphics or tests.
- decide which of these should be public.
- for everything you do not want to be public, create a method in `PacGame` that gives access to the required functionality.
- check whether the tests need to be adjusted.
