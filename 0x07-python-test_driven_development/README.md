# 0x07. Python - Test-driven development

An introductory project into creating doctests and unittests

## Resources

- [doctest — Test interactive Python examples](https://docs.python.org/3.4/library/doctest.html)

- [doctest – Testing through documentation](https://pymotw.com/3/doctest/)

- [Unit Tests in Python](https://www.youtube.com/watch?v=1Lfv5tUGsn8)

## File Descriptions

| Filename                      | Description                                                                                                                   |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `0-add_integer.py`            | Function that adds two integers (Doctest on `tests/0-add_integer.txt`)                                                        |
| `2-matrix_divided.py`         | Function that divides all elemtns of a matrix (Doctest on `tests/2-matrix_divided.txt`)                                       |
| `3-say_my_name.py`            | Function that prints `My name is <first name> <last name>` (Doctest on `tests/3-say_my_name.txt`)                             |
| `4-print_square.py`           | Function that prints a square with the character `#` (Doctest on `tests/4-print_sqaure.txt`)                                  |
| `5-text_indentation.py`       | Function that prints a text with 2 new lines after each of these `.`, `?` and `:` (Doctest on `tests/5-text_indentation.txt`) |
| `tests/6-max_integer_test.py` | Unittests for the function `def max_integer(list=[])`                                                                         |
| `100-matrix_mul.py`           | Function that multiplies 2 matrices (Doctest on `tests/100-matrix_mul.txt`)                                                   |
| `101-lazy_matrix_mul.py`      | Function that multiplies 2 matrices by using the module NumPy (Doctest on `tests/101-lazy_matrix_mul.txt`)                    |
| `102-python.c`                | Function that prints Python strings                                                                                           |

## Tasks

- **0. Integers addition**

  - [0-add_integer.py](./0-add_integer.py): Python function that returns the integer addition
    of two numbers.
  - If either of `a` or `b` is not an `int` or `float`, a `TypeError` is raised
    with the message `a must be an integer` or `b must be an integer`.
  - If either of `a` or `b` is a `float`, it is casted to an `int`
    before addition.

- **1. Divide a matrix**

  - [2-matrix_divided.py](./2-matrix_divided.py): Python function that divides all
    elements of a matrix by a common divisor.
  - Returns a new matrix representing the division of all elements of `matrix`
    by `div`.
  - Quotients are rounded to two decimal places.
  - If `matrix` is not a list of lists of `int`s or `float`s, a `TypeError`
    is raised with the message `matrix must be a matrix (list of lists) of integers/floats`.
  - If `matrix` contains rows of different lengths, a `TypeError` is raised
    with the message `Each row of the matrix must have the same size`.
  - If the divisor `div` is not an `int` or `float`, a `TypeError` is raised
    with the message `div must be a number`.
  - If `div` is `0`, a `ZeroDivisionError` is raised with the message
    `division by zero`.

- **2. Say my name**

  - [3-say_my_name.py](./3-say_my_name.py): Python function that prints a name in
    the format `My name is <first_name> <last_name>`.
  - If either of `first_name` or `last_name` is not a `str`, a `TypeError` is
    raised with the message `first_name must be a string` or `last_name must be a string`.

- **3. Print square**

  - [4-print_square.py](./4-print_square.py): Python function that prints a square using
    the `#` character.
  - The paramter `size` represents the height/width of the square.
  - If `size` is not an `int`, a `TypeError` is raised with the message,
    `size must be an integer`.
  - If `size` is less than `0`, a `ValueError` is raised with the message `size must be >= 0`.

- **4. Text indentation**

  - [5-text_indentation.py](./5-text_indentation.py): Python function that prints text with
    indentation.
  - Two new lines are printed after any `.`, `?`, or `:` character.
  - If `text` is not a `str`, a `TypeError` is raised with the message `text must be a string`.
  - No spaces are printed at the beginning or end of each printed line.

- **5. Max integer - Unittest**

  - [tests/6-max_integer_test.py](./tests/6-max_integer_text.py): Python class/script
    that runs unittests for the function `def max_integer(list=[]):`
    (provided by Holberton School).

- **6. Matrix multiplication**

  - [100-matrix_mul.py](./100-matrix_mul.py): Python function that multiplies two matrices.
  - Returns a new matrix representing the multiplication of `m_a` by `m_b`.
  - If either of `m_a` or `m_b` is empty (ie. `== []` or `== [[]]`), a
    `ValueError` is raised with the message `m_a can't be empty` or `m_b can't be empty`.
  - If either of `m_a` or `m_b` is not a list, a `TypeError` is raised with
    the message `m_a must be a list` or `m_b` must be a list.
  - If either of `m_a` or `m_b` is not a list of lists, a `TypeError` is raised
    with the message `m_a must be a list of lists` or `m_b must be a list of lists`.
  - If either of `m_a` or `m_b` is not a list of lists of `int`s or `float`s, a
    `TypeError` is raised with the message `m_a should contain only integers or floats` or `m_b should contain only integers or floats`.
  - If either of `m_a` or `m_b` contains rows of different lengths, a `TypeError`
    is raised with the message `each row of m_a must should be of the same size` or
    `each row of m_b must should be of the same size`.
  - If `m_a` and `m_b` cannot be multiplied (ie. row size of `m_a` does not match
    column size of `m_b`), a `ValueError` is raised with the message `m_a and m_b can't be multiplied`.

- **7. Lazy matrix multiplication**

  - [101-lazy_matrix_mul.py](./101-lazy_matrix_mul.py): Python function that multiplies
    two matrices using the module `NumPy`.
  - Identical in function to [100-matrix_mul.py](./100-matrix_mul.py).

- **8. CPython #3: Python Strings**
  - [102-python.c](./102-python.c): C function that prints basic information about Python
    string objects.
