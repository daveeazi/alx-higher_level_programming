# 0x0A. Python - Inheritance

An introductory project on inheritance in Python

In this project, I learned about Python class inheritance. I learned about the
differences between super- and sub-classes while practicing inheritance,
definining classes with multiple base classes, and overiding inherited methods
and attributes.

## Function Prototypes

Prototypes for functions written in this project:

| File                    | Prototype                             |
| ----------------------- | ------------------------------------- |
| `0-lookup.py`           | `def lookup(obj):`                    |
| `2-is_same_class.py`    | `def is_same_class(obj, a_class):`    |
| `3-is_kind_of_class.py` | `def is_kind_of_class(obj, a_class):` |
| `4-inherits_from.py`    | `def inherits_from(obj, a_class):`    |
| `101-add_attribute.py`  | `def add_attribute(obj, att, value):` |

## Tasks

- **0. Lookup**

  - [0-lookup.py](./0-lookup.py): Python function that returns a list of available attributes
    and methods of an objects.

- **1. My list**

  - [1-my_list.py](./1-my_list.py): Python class `MyList` that inherits from `list`. Includes:
    - Public instance method `def print_sorted(self):` that prints the list in
      ascending sorted order (assumes all list elements are `int`s).

- **2. Exact same object**

  - [2-is_same_class.py](./2-is_same_class.py): Python function that returns `True` if an object is
    exactly an instance of a specified class; otherwise `False`.

- **3. Same class or inherit from**

  - [3-is_kind_of_class.py](./3-is_kind_of_class.py): Python function that returns `True` if an object is
    an instance or inherited instance of a specified class; otherwise `False`.

- **4. Only sub class of**

  - [4-inherits_from.py](./4-inherits_from.py): Python function that returns `True` if an object is
    an inherited instance (either directly or indirectly) from a specified class;
    otherwise `False`.

- **5. Geometry module**

  - [5-base_geometry.py](./5-base_geometry.py): An empty Python class `BaseGeometry`.

- **6. Improve Geometry**

  - [6-base_geometry.py](./6-base_geometry.py): Python class `BaseGeometry`. Builds on
    [5-base_geometry.py](./5-base_geometry.py) with:
    - Public instance method `def area(self):` that raises an `Exception` with
      the message `area() is not implemented`.

- **7. Integer validator**

  - [7-base_geometry.py](./7-base_geometry.py): Python class `BaseGeometry`. Builds on
    [6-base_geometry.py](./6-base_geometry.py) with:
    - Public instance method `def integer_validator(self, name, value):` that
      validates the parameter `value`.
    - Assumes the parameter `name` is always a string.
    - The parameter `value` must be an `int`, otherwise, a `TypeError` exception
      is raised with the message `<name> must be an integer`.
    - The parameter `value` must be greater than `0`, otherwise, a
      `ValueError` exception is raised with the message `<value> must be greater than 0`.

- **8. Rectangle**

  - [8-rectangle.py](./8-rectangle.py): Python class `Rectangle` that inherits from `BaseGeometry`
    ([7-base_geometry.py](./7-base_geometry.py)). Includes:
    - Private attributes `width` and `height` - validated with `integer_validator`.
    - Instantiation with `width` and `height`: `def __init__(self, width, height):`

- **9. Full rectangle**

  - [9-rectangle.py](./9-rectangle.py): Python class `Rectangle` that inherits from `BaseGeometry`
    ([7-base_geometry.py](./7-base_geometry.py)). Builds on [8-rectangle.py](./8-rectangle.py) with:
    - Implementation of the method `area()`.
    - Special method `__str__` to print `Rectangle`s in the format `[Rectangle] <width>/<height>`.

- **10. Square #1**

  - [10-square.py](./10-square.py): Python class `Square` that inherits from `Rectangle`
    ([9-rectangle.py](./9-rectangle.py)). Includes:
    - Private attribute `size` - validated with `integer_validator`.
    - Instantiation with `size`: `def __init__(self, size):`.
    - Implementation of the `area()` method.

- **11. Square #2**

  - [11-square.py](./11-square.py): Python class `Square` that inherits from `Rectangle`
    ([9-rectangle.py](./9-rectangle.py)). Builds on [10-square.py](./10-square.py) with:
    - Special method `__str__` to print squares in the format `[Square] <width>/<height>`.

- **12. My integer**

  - [100-my_int.py](./100-my_int.py): Python class `MyInt` that inherits from `int`. Includes:
    - Inversion of the `==` and `!=` operators.

- **13. Can I?**
  - [101-add_attribute.py](./101-add_attribute.py): Python function that adds a new attribute to an
    object if possible.
    - If an attribute cannot be added, a `TypeError` exception is raised with the
      message `can't add new attribute`.

<details>
<summary><strong>File Descriptions</strong></summary>
<br>
- (0-lookup.py)[0-lookup.py] - A function that returns the list of available attributes and methods of an object:
  - Prototype: `def lookup(obj):`
  - Returns a `list` object
  - Not allowed to import any module

```
guillaume@ubuntu:~/0x0A$ cat 0-main.py
#!/usr/bin/python3
lookup = __import__('0-lookup').lookup

class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))

guillaume@ubuntu:~/0x0A$ ./0-main.py
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'my_attr1', 'my_meth']
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
guillaume@ubuntu:~/0x0A$
```

- (1-my_list.py)[1-my_list.py] - A class `MyList` that inherits from `list`:
  - Public instance method: `def print_sorted(self):` that prints the list, but sorted (ascending sort)
  - Assumes that all the elements of the list will be of type `int`
  - Not allowed to import any module

```
guillaume@ubuntu:~/0x0A$ cat 1-main.py
#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)

guillaume@ubuntu:~/0x0A$ ./1-main.py
[1, 4, 2, 3, 5]
[1, 2, 3, 4, 5]
[1, 4, 2, 3, 5]
guillaume@ubuntu:~/0x0A$
```

- (2-is_same_class.py)[2-is_same_class.py] - A function that returns `True` if the object is exactly an instance of the specified class; otherwise `False`:
  - Prototype: `def is_same_class(obj, a_class):`
  - Not allowed to import any module

```
guillaume@ubuntu:~/0x0A$ cat 2-main.py
#!/usr/bin/python3
is_same_class = __import__('2-is_same_class').is_same_class

a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))

guillaume@ubuntu:~/0x0A$ ./2-main.py
1 is an instance of the class int
guillaume@ubuntu:~/0x0A$
```

- (3-is_kind_of_class.py)[3-is_kind_of_class.py] - A function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise `False`:
  - Prototype: `def is_kind_of_class(obj, a_class):`
  - Not allowed to import any module

```
guillaume@ubuntu:~/0x0A$ cat 3-main.py
#!/usr/bin/python3
is_kind_of_class = __import__('3-is_kind_of_class').is_kind_of_class

a = 1
if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))
if is_kind_of_class(a, float):
    print("{} comes from {}".format(a, float.__name__))
if is_kind_of_class(a, object):
    print("{} comes from {}".format(a, object.__name__))

guillaume@ubuntu:~/0x0A$ ./3-main.py
1 comes from int
1 comes from object
guillaume@ubuntu:~/0x0A$
```

- (4-inherits_from.py)[4-inherits_from.py] - A function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise `False`:
  - Prototype: `def inherits_from(obj, a_class):`
  - Not allowed to import any module

```
guillaume@ubuntu:~/0x0A$ cat 4-main.py
#!/usr/bin/python3
inherits_from = __import__('4-inherits_from').inherits_from

a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))

guillaume@ubuntu:~/0x0A$ ./4-main.py
True inherited from class int
True inherited from class object
guillaume@ubuntu:~/0x0A$
```

</details>
