---
title: Linters, Formatters, and Other Tools and Practices for Python
sub_title: PICSciE/RC software engineering summer school 2024
author: July 31st 2024, Rob Bierman, Research Software Engineer
theme:
  override:
    footer:
      style: template
      right: "{current_slide} / {total_slides}"
---

Goals for this session
---


# Discussion of developer tools
<!-- pause -->
# Format some code with `black`!
<!-- pause -->
# Format and lint some code with `ruff`!
<!-- pause -->
# Setup a pre-commit hook to automatically format and lint!
<!-- pause -->

Everything we discuss today will be for python, but other
programming languages have the same or similar tools and concepts.

<!-- end_slide -->

Something to look forward to
---
Here's what we'll accomplish with formatting and linting!

Code before:
```python +line_numbers
def calculate_tip(cost, tip_fraction):
    try:
        tip_percent = float(tip_fraction)
        tip_percent >= 0
    except:
        print('Tip must be between 0 and 1')

    O =  cost*( 1+tip_percent );
    return O
```
<!-- pause -->
Code after:

```python +line_numbers
def calculate_tip(cost, tip_fraction):
    try:
        tip_percent = float(tip_fraction)
        assert tip_percent >= 0
    except ValueError:
        raise ValueError("Tip must be between 0 and 1")

    total = cost * (1 + tip_percent)
    return total
```

<!-- end_slide -->

Following along and acknowledgements
---

# If you want to follow along (it will be fun) you'll need access to a terminal with `python` and `git` installed and the ability to `pip install` packages.

<!-- pause -->

## I learned quite a bit to prepare for this session and the following links were very helpful
* https://github.com/klieret/everything-you-didnt-now-you-needed
* https://www.slideshare.net/slideshow/embed_code/key/euNhpSgvuPL9kG
* https://github.com/henryiii/sqat-example

(I *heavily borrowed* from these resources)

These materials were created by **Kilian Lieret** and **Henry Schreiner**
who are excellent Research Software Engineers (RSEs) here at Princeton.
*https://researchcomputing.princeton.edu/services/research-software-engineering*

<!-- end_slide -->

Development tool tradeoffs
---

# Development tools solve problems for developers
* Integrated Development Environments (IDEs)
    * Edit and view multiple files
<!-- new_line -->
<!-- pause -->

* git/github
    * Rolling-back changes and collaborating with others
<!-- new_line -->
<!-- pause -->

* **Formatting and Linting**
    * Standardize code style and enforce best practices
<!-- new_line -->
<!-- pause -->
* **Pre-commit hooks**
    * Small checks before code is committed

<!-- new_line -->
<!-- pause -->
# Development tools add overhead to a project
<!-- incremental_lists: true -->
* "New contributors welcome!"
    * Just setup the dev environment...
    * Make sure the tests pass...
    * Add new tests for the code you've added...
    * Make sure you're using our coding style...

<!-- pause -->
This can be a burden for a small and simple code change.

<!-- end_slide -->

Different types of dev tool learning experiences
---
```
      Good
 
   ┃
W  ┃   ╭──╮
o  ┃───╯  │
r  ┃      │
k  ┃      ╰───
   ┗━━━━━━━━━━
       Time
```


<!-- pause -->
```
       Painful
        ╭──╮
    ┃   │  │
    ┃   │  │
    ┃───╯  │
    ┃      │
    ┃      ╰───
    ┗━━━━━━━━━━
        Time
```
<!-- pause -->

```
          Bad
       ╭───────╮
   ┃   │       │
   ┃   │       │
   ┃───╯       │
   ┃           ╰───
   ┃ 
   ┗━━━━━━━━━━━━━━━
       Time
```

<!-- pause -->

**By the end of this session, hopefully you'll agree that
formatting and linting with pre-commit hooks provide enough
value to outweigh the added "cruft"**

<!-- end_slide -->

Formatters alter the format, but not the function of code
---

This code works, but isn't formatted very nicely:
```python +line_numbers
fruit_counts = {"Pears":1       , "Apples": 4, "Banana":3}
print("Here are the fruits:",fruit_counts,'and thats it')
```

<!-- pause -->

We could manually make the changes, OR we could use a formatter!

Let's use the `black` formatter
![](images/black_logo.png)

## ***"The Uncompromising Code Formatter"***

<!-- end_slide -->

Fetching course materials and installing black
---

# First fetch the class materials using `git clone`
```bash
git clone https://github.com/biermanr/formatters_and_linters
```

then `cd` into the directory and `ls` to see the files
```shell
cd formatters_and_linters
ls
```

<!-- pause -->

# Installing black

It would be better to use `pipx` to install/run `black`, but let's install
it using `pip` for today in a venv.

```shell
which python3             #make sure python3 is available
python3 -m venv .venv     #create a venv virtual environment
source .venv/bin/activate #activate the environment
which pip3                #make sure venv pip3 is used
pip3 install black        #finally install black
```

We'll pause here to for anyone who wants to follow along

If you have a successful `black` installation, you should be
able to run `black --help` on the command line and get the help message.

<!-- end_slide -->

Using black to reformat our fruits
---

When you `git cloned` the class materials you downloaded `fruits.py`
as well as other files that we'll use later!

```bash
cat fruits.py #print the file contents to terminal
```

Which should just be these two lines:
```python +line_numbers
fruit_counts = {"Pears":1       , "Apples": 4, "Banana":3}
print("Here are the fruits:",fruit_counts,'and thats it')
```
<!-- pause -->

Now that we have `black` installed we can simply run:
```bash
black fruits.py
```

<!-- pause -->
```
reformatted fruits.py
All done! ✨ 🍰 ✨
1 file reformatted.
```
<!-- pause -->

If you `cat` the file again, you should see it has done the formatting for us!
```python +line_numbers
fruit_counts = {"Pears": 1, "Apples": 4, "Banana": 3}
print("Here are the fruits:", fruit_counts, "and thats it")
```

<!-- pause -->
Look at what it did to the quotes in the `print` statement!

<!-- end_slide -->

What just happened?
---

# Black had the audacity to change our code!

Try doing the same thing with `long_fruits.py`.
1. `cat long_fruits.py` to see what it looks like
2. `black long_fruits.py` to re-format it
3. `cat long_fruits.py` again to see the final output

<!-- pause -->

## Before:
```python +line_numbers
fruit_counts = {"Pears":1       , "Apples": 4, "Banana":3, "Mango":1, "Grape":17, "Kiwi":1001}
```

<!-- pause -->

## After:
```python +line_numbers
fruit_counts = {
    "Pears": 1,
    "Apples": 4,
    "Banana": 3,
    "Mango": 1,
    "Grape": 17,
    "Kiwi": 1001,
}
```

## What are your opinions with the "extra" comma after `kiwi`? Love? Hate?
## How about the "long" vs. "wide" dictionary?

<!-- pause -->

How is `black` doing this? How does it know what "well-formatted" code looks like?


<!-- end_slide -->

Formatting rules
---

# How is black working and how can it be configured?

<!-- pause -->

Turns out that `black` is pretty opinionated

> Black aims for consistency, generality, readability
> and reducing git diffs. Similar language constructs
> are formatted with similar rules. Style configuration
> options are deliberately limited and rarely added.

<!-- pause -->
"Don't try and tell `black` what to do"

You can read about the `black` formatting style:
https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html

<!-- pause -->
Which includes statements like:


> Pro-tip: If you’re asking yourself “Do I need to configure anything?”
> the answer is “No”. Black is all about sensible defaults.
> Applying those defaults will have your code in compliance with many
> other Black formatted projects.

<!-- pause -->
## I'm trying not to be offended. Let's look at the main other tool, `ruff`!

<!-- end_slide -->

`ruff` is the hip new alternative to `black`
---
# Ruff is new to the game, but gained immediate wide-spread appeal
## GitHub Stars for Black vs. Ruff over time

| Date | Black | Ruff |
| ------ | ------ | ------ |
| Mar 2018 | 0 | N/A |
| Aug 2022 | 27,870 | 0 |
| Feb 2023 | 30,390 | 7,800 |
| Sep 2023 | 32,940 | 17,610 |
| Jan 2024 | 35,460 | 21,510 |
| Jul 2024 | 38,061 | 29,417 |


<!-- pause -->
Let's install `ruff` and try it out ourselves!
```bash
which pip3        #make sure we're still using the venv
pip3 install ruff #install ruff
ruff help         #get the ruff help message
```

<!-- pause -->

# Ruff has multiple commands to choose from

```bash {all|2}
(.venv) $ ruff help
Ruff: An extremely fast Python linter and code formatter.

Usage: ruff [OPTIONS] <COMMAND>

Commands:
  check    Run Ruff on the given files or directories
  ...
  linter   List all supported upstream linters
  clean    Clear any caches in the current directory
  format   Run the Ruff formatter on the given files/dirs
  ...
  help     Print this message or the help of a subcommand(s)
```

<!-- end_slide -->

`ruff` can format code similarly to `black`
---
Let's format the starting example tip-calculator code

Take a look with `cat tip.py`
```python +line_numbers
def calculate_tip(cost, tip_fraction):
    try:
        tip_percent = float(tip_fraction)
        tip_percent >= 0
    except:
        print("The tip must be a number between 0 and 1")

    O =  cost*( 1+tip_percent );
    return O
```

<!-- pause -->
Format with `ruff` using
```bash
$ ruff format tip.py
  1 file reformatted
```

<!-- pause -->
Running `cat` again:
```python +line_numbers {all|6,8}
def calculate_tip(cost, tip_fraction):
    try:
        tip_percent = float(tip_fraction)
        tip_percent >= 0
    except:
        print('The tip must be a number between 0 and 1')

    O = cost * (1 + tip_percent)
    return O
```

<!-- end_slide -->

`ruff` is also a linter
---

It was great that we improved the formatting of the tip.py code, but there
are non-formatting issues with the code.

```python +line_numbers
def calculate_tip(cost, tip_fraction):
    try:
        tip_percent = float(tip_fraction)
        tip_percent >= 0
    except:
        print('The tip must be a number between 0 and 1')

    O = cost * (1 + tip_percent)
    return O
```

<!-- pause -->
The main issues I see is the `tip_percent >= 0` isn't actually doing anything.
## This check is failing silently!

<!-- pause -->
We're going to move into **linting**!

<!-- pause -->
The line between **formatting** and **linting** can be a little blury
* Formatting is concerned with how the code looks
* Linting is concerned with "best practices" and identifying potential bugs
<!-- end_slide -->

Linting tip.py
---

```python +line_numbers
def calculate_tip(cost, tip_fraction):
    try:
        tip_percent = float(tip_fraction)
        tip_percent >= 0
    except:
        print('The tip must be a number between 0 and 1')

    O = cost * (1 + tip_percent)
    return O
```

Run `ruff check tip.py`

We get a lot of output, let's just start with the first complaint:
```bash
tip.py.hold:4:9: B015 Pointless comparison. 
Did you mean to assign a value? 
Otherwise, prepend `assert` or remove it.
  |
2 |     try:
3 |         tip_percent = float(tip_fraction)
4 |         tip_percent >= 0
  |         ^^^^^^^^^^^^^^^^ B015
5 |     except:
6 |         print('The tip must be a number between 0 and 1')
  |
```

<!-- pause -->
### Ahah! `ruff check` found the bug I complained about before (what a coincidence!)

<!-- end_slide -->

What does `B015` mean?
---

```bash
tip.py.hold:4:9: B015 Pointless comparison. 
Did you mean to assign a value? 
Otherwise, prepend `assert` or remove it.
  |
2 |     try:
3 |         tip_percent = float(tip_fraction)
4 |         tip_percent >= 0
  |         ^^^^^^^^^^^^^^^^ B015
5 |     except:
6 |         print('The tip must be between 0 and 1')
```

`B015` is a Linting Rule!

We can ask `ruff` to explain this rule to us with `ruff rule B015`

```bash
# useless-comparison (B015)

Derived from the **flake8-bugbear** linter.

## What it does
Checks for useless comparisons.

## Why is this bad?
Useless comparisons have no effect on the program, 
and are often included by mistake. If the comparison 
is intended to enforce an invariant, prepend the 
comparison with an `assert`. Otherwise, remove it entirely.

## Example
foo == bar

Use instead:
assert foo == bar, "`foo` and `bar` should be equal."
```

<!-- end_slide -->

Fixing the comparison linting error
---
I'm going to use `vim` to make the suggested change to `tip.py`,
of course feel free to use any text editor, even `emacs` I guess.

```python +line_numbers {4}
def calculate_tip(cost, tip_fraction):
    try:
        tip_percent = float(tip_fraction)
        assert tip_percent >= 0
    except:
        print('The tip must be a number between 0 and 1')

    O = cost * (1 + tip_percent)
    return O
```

Now when you run the same `ruff check tip.py` you'll see its no longer
upset about `B015`, but there are a few remaining issues.

```bash
tip.py.hold:5:5: E722 Do not use bare `except`
  |
3 |         tip_percent = float(tip_fraction)
4 |         assert tip_percent >= 0
5 |     except:
  |     ^^^^^^ E722
6 |         print('The tip must be between 0 and 1')
  |

tip.py.hold:8:5: E741 Ambiguous variable name: `O`
  |
6 |         print('The tip must be between 0 and 1')
7 | 
8 |     O = cost * (1 + tip_percent)
  |     ^ E741
9 |     return O
  |
```

Take a look at `ruff rule E741`

<!-- end_slide -->

Final form of tip.py to make `ruff` happy
---

```python
def calculate_tip(cost, tip_fraction):
    try:
        tip_percent = float(tip_fraction)
        assert tip_percent >= 0
    except ValueError:
        print('The tip must be between 0 and 1')

    total = cost * (1 + tip_percent)
    return total


print(calculate_tip(100, 0.18))
```
<!-- pause -->
and now when we run `ruff check tip.py` we see
```bash
All checks passed!
```

<!-- end_slide -->

Where do these Linting Rules come from?
---

Linting rules come from a few different places!

`ruff linting` shows the full list of linting rules that ruff knows

```bash
   F Pyflakes
 E/W pycodestyle
 C90 mccabe
   I isort
   N pep8-naming
   D pydocstyle
   ...
FURB refurb
 DOC pydoclint
 RUF Ruff-specific rules
```

<!-- pause -->
## Unlike `black` we are encouraged to choose which lints to include!

This is controlled either in a `ruff.toml` or a `pyproject.toml` if you
are writing a python package. Let's just use `ruff.toml` for today.

Take a look at the `ruff.toml` in the course materials

```toml
[lint]
# Remember `B015`? It's in the `B` suite of lints.
select = ["E4", "E7", "E9", "F", "B"]

[format]
quote-style = "single"
```
<!-- pause -->
Adding the "D" `pydoclint` suite of and
linting again with `ruff check tip.py`:

<!-- pause -->
```bash
tip.py.hold:1:1: D100 Missing docstring in public module
tip.py.hold:1:5: D103 Missing docstring in public function
Found 2 errors.
```

<!-- end_slide -->

`ruff` is written in rust and is VERY FAST
---

Here's how long various linters take to lint the `CPython` codebase

| Tool | Time(s) |
| ------ | ------ |
| Ruff | 00.29 |
| Autoflake | 06.18 |
| Flake8 | 12.26 |
| Pyflakes | 15.97 |
| Pycodestyle | 46.92 |
| Pylint | 60.00+ |

<!-- pause -->
`CPython` has 600,000 lines of python code (citation needed)

If you're like me and writing < 10,000 lines of code then lint speed might not
be your biggest concern. But `ruff` is user-friendly, so free speed!
<!-- pause -->
Also people praise `ruff` for consolidating functionality from many tools.

<!-- end_slide -->

What is pre-commit and why should I be excited?
---

Oh boy, another developer tool someone is telling me that I should learn...

```
       ╭───────╮
W  ┃   │       │
o  ┃   │       │
r  ┃───╯       │
k  ┃           ╰───
   ┃ 
   ┗━━━━━━━━━━━━━━━
       Time
```
<!-- pause -->
`pre-commit` makes it easy to run code quality checks (like `ruff`!) before
you commit your code. 

<!-- pause -->
It would be both annoying and error prone to have to remember to run `ruff check *.py`
every single time we change our code and make a git commit.

<!-- pause -->
In order to follow along, you need to have `git`, so try `git status`

It will list files that you've changed since running `git clone`

```bash

On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	deleted:    days.py
	modified:   presentation/fmt_lint_precommit.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	ruff.toml
	tip.py

no changes added to commit (use "git add" and/or "git commit -a")
```



