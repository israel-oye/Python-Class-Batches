# Module 1: Introduction to Python and Programming Fundamentals

## Topics

### 1. Setting Up the Environment

- **Sub-topics:**
  - Installing Python: How to download and install Python from the official website.
  - IDEs: Overview of Integrated Development Environments (IDEs) such as VS Code, PyCharm, and Jupyter Notebooks.
  - Configuring the environment: Setting up paths, checking Python version.

**Activities:**

- Guide students to install Python and an IDE of their choice.
- Verify installation by running the `python --version` command in the terminal.
- How to open the IDE and create a basic script.

---

### 2. Introduction to Programming

- **Sub-topics:**
  - What is Python?: Brief history, use cases, and why it’s beginner-friendly.
  - Understanding programming concepts: Algorithms, flow of control, and problem-solving basics.

**Activities:**

- Discuss real-life examples of algorithms (e.g., making eba).
- Write pseudocode for simple tasks like turning on a light bulb.

---

### 3. Basic Syntax and Structure

- **Sub-topics:**
  - Variables:
    - Naming conventions, Naming-Case: snake, camel, Pascal
      - Do's: descriptive, clear
       - Dont's: uppercase, keywords
 	  - Avoiding `NameError`
 	  - Assigning variables: Simple, multi-assignment, variable swapping
  - Primitive Data types: Integers, floats, strings, and boolean.
    - String
  		  - *Formatting
     			- f-string
     			- `.format()`
     			- string literals
       - Changing cases: `upper`, `lower`, `title`, `capitalize`
  		  - Concatenation
  		  - Adding whitespace and character escaping
  		  - Stripping whitespace: `strip`, `lstrip`, `rstrip`
  		  - Other string methods: `startswith`, `endswith`, `count`, `isupper`, `islower`, *`split`
  		  - Avoiding syntax errors with string: enclosing quotes
   		 - Quotes in strings
 	  - Numbers
       - Integers
  		  - Float
  		  - Avoiding `TypeError`
 	  - Boolean
    		- *Truthy and Falsey values
 	  - Type checking, Type conversion/casting - implicit vs explicit , TypeError
  - Input and output: Using `input()` and `print()` functions.
  - Comments: Single-line and multi-line comments.
  - Code readability: Indentation, spacing, and naming conventions.
  - Swapping variables

**Activities:**

- Create variables to store a name and age, then print a greeting message.

```python
name = input("What is your name? ")
age = int(input("How old are you? "))
print(f"Hello, {name}! You are {age} years old.")
```

- Write a program with meaningful comments explaining each step.

---

### 4. Basic Operators

- **Sub-topics:**
  - Arithmetic operators: `+`, `-`, `*`, `/`, `%`, `**`, `//`.
  - Assignment and re-assignment operators: `=`, `+=`, etc.
  - Comparison operators: `==`, `!=`, `>`, `<`, `>=`, `<=`.
  - Operator precedence: Understanding the order of operations (PEDMAS).

**Activities:**

- Create a calculator that performs basic arithmetic operations.

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Quotient: {num1 / num2}")
```

- Write a program to evaluate expressions with multiple operators and explain the results.

---

### Expanded Activities

- **Interactive Quiz:** Create a small quiz to test students’ understanding of Python basics. Questions can include identifying errors, predicting outputs, and choosing the correct operator.

- **Assignment:** Write a program that calculates the area of a rectangle and the circumference of a circle, given user inputs.

```python
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
print(f"Area of the rectangle: {length * width}")

radius = float(input("Enter the radius of the circle: "))
print(f"Circumference of the circle: {2 * 3.14159 * radius}")
```

- **Code Review:** Students exchange programs and provide feedback on code readability and correctness.

# Module 2: Control Flow

## Topics and Sub-Topics

### 1. Conditional Statements

#### Sub-Topics

- **Recap of Truthy & Falsy values**
- **Basic If Statements**
  - Syntax and usage of `if` statements.

      ```
   # !!This is pseudocode not Python!!
   if conditional_test:
       do something   
   ```

  - Equality operator `=` vs `==`
  - Other comparism operators: `!=`, `>`, `<`, `>=`, `<=`,
  - Logical operators:`and`, `or`, `not`
  - Identity operator: `is`, `is not`
  - Understanding indentation and block structure.
- **If-Else Statements**
  - Adding alternate execution paths.
- **Elif Statements**
  - Handling multiple conditions with `elif`.
- **Nested Conditions**
  - Writing `if` statements within other `if` blocks.
- **Logical Operators in Conditions**
  - Using `and`, `or`, and `not` for compound conditions.
- **Omitting the else block**

#### Code Examples

```python
# Basic If Statement
number = 10
if number > 5:
    print("The number is greater than 5")

# If-Else Statement
age = 18
if age >= 18:
    print("You are eligible to vote.")
else:
    print("Wọn kere si number wa!")

# Elif Statement
marks = 85
if marks >= 90:
    print("Grade: A1")
elif marks >= 75:
    print("Grade: B2")
elif marks >= 50:
    print("Grade: C3")
else:
    print("Grade: F9 🐟")

# Nested Conditions
num = 15
if num > 10:
    if num % 2 == 0:
        print("The number is even and greater than 10.")
    else:
        print("The number is odd and greater than 10.")
```

### 2. Loops

~Explain list, random and range before going ahead~

#### Sub-Topics

- **For Loops**
  - Iterating over a range of numbers.
  - Iterating over lists, strings, and other iterables.
- **While Loops**
  - Repeating actions until a condition becomes false.
- **Loop Control Statements**
  - `break`: Exiting a loop prematurely.
  - `continue`: Skipping the current iteration.
  - `pass`: Placeholder for incomplete code.

#### Code Examples

```python
# For Loop with Range
for i in range(5):
    print(f"Iteration {i}")

# For Loop with List
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# While Loop
counter = 0
while counter < 5:
    print(f"Counter: {counter}")
    counter += 1

# Using Break
for number in range(10):
    if number == 5:
        break
    print(number)

# Using Continue
for number in range(10):
    if number % 2 == 0:
        continue
    print(number)

# Using Pass
for _ in range(5):
    pass  # Placeholder for future code
```

### 3. Basic Debugging

#### Sub-Topics

- **Identifying Syntax Errors**
  - Common issues like indentation errors and incorrect operators.
- **Using Print Statements for Debugging**
  - Adding print statements to track variables and flow.
- **Understanding Error Messages**
  - Reading and interpreting Python error messages.

#### Code Examples

```python
# Debugging with Print Statements
for i in range(5):
    print(f"Debug: i = {i}")  # Helps to track loop iterations

# Syntax Error Example
# print("Hello World"   # Uncomment to fix missing parenthesis

# Error Message Example
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error occurred: {e}")
```

## Expanded Class Activities

1. **Number Classification**:
   - Write a program that asks the user for a number and classifies it as positive, negative, or zero using conditional statements.

   ```python
   num = int(input("Enter a number: "))
   if num > 0:
       print("Positive number")
   elif num < 0:
       print("Negative number")
   else:
       print("Zero")
   ```

2. **FizzBuzz Game**:
   - Implement a FizzBuzz program using loops and conditional statements.

   ```python
   for num in range(1, 21):
       if num % 3 == 0 and num % 5 == 0:
           print("FizzBuzz")
       elif num % 3 == 0:
           print("Fizz")
       elif num % 5 == 0:
           print("Buzz")
       else:
           print(num)
   ```

3. **Basic Pattern Printing**:
   - Use nested loops to print a pyramid pattern.

   ```python
   rows = 5
   for i in range(1, rows + 1):
       print(" " * (rows - i) + "*" * (2 * i - 1))
   ```

4. **Guess the Number Game**:
   - Implement a number guessing game where the user has to guess a randomly generated number.

   ```python
   import random

   secret_number = random.randint(1, 100)
   attempts = 0

   while True:
       guess = int(input("Guess the number (1-100): "))
       attempts += 1
       if guess == secret_number:
           print(f"Congratulations! You guessed it in {attempts} attempts.")
           break
       elif guess < secret_number:
           print("Too low. Try again.")
       else:
           print("Too high. Try again.")
   ```

5. **BMI Calculator**
 - Design a BMI calculator based on the user's age and height.

# Module 3: Data Structures

## Topics

### 1. **Lists**

- **Definition**: a collection of items in a particular order
- **Creating Lists**: Introduction to creating and initializing lists.
- **Manipulating Lists**
  - Accessing: by index,
  - Adding: `append()`, by assignment
  - Removing:`remove()`, `pop()`, `del list[index]`
  - Inserting: `insert()`, by index
  - Methods: , `extend()`, by assignment
- **List Slicing**: Extracting sublists using slicing
- **Organizing Lists**: `list.sort()`, `sorted()`, *`list.reverse()`
- **Length of a list**
- **Avoiding the `IndexError`**
- **`str.split()` and `str.join()`**
- **Iteration**: Looping through lists using `for`, Membership operators, and list comprehensions;

#### Code Example

```python
# Creating and manipulating a list
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'cherry', 'orange']

# Slicing
print(fruits[1:])  # Output: ['cherry', 'orange']

# List comprehension
uppercase_fruits = [fruit.upper() for fruit in fruits]
print(uppercase_fruits)  # Output: ['APPLE', 'CHERRY', 'ORANGE']
```

---

### 1a. **Range**

- **Definition**: A sequence of numbers, often used in loops.
- **Creating a Range**:
  - Syntax: `range(start, stop, step)`
  - Default behavior: `range(stop)` assumes `start=0` and `step=1`.
- **Accessing Range Elements**:
  - Converting to a list using `list(range())`.
  - Indexing within a range.
- **Common Uses**:
  - Iterating in `for` loops.
  - Generating sequences of numbers.
- **Memory Efficiency**: Why `range` is more efficient than lists for large sequences.
    >When you create a large list, such as `list(range(1000000))`, the entire sequence from 0 to 999,999 must be generated and stored in memory. This can be very memory-intensive, especially for sequences with millions of numbers. For example, creating a list of one million numbers will take up a significant amount of RAM, as the entire list exists at once in memory.
 
 >In contrast, `range(1000000)` only stores the start, stop, and step values, without allocating memory for every number in the sequence. If you need a specific value from the range, Python calculates it as needed. This leads to a dramatic reduction in memory usage, which is particularly beneficial when working with very large sequences.
- **Range Object Properties**: Immutable nature, cannot be changed after creation.
  
#### Code Example

```python
# Creating ranges
r = range(1, 10, 2)
print(list(r))  # Output: [1, 3, 5, 7, 9]

# Using range in a loop
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4
```

---

### 1b. **Random**

- **Definition**: Module for generating random numbers or choices.
- **Importing the Module**: `import random`.
- **Generating Random Numbers**:
  - `random.randint(a, b)`: Random integer between `a` and `b` (inclusive).
  - `random.random()`: Random float between `0.0` and `1.0`.
  - `random.uniform(a, b)`: Random float between `a` and `b`.
- **Working with Lists**:
  - `random.choice(seq)`: Select a random item from a sequence.
  - `random.shuffle(seq)`: Shuffle a sequence in place.
  - `random.sample(seq, k)`: Select `k` random items without replacement.
- **Seeding Randomness**:
  - Setting a seed using `random.seed()` for reproducible results.
- **Advanced Methods**:
  - Generating Gaussian numbers: `random.gauss(mu, sigma)`.
  - Working with probability distributions.

#### Code Example

```python
import random #this is a module

# Random integers
num = random.randint(1, 100)
print(num)  # Example output: 42

# Random float
flt = random.random()
print(flt)  # Example output: 0.7234

# Shuffle and choice
fruits = ["apple", "banana", "cherry"]
random.shuffle(fruits)
print(fruits)  # Example output: ['cherry', 'apple', 'banana']

random_fruit = random.choice(fruits)
print(random_fruit)  # Example output: 'apple'
```

---

## Class Activities

1. **Range Exploration Game**:
   - Write a program where students:
     - Create ranges with different `start`, `stop`, and `step` values.
     - Use the range in loops to print patterns (e.g., number pyramids).
  
2. **Random Number Guessing Game**:
   - Create a game where the program:
     - Generates a random number.
     - Asks the user to guess it, providing feedback (higher/lower).
     - Tracks the number of attempts.

---

### 2. **Tuples**

- **What Are Tuples?**: Understanding the immutability of tuples.
- **Accessing Elements**: Indexing and slicing.
- **Unpacking Tuples**: Assigning tuple elements to variables.

#### Code Example

```python
# Creating and using tuples
coordinates = (10, 20, 30)

# Accessing elements
print(coordinates[1])  # Output: 20

# Unpacking
x, y, z = coordinates
print(x, y, z)  # Output: 10 20 30
```

### 3. **Dictionaries**

- **Introduction to Dictionaries**: Key-value pairs.
- **Basic Operations**: Adding, updating, deleting entries.
- **Dictionary Methods**: `keys()`, `values()`, `items()`.
- **Nested Dictionaries**: Storing dictionaries within dictionaries.

#### **🔹 What is a Dictionary?**

A **dictionary (`dict`)** in Python is like a **real-world dictionary** 📖—it holds **key-value pairs** where you look up a **word (key)** and find its **meaning (value)**.

🔹 **Think of it as a contact book** 📞

- The **name** is the **key**
- The **phone number** is the **value**

```python
contacts = {"Alice": "123-456", "Bob": "987-654"}
print(contacts["Alice"])  # Output: 123-456
```

---

#### **🔹 Creating and Using a Dictionary**

#### **1️⃣ Creating a Dictionary**

```python
student = {
    "name": "John",
    "age": 20,
    "grade": "A"
}
```

---

#### **2️⃣ Accessing Values**

```python
print(student["name"])  # Output: John
print(student["age"])   # Output: 20
```

---

### **3️⃣ Adding & Updating Entries**

```python
student["city"] = "New York"   # Adding new key-value pair
student["grade"] = "A+"        # Updating value
print(student)
```

---

#### **4️⃣ Deleting a Key**

```python
del student["city"]
print(student)
```

---

### **🔹 Looping Through Dictionaries**

#### **1️⃣ Looping Through Keys**

```python
for key in student:
    print(key)  # Prints each key
```

---

#### **2️⃣ Looping Through Values**

```python
for value in student.values():
    print(value)  # Prints each value
```

---

#### **3️⃣ Looping Through Key-Value Pairs**

```python
for key, value in student.items():
    print(f"{key}: {value}")
```

---

#### **4️⃣ Checking if a Key Exists**

```python
if "name" in student:
    print("Student has a name key!")
```

---

### **📝 Exercises (Increasing Difficulty)**

#### **1️⃣ Simple Dictionary Lookup**

📌 **Exercise:** Create a dictionary of **3 countries and their capitals**. Allow the user to enter a country name and print its capital.

🛠 **Assignment:** Modify the program to display **"Not found"** if the country is not in the dictionary.

---

#### **2️⃣ Counting Word Frequency**

📌 **Exercise:** Given the sentence `"apple banana apple orange banana apple"`, count how many times each word appears using a dictionary.

```python
sentence = "apple banana apple orange banana apple"
words = sentence.split()

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)
```

🛠 **Assignment:** Modify it to ignore case (`"Apple"` and `"apple"` should count as the same word).

---

#### **3️⃣ Reverse a Dictionary**

📌 **Exercise:** Given a dictionary `{1: 'a', 2: 'b', 3: 'c'}`, swap keys and values to get `{'a': 1, 'b': 2, 'c': 3}`.

🛠 **Assignment:** Modify it to handle cases where **two keys might have the same value**.

---

#### **4️⃣ Student Grades System**

📌 **Exercise:**

- Create a dictionary where **student names** are keys and **lists of scores** are values.
- Calculate the **average score** for each student.

```python
students = {
    "Alice": [85, 90, 78],
    "Bob": [88, 76, 92]
}

for name, scores in students.items():
    avg = sum(scores) / len(scores)
    print(f"{name}: {avg:.2f}")
```

🛠 **Assignment:** Modify the program to **find the student with the highest average score**.

---

#### **5️⃣ Merging Two Dictionaries**

📌 **Exercise:** Given two dictionaries:

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
```

Write a program to **merge them into one dictionary**.

🛠 **Assignment:** Modify the code to **combine values** if a key appears in both dictionaries.

#### Code Example

```python
# Working with dictionaries
student = {
    "name": "John",
    "age": 25,
    "grades": [90, 85, 92]
}

# Accessing and modifying data
print(student["name"])  # Output: John
student["age"] = 26

# Nested dictionary
class_data = {
    "class_name": "Physics",
    "students": [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 23}
    ]
}
print(class_data["students"][0]["name"])  # Output: Alice
```

### 3b. **List & Dictionary Comprehensions**

- **What Are List Comprehensions?**: A concise way to create lists.
- **What Are Dictionary Comprehensions?**: A concise way to create dictionaries.

#### Code Example

```python
# List comprehension
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# Dictionary comprehension
squared_dict = {x: x**2 for x in range(10)}
print(squared_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
```

---

### 4. **Sets**

- **What Are Sets?**: Properties of sets (unique elements, unordered).
- **Set Operations**: Union, intersection, difference, symmetric difference.
- **Methods**: `add()`, `remove()`, `discard()`, `clear()`.

#### Definition
>
> A set is an unordered collection of unique, hashable elements. Sets are mutable, meaning you can add or remove items after its creation, but the items themselves must be of an immutable type (like strings, numbers, or tuples).
>
### Understanding Sets in Python

#### Key Characteristics of Sets

1. **Unordered Nature**:

- Sets do not maintain a specific order of elements. This means the order in which you add elements to a set may not be the same as the order in which they are stored or displayed.

2. **Unique Elements**:

- Sets automatically remove duplicate values, ensuring that each element is unique.

#### Why Use Sets?

1. **Set Operations**:

- Sets are ideal for performing mathematical set operations like union, intersection, and difference.

2. **Removing Duplicates**:

- Sets can be used to quickly eliminate duplicate values from a collection.

3. **Efficient Membership Testing**:

- Checking if an element exists in a set is highly efficient due to the underlying hash-based implementation.

4. **Simplifying Data**:

- Sets help in managing and simplifying data by focusing on unique and relevant elements.

#### Code Example

```python
# Working with sets
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Set operations
print(set_a | set_b)  # Union: {1, 2, 3, 4, 5, 6}
print(set_a & set_b)  # Intersection: {3, 4}
print(set_a - set_b)  # Difference: {1, 2}
```

## Class Activities

1. **List Manipulation Game**:
   - Create a shopping list program where students can:
     - Add items to a list.
     - Remove items.
     - Display the current list.

2. **Dictionary Lookup Tool**:
   - Build a dictionary where students store and retrieve definitions of words.
   - Implement a feature to add new words and delete existing ones.

3. **Tuple Unpacking Challenge**:
   - Provide a tuple containing dimensions of objects and have students unpack and calculate areas or volumes.

4. **Set Operations Quiz**:
   - Create two sets of numbers and have students perform union, intersection, and difference operations interactively.

5. **Group Activity**: Create a nested dictionary to represent a school's structure (e.g., classes, students, grades) and perform operations to retrieve specific details like a student’s grade.

---

# Module 3: Functions

## Topics

### 1. **Defining and Calling Functions**

- **What Are Functions?**: Introduction to reusable blocks of code.
- **Defining Functions**:
  - Syntax of `def` and the importance of function names.
  - Writing the first simple function.
- **Calling Functions**:
  - How to execute a defined function.
  - Passing no arguments and receiving default behavior.

#### Code Example

```python
# Defining and calling a function
def greet():
    """Display a simple greeting"""
    print("Ẹnlẹ o, araye!")

greet()  # Output: Hello, world!
```

### 2. **Function Arguments & Parameters**

- **What Are Parameters?**: Inputs to functions for customization.
- **Parameter vs Argument**: e.g block mould vs concrete
- **Positional Arguments**:
  - Passing arguments based on position.
- **Keyword Arguments**:
  - Explicitly specifying argument names.
  > A keyword argument is a name-value pair that you pass to a function. You directly associate the name and the value within the argument, so when you pass the argument to the function, there’s no confusion (you won’t end up with a bingo named Dog). Keyword arguments free you from having to worry about correctly ordering your arguments in the function call, and they clarify the role of each value in the function call.
- **Default Parameters**:
  - Providing default values for parameters.
- **Arbitrary Arguments**:
  - Using `*args` for multiple positional arguments.
  - Using `**kwargs` for multiple keyword arguments.

#### Code Example

```python
# Function with parameters
def greet_person(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet_person("Aliyu")  # Output: Hello, Aliyu!
greet_person("Bobola", greeting="Hi")  # Output: Hi, Bobola!


# Passing arguments based on position
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
 
describe_pet('bingo', 'dog')  #Output: I have a bingo.\nMy bingo's name is Dog.


# Passing arguments by keyword
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
 
describe_pet(animal_type='dog', pet_name='bingo') #Output: I have a dog.\nMy dog's name is Bingo


# Using *args and **kwargs
def print_details(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

print_details(1, 2, 3, name="Alice", age=30)
```

### 3. **Returning Values**

- **What Is a Return Statement?**:
  - Sending data back to the caller.
- **Single vs Multiple Returns**:
  - Returning one value or multiple values (as tuples).

#### Code Example

```python
# Function with return value
def square(number):
    return number * number

result = square(5)
print(result)  # Output: 25

# Returning multiple values
def math_operations(a, b):
    return a + b, a - b, a * b, a / b

add, subtract, multiply, divide = math_operations(10, 2)
print(add, subtract, multiply, divide)
```

### 3B. **Docstrings and Annotations**
- **What Are Docstrings?**:
  - Multi-line strings used to document functions.
- **Function Annotations**:
  - Adding type hints to function parameters and return values.
#### Code Example

```python
# Function with docstring and annotations
def add_numbers(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b
result = add_numbers(3, 5)
print(result)  # Output: 8
```
- **Argument Annotations**:
  - Specifying expected types for function parameters.
```pythondef greet(name: str, age: int) -> str:
    """Return a greeting message."""
    return f"Hello, {name}! You are {age} years old."
print(greet("Alice", 30))  # Output: Hello, Alice! You are 30 years old.
```
- **Return Type Annotations**:
  - Indicating the type of value a function returns.
```python
def calculate_area(radius: float) -> float:
    """Return the area of a circle given its radius."""
    import math
    return math.pi * radius ** 2
print(calculate_area(5.0))  # Output: 78.53981633974483
```
- **Parameter documentation**:
  - Using docstrings to describe parameters and return values.
```python
def multiply(x: float, y: float) -> float:
    """
    Multiply two numbers.

    Parameters:
    x (float): The first number.
    y (float): The second number.

    Returns:
    float: The product of x and y.
    """
    return x * y
print(multiply(4.0, 5.0))  # Output: 20.0
```

### 3C. **Arbitrary Argument Lists**
- **Using `*args`**:
  - Accepting a variable number of positional arguments.
- **Using `**kwargs`**:
  - Accepting a variable number of keyword arguments.
#### Code Example
```python
# Using *args
def sum_all(*args):
    return sum(args)
print(sum_all(1, 2, 3, 4))  # Output: 10
# Using **kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="Alice", age=30, city="New York")  # Output: name: Alice\nage: 30\ncity: New York
```



### 4. **Scope**

- **Local vs Global Variables**:
  - Understanding the visibility of variables.
- **Modifying Global Variables**:
  - Using the `global` keyword.

#### Code Example

```python
# Local vs Global Scope
x = 10  # Global variable

def modify_variable():
    global x
    x = x + 5  # Modify global variable

modify_variable()
print(x)  # Output: 15
```

### 5. **Lambda Functions**

- **What Are Lambda Functions?**:
  - Anonymous, one-line functions.
- **When to Use Lambda Functions**:
  - Use in sorting, filtering, and map/reduce operations.

#### Code Example

```python
# Lambda function example
square = lambda x: x * x
print(square(4))  # Output: 16

# Using lambda with sorted
students = [("Alice", 25), ("Bob", 22), ("Charlie", 23)]
sorted_students = sorted(students, key=lambda student: student[1])
print(sorted_students)  # Output: [('Bob', 22), ('Charlie', 23), ('Alice', 25)]
```

---

## Class Activities

1. **Custom Greeting Function**:
   - Write a function that accepts a name and a greeting message, then prints the personalized greeting.

   ```python
   def custom_greeting(name, message):
       print(f"{message}, {name}!")
   custom_greeting("John", "Good morning")
   ```

2. **Calculator Function**:
   - Implement a calculator function that accepts two numbers and an operation (e.g., add, subtract, multiply, divide).

   ```python
   def calculator(a, b, operation):
       if operation == "add":
           return a + b
       elif operation == "subtract":
           return a - b
       elif operation == "multiply":
           return a * b
       elif operation == "divide":
           return a / b
   print(calculator(10, 5, "add"))  # Output: 15
   ```

3. **Student Score Analyzer**:
   - Create a function that calculates the average score of a list of students and identifies the highest and lowest scores.

   ```python
   def analyze_scores(scores):
       return {
           "average": sum(scores) / len(scores),
           "highest": max(scores),
           "lowest": min(scores)
       }
   results = analyze_scores([85, 90, 78, 92, 88])
   print(results)
   ```

4. **Lambda Sorting Challenge**:
   - Sort a list of dictionaries representing books by title or author using a lambda function.

5. **Scope Experiment**:
   - Write a program to demonstrate the difference between local and global variables.

---

# Recursion in Python

Recursion is a programming technique in which a function calls itself to solve a problem. It is especially useful for solving problems that can be broken down into smaller, similar sub-problems. In a recursive solution, the function usually has a base case to end the recursion and one or more recursive cases that continue breaking down the problem.

---

## Key Concepts

- **Base Case**: The simplest instance of the problem that can be solved directly, preventing infinite recursion.
- **Recursive Case**: The part of the function that breaks the problem into smaller sub-problems and calls the function itself.
- **Stack Overflow**: Recursion uses the call stack. If the recursion is too deep (no proper base case or too many recursive calls), it can lead to a stack overflow error.

---

## Example 1: Factorial Function

The factorial of a non-negative integer `n` (denoted as `n!`) is the product of all positive integers less than or equal to `n`. The factorial can be defined recursively:

- **Base Case**: `factorial(0) = 1`
- **Recursive Case**: `factorial(n) = n * factorial(n-1)`

### Code Example

```python
def factorial(n):
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    # Recursive case: multiply n by factorial of n-1
    else:
        return n * factorial(n - 1)

# Testing the factorial function
print(factorial(5))  # Expected output: 120
```

### Exercises

1. **Exercise 1**: Modify the `factorial` function to handle negative numbers by returning an error message if `n` is negative.
2. **Exercise 2**: Write a loop or a recursive function to calculate the factorial of a series of numbers (e.g., from 0 to 10) and print each result.

---

## Example 2: Fibonacci Sequence

The Fibonacci sequence is a series where each number is the sum of the two preceding ones. The recursive definition is:

- **Base Cases**: `fibonacci(0) = 0`, `fibonacci(1) = 1`
- **Recursive Case**: `fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)`

### Code Example

```python
def fibonacci(n):
    # Base cases: return n if n is 0 or 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case: sum of the two preceding numbers
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Testing the fibonacci function
print(fibonacci(6))  # Expected output: 8, since the sequence is 0, 1, 1, 2, 3, 5, 8...
```

### Exercises

1. **Exercise 1**: Write a function that prints the first `n` Fibonacci numbers by calling the `fibonacci` function for each index from 0 to `n-1`.
2. **Exercise 2**: Analyze the performance of the recursive Fibonacci function. Hint: For larger values of `n`, consider exploring memoization to improve efficiency.

---

## Example 3: Sum of a List Using Recursion

Recursion can also be applied to data structures like lists. In this example, we'll sum all the numbers in a list recursively.

### Code Example

```python
def recursive_sum(numbers):
    # Base case: if the list is empty, the sum is 0
    if not numbers:
        return 0
    # Recursive case: sum the first number with the sum of the remaining list
    else:
        return numbers[0] + recursive_sum(numbers[1:])

# Testing the recursive sum function
print(recursive_sum([1, 2, 3, 4, 5]))  # Expected output: 15
```

### Exercises

1. **Exercise 1**: Modify the `recursive_sum` function to handle a list of numbers that may include negative values.
2. **Exercise 2**: Compare the recursive approach with an iterative approach. Implement an iterative version and test both with a large list to see which one performs better.

---

## Recursion: Advantages and Challenges

### Advantages

- **Simplicity**: Code can be easier to read and write, particularly for problems that fit naturally into a recursive model.
- **Problem Breakdown**: Encourages breaking a problem into smaller, identical problems.

### Challenges

- **Performance**: Recursive solutions can be less efficient and require more memory due to function calls.
- **Debugging**: Tracing recursive calls can be more difficult.

---

```
