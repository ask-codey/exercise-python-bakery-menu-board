# Tests for menu.py. Run them with: pytest (in the exercise folder, with the virtual environment on).
# They run menu.py the way `python menu.py` does, then read each line it prints, such as
# "1) Blueberry muffin: $3.25". A failing test says the line it expected and the line
# menu.py printed, or the error that stopped menu.py.
# You don't need to change this file.
import os
import re
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parent.parent / "menu.py"


def typing(typed):
    """How a test's message starts: "Typing 'Maya', '3', '2', receipt.py", or just "menu.py" for a script that
    asks nothing, so the tests type nothing."""
    if not typed:
        return SCRIPT.name
    return "Typing " + ", ".join(repr(answer) for answer in typed) + ", " + SCRIPT.name


def run_script(*typed):
    """Runs the script with this Python, types each answer in typed followed by Enter, and returns what happened.
    A run still going after 10 seconds is stopped: a while loop that never ends is the usual reason."""
    __tracebackhide__ = True
    try:
        return subprocess.run(
            [sys.executable, str(SCRIPT)],
            input="".join(answer + "\n" for answer in typed),
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=10,
            env={**os.environ, "PYTHONUTF8": "1"},  # the same text on every computer
        )
    except subprocess.TimeoutExpired:
        pass  # failed below, outside this except, so pytest shows only the message
    pytest.fail(
        f"{typing(typed)} was still running after 10 seconds, so the test stopped it. Look for a while loop that "
        "never ends: does the loop change, or ask again for, the value its condition checks?",
        pytrace=False,
    )


def printed_lines(result):
    """Each line the script printed that has a line number and ")", by that number:
    "1) name: Maya" -> {"1": "1) name: Maya"}.
    When the tests type the answers, nothing ends the question's line, so a numbered line can come right after a
    question, as in "How many sodas? 1) name: Maya". The number is found there too."""
    lines = {}
    for line in result.stdout.splitlines():
        match = re.search(r"(?:^|\s)(\w+)\)", line)
        if match:
            lines[match.group(1)] = line[match.start(1):].strip()
    return lines


def expect(condition, message):
    """Fails with just the message when the condition isn't true."""
    __tracebackhide__ = True  # pytest shows the message, not this helper's code
    if not condition:
        pytest.fail(message, pytrace=False)


def program_runs(result, typed=()):
    """Fails, with the end of Python's traceback, when the script stopped with an error."""
    __tracebackhide__ = True
    traceback_end = "\n".join([line for line in result.stderr.splitlines() if line.strip()][-4:])
    same_answers = ", type the same answers," if typed else ""
    expect(
        result.returncode == 0,
        f"{typing(typed)} stopped with an error. Run python {SCRIPT.name} in the terminal{same_answers} and read "
        "the traceback from its last line up:\n" + traceback_end,
    )


def check(typed, number, expected):
    """Fails unless the script, given these answers, ran to the end and printed exactly the line expected."""
    __tracebackhide__ = True
    result = run_script(*typed)
    program_runs(result, typed)
    lines = printed_lines(result)
    expect(number in lines, f"{typing(typed)} printed no line {number}. It should print: {expected}")
    got = lines[number]
    expect(got == expected, f"{typing(typed)} should print the line: {expected}\nbut it printed: {got}")


NOTHING_TYPED = []  # menu.py asks no questions, so the tests type nothing


def source():
    return SCRIPT.read_text(encoding="utf-8")


def test_1_prints_blueberry_muffin_3_25():
    check(NOTHING_TYPED, "1", "1) Blueberry muffin: $3.25")


def test_2_prints_cranberry_scone_3_50():
    check(NOTHING_TYPED, "2", "2) Cranberry scone: $3.50")


def test_3_prints_sourdough_loaf_6_50():
    check(NOTHING_TYPED, "3", "3) Sourdough loaf: $6.50")


def test_4_prints_cinnamon_roll_3_75():
    check(NOTHING_TYPED, "4", "4) Cinnamon roll: $3.75")


def test_5_the_line_with_a_mistake_is_fixed_and_prints_bread_of_the_day_rye():
    check(NOTHING_TYPED, "5", "5) Bread of the day: Rye")


def test_6_the_sold_out_lemon_tart_does_not_print_and_stays_in_the_file_as_a_comment():
    result = run_script()
    program_runs(result)
    expect(
        "6" not in printed_lines(result),
        "Problem 6: the lemon tart sold out, so its line should not print. Turn it into a comment.",
    )
    expect(
        re.search(r"^\s*#.*Lemon tart", source(), re.MULTILINE),
        "Problem 6: keep the lemon tart's line in the file, as a comment, for tomorrow.",
    )


def test_7_prints_loaves_left_14_with_14_given_to_print_as_a_number():
    check(NOTHING_TYPED, "7", "7) Loaves left: 14")
    expect(
        re.search(r"""print\(\s*["']7\) Loaves left:["']\s*,\s*14\s*\)""", source()),
        "Problem 7: give print() two values, the text in quotes, a comma, then the number 14 with no quotes.",
    )


def test_8_prints_open_7_am_to_2_pm():
    check(NOTHING_TYPED, "8", "8) Open: 7 AM to 2 PM")


def test_9_the_lines_print_in_order_i_1_to_5_then_7_and_8():
    result = run_script()
    program_runs(result)
    order = ["i", "1", "2", "3", "4", "5", "7", "8"]
    numbers = [number for number in printed_lines(result) if number in order]
    expect(
        numbers == order,
        "Print every line of the board in the order of the problems in menu.py: "
        f"{', '.join(order)}. Printed so far: {', '.join(numbers) or 'nothing'}.",
    )
