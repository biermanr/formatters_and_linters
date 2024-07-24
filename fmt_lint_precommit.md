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

Everything we discuss today will be in relation to python, but other
programming languages have the same or similar tools and concepts.

# Discussion of developer tools
# Introduction to formatters, linters, and pre-commit
# Discuss the appeal of code formatters and linters
# Setup a pre-commit hook to automatically format and lint our code samples!

## You'll need access to a command line. We'll download course materials together.

### I needed to learn quite a bit to prepare for this session and the following links were very helpful
* https://github.com/klieret/everything-you-didnt-now-you-needed
* https://www.slideshare.net/slideshow/embed_code/key/euNhpSgvuPL9kG
* https://github.com/henryiii/sqat-example

(I sometimes *heavily borrowed* from these resources)

These materials were created by **Kilian Lieret** and **Henry Schreiner**
who are Research Software Engineers here at Princeton.

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
