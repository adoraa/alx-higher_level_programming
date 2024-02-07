# Python - Classes and Objects

## Overview
This project is a collection of Python files that demonstrate the usage of classes and objects. It includes examples of encapsulation, data abstraction, and information hiding.

## Learning Objectives
- What is self
- What is the special __init__ method and how to use it
- What is a property
- What is the difference between an attribute and a property in Python
- What is the Python way of writting getters and setters in Python
- How to dynamically create arbitrary new attributes for existing instances of a class
- How to bind attributes to object and classes
- What is the __dict__ of a class and/or instance of a class and what does it contain
- How Python finds the attributes of an object or class
- How to use the getattr function

## Files
- `my_module.py`: Contains Python modules with classes and functions related to the project.

## How to Run
1. Make sure you have Python 3.8.5 installed.
2. Clone the repository to your local machine.
3. Run the Python files using an editor (vi, vim, emacs) or preferred IDE.

## Style Guide
Code adheres to PEP 8 style guidelines using pycodestyle.

## Documentation
- Modules: `python3 -c 'print(__import__("my_module").__doc__)'`
- Classes: `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`
- Functions: 
  - `python3 -c 'print(__import__("my_module").my_function.__doc__)'`
  - `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`

## By
Guillaume
