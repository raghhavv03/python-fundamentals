# Python Fundamentals

[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A structured, hands-on repository covering core Python programming fundamentals. This collection documents a systematic learning pathway from basic syntax and control flow to object-oriented programming, data structures, and file I/O operations.

---

## 📚 Curriculum Breakdown

The repository is organized into 5 progressive modules:

| Module | Core Concepts & Topics | Lessons | Assignments & Notes |
| :--- | :--- | :--- | :--- |
| **Part 1: Basics & Operations** | Variables, primitive data types, arithmetic/logical operators, type casting, basic user I/O | [`01_part_1.py`](file:///Users/raghhavv03/Workspace/Learning/python-fundamentals/lessons/01_part_1.py) | [Notes](file:///Users/raghhavv03/Workspace/Learning/python-fundamentals/notes/01_part_1_notes.pdf) \| [Assignment](file:///Users/raghhavv03/Workspace/Learning/python-fundamentals/assignments/01_part_1_assignment.pdf) \| [Solution](file:///Users/raghhavv03/Workspace/Learning/python-fundamentals/assignments/02_part_1_assignment_solution.py) |
| **Part 2: Control Flow & Functions** | `if-elif-else`, `match-case`, `while`/`for` loops, break/continue, functions, lambda expressions, recursion | [`02_part_2.py`](file:///Users/raghhavv03/Workspace/Learning/python-fundamentals/lessons/02_part_2.py) | [Notes](file:///Users/raghhavv03/Workspace/Learning/python-fundamentals/notes/02_part_2_notes.pdf) \| [Assignment](file:///Users/raghhavv03/Workspace/Learning/python-fundamentals/assignments/03_part_2_assignment.pdf) \| [Solution](file:///Users/raghhavv03/Workspace/Learning/python-fundamentals/assignments/04_part_2_assignment_solution.py) |
| **Part 3: Data Structures** | Strings, lists, tuples, dictionaries, sets, indexing/slicing, format methods, comprehensions | [`03_part_3.py`](file:///Users/raghhavv03/Workspace/Learning/python-fundamentals/lessons/03_part_3.py) | [Notes](file:///Users/raghhavv03/Workspace/Learning/python-fundamentals/notes/03_part_3_notes.pdf) \| [Assignment](file:///Users/raghhavv03/Workspace/Learning/python-fundamentals/assignments/05_part_3_assignment.pdf) \| [Solution](file:///Users/raghhavv03/Workspace/Learning/python-fundamentals/assignments/06_part_3_assignment_solution.py) |
| **Part 4: Object-Oriented Programming** | Classes, constructors (`__init__`), instance vs class attributes, OOP pillars (Encapsulation, Inheritance, Abstraction, Polymorphism), duck typing | [`04_part_4.py`](file:///Users/raghhavv03/Workspace/Learning/python-fundamentals/lessons/04_part_4.py) | [Notes](file:///Users/raghhavv03/Workspace/Learning/python-fundamentals/notes/04_part_4_notes.pdf) \| [Assignment](file:///Users/raghhavv03/Workspace/Learning/python-fundamentals/assignments/07_part_4_assignment.pdf) \| [Solution](file:///Users/raghhavv03/Workspace/Learning/python-fundamentals/assignments/08_part_4_assignment_solution.py) |
| **Part 5: File I/O & Advanced Topics** | File handling (`open`/`with`), JSON serialization (`json`), Exception handling (`try`/`except`/`finally`), List comprehensions | [`05_part_5.py`](file:///Users/raghhavv03/Workspace/Learning/python-fundamentals/lessons/05_part_5.py) | [Notes](file:///Users/raghhavv03/Workspace/Learning/python-fundamentals/notes/05_part_5_notes.pdf) \| [Assignment](file:///Users/raghhavv03/Workspace/Learning/python-fundamentals/assignments/09_part_5_assignment.pdf) \| [Solution](file:///Users/raghhavv03/Workspace/Learning/python-fundamentals/assignments/10_part_5_assignment_solution.py) |

---

## 📁 Repository Structure

```
python-fundamentals/
├── lessons/           # Topic-by-topic code demonstrations
│   ├── 01_part_1.py
│   ├── 02_part_2.py
│   ├── 03_part_3.py
│   ├── 04_part_4.py
│   └── 05_part_5.py
├── assignments/       # Problem statements (PDF) and solutions (.py)
│   ├── 01_part_1_assignment.pdf
│   ├── 02_part_1_assignment_solution.py
│   ├── 03_part_2_assignment.pdf
│   ├── 04_part_2_assignment_solution.py
│   ├── 05_part_3_assignment.pdf
│   ├── 06_part_3_assignment_solution.py
│   ├── 07_part_4_assignment.pdf
│   ├── 08_part_4_assignment_solution.py
│   ├── 09_part_5_assignment.pdf
│   └── 10_part_5_assignment_solution.py
├── notes/             # Comprehensive lecture notes (PDF)
│   ├── 01_part_1_notes.pdf
│   ├── 02_part_2_notes.pdf
│   ├── 03_part_3_notes.pdf
│   ├── 04_part_4_notes.pdf
│   └── 05_part_5_notes.pdf
└── data/              # Input data files for file handling exercises (JSON, TXT)
    ├── data.json
    ├── sample_1.txt
    ├── sample_2.txt
    ├── sample_3.txt
    └── word_search.txt
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher

### Running Lessons & Assignments

Clone the repository and run scripts directly from the repository root to ensure correct relative path resolution for data files:

```bash
# Clone the repository
git clone https://github.com/<username>/python-fundamentals.git

# Change into directory
cd python-fundamentals

# Execute a lesson script
python3 lessons/01_part_1.py

# Execute an assignment solution
python3 assignments/02_part_1_assignment_solution.py
```

---

## 🛠️ Key Topics & Technologies

- **Core Python**: Syntax, operators, type casting, control structures.
- **Data Structures**: Lists, Tuples, Sets, Dictionaries, Methods & Operations.
- **OOP Architecture**: Encapsulation, Multilevel/Multiple Inheritance, Polymorphism, Abstract Base Classes (`abc`).
- **File Management & Data Handling**: File I/O with context managers (`with`), JSON Parsing & Serialization (`json` module).
- **Robust Code**: Exception Handling (`try-except-else-finally`) & Defensive Programming.

---

## 📄 License

This repository is available for personal learning and reference.
