#note the same method has been used for both advanced.

"""
Now that you know how to loop through a dictionary, clean up the code
from exercise 6.3 by replacing your series of print() calls with a loop
that runs though the dictionary's keys and values. When you're sure
that your loop works, add five more Python terms to your glossary.
When you run your program again, these new words and meanings should
automatically be included in the output."""

#he specified 5 but i did 50 for fun its not compulsory though


dictionary = {"Algorithm": "A step-by-step procedure to solve a problem.",
        "Argument": "A value passed to a function when calling it.",
        "Array": "A collection of items stored at contiguous memory locations.",
        "Assignment": "The process of storing a value in a variable.",
        "Boolean": "A data type with two possible values: True or False.",
        "Bug": "An error in a program that causes incorrect results.",
        "Class": "A blueprint for creating objects in object-oriented programming.",
        "Compiler": "A program that translates source code into machine code.",
        "Concatenation": "Joining two or more strings end-to-end.",
        "Conditional": "A statement that runs code only if a condition is true.",
        "Constant": "A variable whose value should not change during execution.",
        "Constructor": "A special method used to initialize objects.",
        "Data Structure": "A way of organizing and storing data efficiently.",
        "Debugging": "The process of finding and fixing errors in code.",
        "Decorator": "A function that modifies another function or method.",
        "Dictionary": "A collection of key-value pairs in Python.",
        "Docstring": "A string literal used to document a function, class, or module.",
        "Dynamic Typing": "Python determines variable types at runtime.",
        "Exception": "An error detected during execution.",
        "Expression": "A combination of values and operators that produces a result.",
        "Float": "A number with a decimal point.",
        "For Loop": "A loop that iterates over a sequence.",
        "Function": "A block of reusable code that performs a task.",
        "Garbage Collection": "Automatic memory management in Python.",
        "Generator": "A function that yields values one at a time using 'yield'.",
        "Global Variable": "A variable declared outside all functions.",
        "IDE": "Integrated Development Environment for coding.",
        "Immutable": "An object whose value cannot be changed after creation.",
        "Indentation": "Whitespace at the start of a line to define code blocks.",
        "Instance": "An object created from a class.",
        "Integer": "A whole number without a decimal point.",
        "Iterable": "An object capable of returning its members one at a time.",
        "Lambda": "An anonymous function defined with the lambda keyword.",
        "Library": "A collection of pre-written code for reuse.",
        "List": "An ordered, mutable collection of items.",
        "Loop": "A control structure for repeated execution.",
        "Method": "A function defined inside a class.",
        "Module": "A file containing Python code that can be imported.",
        "Mutable": "An object whose value can be changed after creation.",
        "Namespace": "A container for variable names and their values.",
        "Object": "An instance of a class.",
        "Operator": "A symbol that performs an operation on values.",
        "Parameter": "A variable in a function definition.",
        "Recursion": "A function calling itself.",
        "Return": "A statement that sends a value back from a function.",
        "Set": "An unordered collection of unique items.",
        "String": "A sequence of characters.",
        "Syntax": "The rules that define valid combinations of symbols in code.",
        "Tuple": "An ordered, immutable collection of items.",
        "Variable": "A named location in memory that stores a value."
    }

for name, meaning in dictionary.items():

    print(f"{name}: \t\t{meaning}")