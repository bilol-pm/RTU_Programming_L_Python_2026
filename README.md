# RTU_Programming_Languages_Python_Fall_2026
Python portion of Programming Languages Course at RTU Fall 2026

## 🐍 Python Programming – 5-Week Continuation Course (Revised)

This 5-week course introduces Python to students who have completed the C Programming course and already know C++ and/or Java.  
It emphasizes *translating structured C-style programming into idiomatic Python* and prepares students for data-oriented and scripting tasks.  
Each week includes one **lecture (2×45 min)** and one **lab (2×45 min)**.

## 🧑‍🎓 Student Instructions

1. **Fork** this repository to your own GitHub account.  
2. **Open in GitHub Codespaces** (use “Code → Open with Codespaces”) on **your fork**.  
3. Check your setup by running `python src/week1/hello.py` in the terminal.  
4. Navigate to `src/week1/` (and other weeks later on).  
5. Complete each task file (`python_lab1_task1.py` … `python_lab1_task4.py`) by replacing the TODOs and the `raise NotImplementedError(...)` lines.  
   - Read the docstring at the top of each file carefully: it states exactly what each function must **return**, with examples.  
   - Keep all `input()` and `print()` calls inside the `if __name__ == "__main__":` block. The autograder imports your functions, and an `input()` outside that block makes it hang.  
   - Do not rename the files or the functions.  
6. Run a task interactively: `python src/week1/python_lab1_task1.py`  
7. **Check your own work before submitting.** Your code is checked by the instructor after the deadline, and nothing runs automatically when you push. Run the docstring examples yourself:  
   `python -m doctest -v src/week1/python_lab1_task1.py`  
   If every example passes, you are on the right track. The final check also uses additional test cases.  
8. **Commit and push** your completed work, then open your fork on github.com and confirm your changes are there.  
9. Submit **only the URL of your fork** in the Moodle (ORTUS on RTU) text field, in exactly this form:  
   `https://github.com/<your-username>/<repository-name>`  
   - It must contain **your** GitHub username, not the course's.  
   - Do not link to a single file or folder (no `/tree/...` or `/blob/...`), and do not add `.git` at the end.  
   - Keep your fork **public** and do not rename or delete it. Work pushed after the deadline is not checked.

> **Feedback:** results and comments for each task will appear in Moodle after the lab has been checked. This lab is for practice and does not count toward your final grade.

> **Keeping your fork up to date:** new weeks will be added in new folders (`src/week2/`, …). Use **“Sync fork”** on your fork's GitHub page to get them. Only edit your own task files so syncing does not cause conflicts.

---

## 📅 Weekly Overview

| **Week** | **Topic** | **Focus Keywords** |
|-----------|------------|--------------------|
| **1** | Python Basics, Branching & Iteration | syntax, variables, input/output, `if`, `for`, `while`, basic functions |
| **2** | Functions, Strings & Iteration Patterns | parameters, return values, scope, string operations, slicing |
| **3** | Core Data Structures & Functional Tools | lists, tuples, sets, dicts, comprehensions, `map`, `filter`, `zip`, `apply` |
| **4** | File I/O, Modules & Exceptions | reading/writing files, modularity, error handling |
| **5** | Object-Oriented Python & Project Integration | classes, testing, integration with C parser project |

---

## Week 1 – Python Basics, Branching & Iteration

**Lecture**
- Python syntax vs C syntax: indentation, comments, dynamic typing  
- Variables, literals, and basic data types (`int`, `float`, `bool`, `str`)  
- Input/output using `input()` and formatted `print()` (f-strings)  
- Arithmetic and comparison operators  
- Conditional statements (`if`, `elif`, `else`)  
- Loops: `for` and `while` (no nested data structures yet)  
- Basic function definition and calling (`def`, `return`)  

**Lab** (`src/week1/`)
- Task 1: write a function with arithmetic using the `math` module (`circle_area`)  
- Task 2: clean up and format user input with string methods (`greet_user`)  
- Task 3: combine `len()`, `split()` and a case-insensitive check, returning a tuple (`analyze_sentence`)  
- Task 4: build a text-based arithmetic analyzer from small helper functions (`analyze_text`)  
- Practice `input()`, f-string formatting, simple `if` branching and loops along the way  

---

## Week 2 – Functions, Strings & Iteration Patterns

**Lecture**
- Function parameters, return values, and default arguments  
- Local vs global variables; scoping rules  
- String basics and operations: concatenation, repetition, indexing, slicing  
- String methods: `split()`, `join()`, `strip()`, `replace()`, `find()`  
- Iterating through strings and sequences (`for char in string`)  
- Reusable code style: docstrings and comments  

**Lab**
- Extend the Week 1 text analyzer with default arguments and new string methods (`join()`, `replace()`, `find()`)  
- Explore string slicing and iteration patterns  
- Practice writing functions that transform and return text results  

---

## Week 3 – Core Data Structures & Functional Tools

**Lecture**
- Lists, tuples, sets, and dictionaries: creation, indexing, iteration  
- Mutability and immutability concepts  
- List methods and slicing  
- Dictionary key–value operations and nested structures  
- Set operations: union, intersection, difference  
- Comprehensions (`list`, `dict`, `set`)  
- Functional programming tools: `map()`, `filter()`, `zip()`, `apply()` (from Pandas preview)  
- When to use loops vs comprehensions vs functional style  

**Lab**
- Build simple datasets (lists/dicts) and compute aggregates  
- Practice comprehensions and transformations  
- Implement frequency counter for arithmetic operators and operands  
- Experiment with `map()` and `filter()` to process lists  

---

## Week 4 – File I/O, Modules & Exceptions

**Lecture**
- Reading/writing text files with `open()` and `with`  
- Basic CSV and JSON handling  
- Organizing code into modules; `import`, `from`, `as`  
- Exception handling: `try`, `except`, `finally`  
- Reusing modular design concepts from C  

**Lab**
- Read/write structured data from files  
- Create helper module `arithutils.py`  
- Handle division-by-zero and invalid inputs gracefully  
- Log program output to file  

---

## Week 5 – Object-Oriented Python & Project Integration

**Lecture**
- Classes and objects; defining `__init__` and instance methods  
- Encapsulation and inheritance basics  
- Magic methods (`__str__`, `__repr__`)  
- Unit testing with `unittest` and `pytest`  
- Integrating C and Python components conceptually (data types, APIs)  

**Lab**
- Implement `Expression` class with evaluation method  
- Write and run unit tests  
- Package project as a module with documentation  
- Bonus: visualize expression tree recursively  

---

## 🧩 Course Outcomes

By the end of the course, students will be able to:

- Write readable, modular Python code using branching, iteration, and functions  
- Work fluently with strings, lists, tuples, sets, and dictionaries  
- Employ comprehensions and functional programming tools for data transformation  
- Handle files and exceptions safely  
- Organize code into reusable modules and classes  
- Integrate and test Python programs effectively  
- Transition smoothly from C-style logic to expressive, idiomatic Python  

