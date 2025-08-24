
# Build a Python Package

In this exercise, you will use  `uv <https://docs.astral.sh/uv/>`__ to create a package structure for the game `pac` application.
**uv** is a modern tool for managing virtual environments written in rust. It works similar to **pipenv** and **poetry** but is 100x faster when resolving dependencies.

## 1. Installation

Install uv with:

    python -m pip install uv

or

    curl -LsSf https://astral.sh/uv/install.sh | sh


## 2. Create environment

Create a project folder and execute the commands

    uv python install 3.12
    uv init

Check what files have been created.

## 3. pyproject.toml

The file [pyproject.toml](pyproject.toml) creates everything to package the project.
Inspect the file and clarify its contents.

## 4. Install libraries

Install the dependencies listed in `pyproject.toml`:

    uv lock
    uv sync

The development libraries are installed by default.

## 5. Add source code

Add a folder `pac/` below the folder containing `pyproject.toml`
Download and add the following two files:

* [pac_game.py](pac_game.py)
* [tiles.png](tiles.png)

## 6. Execute code

Now the program is ready to be executed:

    uv run python pac/pac_game.py

Also using the `[project.scripts]` configuration:

    uv run pac

## 7. Release the package

Create a distribution with:

    uv build

You should find the release files in the `dist/` folder.

If you want to release the sources only, use:

    uv build --sdist

## 7. Install the package

The newly created package can be installed with ``pip`` from the release wheel:

    pip install dist/pac-1.1.0-py3-none-any.whl

and

    python
    
    >>> import pac
