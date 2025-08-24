
# Code Checks

## 1. Type Hints

Complete the code in `type_annotations.py` and make sure it works.

*Does the code work even if you enter wrong types?*


## 2. Type Checks

Check the types with:

    uv run mypy type_annotations.py

## 3. Code Linter

Clean the code with:

    uv run black type_annotations.py

## 4. Sort imports

Run `isort` on your `pac` program to sort the imports:

    uv run isort pac/*

## 5. Style Checks

Run `flake8` on your `pac` program to get extra hints:

    uv run flake8 pac/*
