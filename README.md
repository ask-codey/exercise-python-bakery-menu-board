# Exercise: The Bakery Menu Board

Exercise code for the lesson **Exercise: The Bakery Menu Board** in the Python in Depth course on [ask-codey.com](https://www.ask-codey.com).

Maple Street Bakery wants its menu board printed by a program, so it can go on the screen by the counter. You'll finish `menu.py`, a Python program that prints the board with `print()`, one line per item. Along the way you'll fix a line with a mistake in it, switch a sold-out item off with a comment, and give `print()` a number as well as text. Tests run your program and check every line it prints.

## What's here

- `menu.py`: the menu board program. The comment at the top shows every line it should print when you're done; the comments below it list each problem, and one example shows the format. For you to finish.
- `tests/test_menu.py`: tests that run your program the way `python menu.py` does and read each line it prints. You don't need to change this file.
- `requirements.txt`: the one package the tests need, pytest, at an exact version. Ready to use.
- `pytest.ini`: tells pytest where the tests are. Ready to use.
- `.gitignore`: tells Git to leave out the virtual environment and the files Python and pytest make as they run. Ready to use.

## Before you start

The tests need pytest, and pytest goes in a virtual environment: a private set of packages for this folder only. In VS Code's terminal, in this folder, run these three commands.

On Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

On a Mac (zsh):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

- The first command makes the virtual environment, in a folder named `.venv`.
- The second turns it on for this terminal: the prompt starts with `(.venv)` from then on, and on a Mac plain `python` works too.
- The third installs the packages `requirements.txt` lists into it: here, only pytest.

*Virtual Environments and pip*, in Module 3, explains all three. The `.venv` folder is in `.gitignore`, so Git leaves it out: these commands make it again on any computer.

If PowerShell answers that running scripts is disabled on this system, run this once, then run the second command again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Each new terminal starts with the virtual environment off. If the prompt doesn't start with `(.venv)`, run the second command again. (VS Code often turns it on for you.)

## Run it

```bash
python menu.py
```

The first time, Python prints a traceback that ends with a `SyntaxError`, and nothing else. That's expected: one line has a mistake, and Python can't run the file until it's fixed. Fixing it is problem 5.

## Check your work

```bash
pytest
```

At first every test fails: that is expected. Each problem you solve turns its test green. A failing test's message says the line it expected and the line your program printed, for example *menu.py printed no line 1. It should print: 1) Blueberry muffin: $3.25*. While `menu.py` stops with an error, every test fails with that error: fix it first, and the rest start to pass one by one.

## The rules

- Print each answer on one line: the problem number, `)`, the item's name, `: `, and its price or value. For example: `1) Blueberry muffin: $3.25`.
- Print the lines in the same order as the problems.
- Write prices with a dollar sign and two digits after the point, as the board does: `$6.50`.
- Problem 6: keep the lemon tart's line in the file, as a comment.
- Problem 7: give `print()` the number 14 as a second value, with no quotes.
- Don't change the tests.

## Tips

- Copy the shape of the example. Every line you write is the same pattern with different words.
- When the program stops, read the traceback from its last line up: the last line names the error and says what's wrong, and the `File` line above it gives the line number.
- A hash, `#`, at the start of a line turns it into a comment: Python skips it.
- `print()` prints every value you give it, separated by spaces: `print("Loaves left:", 14)` prints `Loaves left: 14`.
- Run `python menu.py` after every line or two you add, so a mistake is never far from where you're working.

## Hand it in

When it works, push your solution to a public repo of your own on GitHub, then paste that repo's address into **Submit your exercise** on the lesson page at [ask-codey.com](https://www.ask-codey.com). That's what completes the lesson. The lesson page shows the Git commands, step by step.
