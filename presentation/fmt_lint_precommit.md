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

<!-- pause -->

Here's what we'll accomplish with formatting and linting!

Code before:
```python
def is_weekend(day):
    weekdays = ['Mon','Tue','Wed','Thur','Fri']
    weekends = ['Sat','Sun']

    if day in weekdays
        return False
    else:
        return True
```
<!-- pause -->
Code after:

```python
def is_weekend(day):
    """Return True/False if day is a Weekend."""
    weekdays = [
        "Mon",
        "Tue",
        "Wed",
        "Thur",
        "Fri",
    ]

    return day not in weekdays
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
```python
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
which pip3                #check to make sure venv pip3 is used
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
cat fruits.py #print the contents of fruits.py to the terminal
```

Which should just be these two lines:
```python
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
```python
fruit_counts = {"Pears": 1, "Apples": 4, "Banana": 3}
print("Here are the fruits:", fruit_counts, "and thats it")
```

<!-- pause -->
Look at what it did to the quotes in the `print` statement!

<!-- end_slide -->

What just happened?
---

# Black had the audacity to change our code!
## But I guess it is slightly easier to read now

Try doing the same thing with `long_fruits.py`.
1. `cat long_fruits.py` to see what it looks like
2. `black long_fruits.py` to re-format it
3. `cat long_fruits.py` again to see the final output

<!-- pause -->

## Before:
```python
fruit_counts = {"Pears":1       , "Apples": 4, "Banana":3, "Mango":1, "Grape":17, "Kiwi":1001}
```

<!-- pause -->

## After:
```python
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
## GitHub Stars for Black vs. Ruff

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
  check    Run Ruff on the given files or directories (default)
  rule     Explain a rule (or all rules)
  config   List or describe the available configuration options
  linter   List all supported upstream linters
  clean    Clear any caches in the current directory and any subdirs
  format   Run the Ruff formatter on the given files or directories
  server   Run the language server
  version  Display Ruff version
  help     Print this message or the help of the given subcommand(s)
```

<!-- end_slide -->

`ruff` can format code similarly to `black`
---
TODO


<!-- end_slide -->

`ruff` is also a linter
---

TODO, WHAT IS THE DIFF BETWEEN FMT AND LINT?


<!-- end_slide -->

More on linting
---

TODO, WHAT IS THE DIFF BETWEEN FMT AND LINT?


<!-- end_slide -->

`ruff` is written in rust and is VERY FAST
---

TODO, SPEED OF `ruff`

<!-- end_slide -->

What is pre-commit?
---

WHAT IS pre-commit, and why do I want it?

