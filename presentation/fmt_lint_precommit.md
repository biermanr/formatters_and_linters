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
# Introduction to formatters, linters, and pre-commit
<!-- pause -->
# Discuss the appeal of code formatters and linters
<!-- pause -->
# Format some code!
<!-- pause -->
# Lint some code!
<!-- pause -->
# Setup a pre-commit hook to automatically format and lint our code samples!
<!-- pause -->

Everything we discuss today will be in relation to python, but other
programming languages have the same or similar tools and concepts.

<!-- end_slide -->

Following along and acknowledgements
---

# If you want to follow along, and I think you should, you'll need access to a command line with python installed and the ability to `pip install` packages.

<!-- pause -->

## I needed to learn quite a bit to prepare for this session and the following links were very helpful
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


<!-- end_slide -->

Different types of dev tool learning experiences
---
```
      Good             Painful             Bad
                        ╭──╮            ╭───────╮    
   ┃                ┃   │  │        ┃   │       │    
W  ┃   ╭──╮      W  ┃   │  │     W  ┃   │       │    
o  ┃───╯  │      o  ┃───╯  │     o  ┃───╯       │    
r  ┃      │      r  ┃      │     r  ┃           ╰───     
k  ┃      ╰───   k  ┃      ╰───  k  ┃                
   ┗━━━━━━━━━━      ┗━━━━━━━━━━     ┗━━━━━━━━━━━━━━━
       Time             Time            Time    
```
<!-- pause -->

**By the end of this session, hopefully you'll agree that 
formatting and linting with pre-commit hooks provide enough
value to outweigh any added "cruft"**

<!-- end_slide -->

Formatters alter the format, but not the function of code
---

This code works, but isn't formatted nicely:
```python
fruit_counts = {"Pears":1       , "Apples": 4, "Banana":3}
print(fruit_counts)
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
```shell
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

We'll pause here to make sure anyone who wants to follow along can

If you have a successful `black` installation, you should be
able to run `black --help` on the command line and get the help message.

<!-- end_slide -->

Using black to reformat our fruits
---

When you `git cloned` the class materials you downloaded `fruits.py`
```python
fruit_counts = {"Pears":1       , "Apples": 4, "Banana":3}
print(fruit_counts)
```
<!-- pause -->

