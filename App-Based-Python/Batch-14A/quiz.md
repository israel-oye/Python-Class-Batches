## Python Data Types Quiz

### Question 1: What is the data type of the following value?  

```python
x = 10
```

a) float  
b) string  
c) int  
d) list  

---

### Question 2: Which of the following is a valid way to define a string in Python?  

a) `'Hello'`  
b) `"Hello"`  
c) `"""Hello"""`  
d) All of the above  

---

### Question 3: What will be the output of the following code?  

```python
print(type(3.14))
```

a) `<class 'int'>`  
b) `<class 'float'>`  
c) `<class 'str'>`  
d) `<class 'bool'>`  

---

### Question 4: What data type is the result of the following operation?  

```python
result = "5" + "10"
```

a) int  
b) float  
c) str  
d) list  

---

## Python Comparison Operators Quiz

### Question 1: What is the result of `5 == 5`?  

a) True  
b) False  

---

### Question 2: What does the expression `10 != 5` evaluate to?  

a) True  
b) False  

---

### Question 3: What is the outcome of `7 > 3`?  

a) True  
b) False  

---

### Question 4: Evaluate `4 <= 4`  

a) True  
b) False  

---

### Question 5: What will `8 >= 9` return?  

a) True  
b) False  

---

### Question 6: What is the result of the expression `"apple" < "banana"`?  

a) True  
b) False  

---

### Question 7: What does `"hello" == "Hello"` evaluate to?  

a) True  
b) False  

---

### Question 8: What will the expression `len("Python") == 6` return?  

a) True  
b) False  

---

### Question 9: Evaluate `3 < 5 or 10 > 20`  

a) True  
b) False  

---

### Question 10: What does the expression `not ("Python" == "Python")` return?  

a) True  
b) False  

---

## Python If-Else-Elif and Logical Operators Quiz

### Question 1: What will be the output of the following code?
```python
x = 5
if x > 3:
    print("Greater")
else:
    print("Lesser")
```
a) Greater  
b) Lesser  

---

### Question 2: Evaluate the following code snippet:
```python
y = 10
if y < 5:
    print("Low")
elif y < 15:
    print("Medium")
else:
    print("High")
```
a) Low  
b) Medium  
c) High  

---

### Question 3: What will the following code print?
```python
a = True
b = False
if a and b:
    print("True")
else:
    print("False")
```
a) True  
b) False  

---

### Question 4: What is the output of this code?
```python
x = 20
if x < 10 or x > 15:
    print("Outside")
else:
    print("Inside")
```
a) Outside  
b) Inside  

---

### Question 5: What will be printed by the following code?
```python
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D")
```
a) A  
b) B  
c) C  
d) D  

---

### Question 6: What will be the output?
```python
x = 7
if x % 2 == 0:
    print("Even")
else:
    print("Odd")
```
a) Even  
b) Odd  

---

### Question 7: Evaluate the following:
```python
x = 4
if x > 0 and x < 10:
    print("In range")
else:
    print("Out of range")
```
a) In range  
b) Out of range  

---

### Question 8: What does the following code print?
```python
age = 17
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")
```
a) Adult  
b) Teenager  
c) Child  

---

### Question 9: What will the output be?
```python
x = 15
if x < 10 or (x >= 10 and x < 20):
    print("Valid")
else:
    print("Invalid")
```
a) Valid  
b) Invalid  

---

### Question 10: Evaluate the following conditional statement:
```python
color = "red"
if color == "blue":
    print("It's blue")
elif color == "green":
    print("It's green")
else:
    print("Not blue or green")
```
a) It's blue  
b) It's green  
c) Not blue or green  

---

### Answers:
1. a) Greater
2. b) Medium
3. b) False
4. a) Outside
5. b) B
6. b) Odd
7. a) In range
8. b) Teenager
9. a) Valid
10. c) Not blue or green

## Advanced Python Logical Operators Quiz

### Question 1: What will be the output of the following code?

```python
x = 7
y = 3
if (x > 5 and y < 5) or (x < 5 and y > 1):
    print("Condition met")
else:
    print("Condition not met")
```

a) Condition met  
b) Condition not met  

---

### Question 2: Evaluate this expression

```python
age = 20
has_permission = False
if age >= 18 or has_permission:
    print("Access granted")
else:
    print("Access denied")
```

a) Access granted  
b) Access denied  

---

### Question 3: What will the following code print?

```python
score = 75
if (score >= 90 and score <= 100) or (score >= 80 and score < 90):
    print("Good job")
else:
    print("Needs improvement")
```

a) Good job  
b) Needs improvement  

---

### Question 4: Evaluate the following code

```python
is_sunny = False
is_warm = True
if not(is_sunny or is_warm):
    print("Stay indoors")
else:
    print("Enjoy the weather")
```

a) Stay indoors  
b) Enjoy the weather  

---

### Question 5: What will be printed by the following code?

```python
num = 12
if (num % 2 == 0 and num % 3 == 0) or (num % 5 == 0):
    print("Divisible")
else:
    print("Not divisible")
```

a) Divisible  
b) Not divisible  

---

### Answers

1. a) Condition met
2. a) Access granted
3. b) Needs improvement
4. b) Enjoy the weather
5. a) Divisible


## Python Lists Quiz

### Question 1: What will be the output after executing the following code?

```python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
```

a) [1, 2, 3]  
b) [1, 2, 3, 4]  
c) [4, 1, 2, 3]  

---

### Question 2: What does the following code print?

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
```

a) apple  
b) banana  
c) cherry  

---

### Question 3: Evaluate the following code

```python
days = ["Monday", "Tuesday", "Wednesday"]
days.insert(1, "Friday")
print(days)
```

a) ["Monday", "Friday", "Tuesday", "Wednesday"]  
b) ["Monday", "Tuesday", "Friday", "Wednesday"]  
c) ["Friday", "Monday", "Tuesday", "Wednesday"]  

---

### Question 4: What will happen if you execute this code?

```python
numbers = [10, 20, 30, 40]
del numbers[1]
print(numbers)
```

a) [10, 30, 40]  
b) [10, 20, 30]  
c) [20, 30, 40]  

---

### Question 5: What does the expression `len(my_list)` return if `my_list = [5, 10, 15]`?

a) 2  
b) 3  
c) 4  

---

### Question 6: What will be the output of this code?

```python
colors = ["red", "green", "blue"]
colors.remove("green")
print(colors)
```

a) ["red", "green", "blue"]  
b) ["red", "blue"]  
c) Error  

---

### Question 7: Evaluate the outcome of the following snippet

```python
items = ["pen", "pencil", "eraser"]
items.pop()
print(items)
```

a) ["pen", "pencil"]  
b) ["pen", "pencil", "eraser"]  
c) Error  

---

### Question 8: What will this code print?

```python
my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)
```

a) [1, 2, 3]  
b) [1, 2, 3, [4, 5]]  
c) [1, 2, 3, 4, 5]  

---

### Question 9: What does `my_list = [1, 2, 3]` followed by `my_list += [4]` result in?

a) [1, 2, 3]  
b) [1, 2, 3, 4]  
c) Error  

---

### Question 10: What will be the output of this code snippet?

```python
numbers = [5, 10, 15, 20]
if 10 in numbers:
    print("Found")
else:
    print("Not found")
```

a) Found  
b) Not found  

---

### Answers

1. b) [1, 2, 3, 4]
2. b) banana
3. a) ["Monday", "Friday", "Tuesday", "Wednesday"]
4. a) [10, 30, 40]
5. b) 3
6. b) ["red", "blue"]
7. a) ["pen", "pencil"]
8. c) [1, 2, 3, 4, 5]
9. b) [1, 2, 3, 4]
10. a) Found

## Python For-Loop Quiz

### Question 1: What will be printed by the following code?

```python
for i in range(3):
    print(i)
```

a) 0  
b) 1  
c) 0 1 2  
d) 1 2 3  

---

### Question 2: What does the following code output?

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

a) apple  
b) banana  
c) cherry  
d) All of the above  

---

### Question 3: What will the following code print?

```python
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(total)
```

a) 10  
b) 15  
c) 5  

---

### Question 4: What does the following code do?

```python
for i in range(2, 6):
    print(i)
```

a) Prints numbers from 2 to 5  
b) Prints numbers from 2 to 6  
c) Prints numbers from 1 to 5  

---

### Question 5: What will be the result of executing this code?

```python
for i in range(5):
    print(i * 2)
```

a) 0 2 4 6 8  
b) 0 1 2 3 4  
c) 1 2 3 4 5  

---

### Question 6: What will this code output?

```python
numbers = [10, 20, 30]
for num in numbers:
    print(num + 5)
```

a) 10 20 30  
b) 15 25 35  
c) 5 10 15  

---

### Question 7: How many times will the loop run in the following code?

```python
for i in range(1, 10, 2):
    print(i)
```

a) 5  
b) 4  
c) 9  

---

### Question 8: What will be the output of this code?

```python
animals = ["cat", "dog", "fish"]
for animal in animals:
    if animal == "dog":
        print("Found a dog!")
```

a) Found a cat!  
b) Found a dog!  
c) No output  

---

### Question 9: What will this code print?

```python
for i in range(1, 5):
    print(i ** 2)
```

a) 1 2 3 4  
b) 1 4 9 16  
c) 1 4 9  

---

### Question 10: What is the output of the following code?

```python
count = 0
for i in range(3):
    count += 1
print(count)
```

a) 2  
b) 3  
c) 0  

---

### Answers

1. c) 0 1 2
2. d) All of the above
3. b) 15
4. a) Prints numbers from 2 to 5
5. a) 0 2 4 6 8
6. b) 15 25 35
7. a) 5
8. b) Found a dog!
9. c) 1 4 9
10. b) 3

---

# Revision Quiz

**Total Questions: 25**

---

## Section 1: String Operations & Methods (Questions 1-5)

**1. Which of the following string methods removes whitespace from both ends of a string?**
   - A) `strip()`
   - B) `clean()`
   - C) `trim()`
   - D) `remove()`

**2. What is the output of the following code?**
   ```python
   text = "Python"
   result = text.replace('P', 'J')
   print(result)
   ```
   - A) `"Jython"`
   - B) `"Python"` (original string modified)
   - C) `"Jython"` but original string is unchanged
   - D) Error

**3. If you have the string `email = "user@domain.com"`, how would you check if the `@` character is present in the email?**
   - A) `email.contains('@')`
   - B) `'@' in email`
   - C) `email.has('@')`
   - D) `email.index('@')`

**4. What does the `split()` method return when applied to a string?**
   - A) A string
   - B) A tuple
   - C) A list
   - D) A set

**5. What is the output of the following code?**

   ```python
   fruits = ['apple', 'banana', 'cherry']
   result = ', '.join(fruits)
   print(result)
   ```

- A) `['apple, banana, cherry']`
- B) `'apple, banana, cherry'`
- C) `'applr, banana, cherry'`
- D) Error

---

## Section 2: List Operations & Slicing (Questions 6-10)

**6. What is the result of the following list slicing?**

   ```python
   numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
   result = numbers[::2]
   ```

- A) `[0, 2, 4, 6, 8]`
- B) `[1, 3, 5, 7, 9]`
- C) `[0, 1, 2, 3, 4]`
- D) `[5, 6, 7, 8, 9]`

**7. Which method adds an element to the end of a list?**
   - A) `insert()`
   - B) `extend()`
   - C) `append()`
   - D) `add()`

**8. What is the difference between `remove()` and `pop()` methods?**
   - A) `remove()` removes the first occurrence of a value; `pop()` removes by index
   - B) `remove()` removes by index; `pop()` removes by value
   - C) They are identical
   - D) `remove()` modifies the list; `pop()` does not

**9. How would you reverse a list using slicing?**
   - A) `list[0:-1]`
   - B) `list[::-1]`
   - C) `list[-1:0]`
   - D) `list.reverse()`

**10. What is the output of the following code?**
   ```python
   data = [1, 2, 3, 4, 5]
   new_data = data[:]
   new_data.append(6)
   print(data)
   ```
   - A) `[1, 2, 3, 4, 5, 6]`
   - B) `[1, 2, 3, 4, 5]`
   - C) `[6]`
   - D) Error

---

## Section 3: Conditionals & Logical Operators (Questions 11-13)

**11. What is the output of the following code?**
   ```python
   x = 10
   if x > 5 and x < 15:
       print("In range")
   else:
       print("Out of range")
   ```
   - A) `"In range"`
   - B) `"Out of range"`
   - C) `"In range" "Out of range"`
   - D) Error

**12. Which of the following is a "falsy" value in Python?**
   - A) `1`
   - B) `"text"`
   - C) `[]`
   - D) `True`

**13. What does the `in` operator do when used with a string?**
   - A) Checks if a substring exists in the string
   - B) Checks if a character is at a specific index
   - C) Adds a substring to the string
   - D) Removes a substring from the string

---

## Section 4: Loops & Iteration (Questions 14-17)

**14. What is the output of the following code?**
   ```python
   for i in range(1, 4):
       print(i)
   ```
   - A) `1 2 3 4`
   - B) `1 2 3`
   - C) `0 1 2 3`
   - D) `0 1 2`

**15. How can you break out of a loop in Python?**
   - A) `stop`
   - B) `break`
   - C) `exit()`
   - D) `continue`

**16. What is the purpose of the `range()` function's third parameter?**
   - A) The starting point
   - B) The stopping point
   - C) The step size
   - D) The total count

**17. What is the output of the following nested loop?**
   ```python
   for i in range(3):
       for j in range(2):
           print(f"{i}{j}", end=" ")
   ```
   - A) `0 1 2`
   - B) `0 1 0 1 0 1`
   - C) `00 01 10 11 20 21`
   - D) Error

---

## Section 5: List Comprehension (Questions 18-20)

**18. What does the following list comprehension produce?**
   ```python
   squares = [x**2 for x in range(5)]
   print(squares)
   ```
   - A) `[0, 1, 2, 3, 4]`
   - B) `[0, 1, 4, 9, 16]`
   - C) `[1, 4, 9, 16, 25]`
   - D) `[2, 4, 6, 8, 10]`

**19. Which of the following creates a new list with only even numbers from 1 to 10?**
   - A) `[x for x in range(1, 11) if x % 2 == 0]`
   - B) `[x for x in range(1, 11) if x % 2 != 0]`
   - C) `[x for x in range(1, 10)]`
   - D) `[x * 2 for x in range(1, 6)]`

**20. What is the output of the following code?**
   ```python
   words = ["hello", "world"]
   reversed_words = [word[::-1] for word in words]
   print(reversed_words)
   ```
   - A) `["dlrow", "olleh"]`
   - B) `["olleh", "dlrow"]`
   - C) `["world", "hello"]`
   - D) Error

---

## Section 6: Advanced Topics (Questions 21-25)

**21. What does the `split()` method do when used with a custom delimiter?**
   ```python
   text = "apple,banana,cherry"
   result = text.split(',')
   ```
   - A) Splits text into characters
   - B) Splits text by the delimiter and returns a list
   - C) Removes the delimiter from the string
   - D) Counts occurrences of the delimiter

**22. What is the output of this code?**
   ```python
   import random
   random.seed(42)
   nums = [random.randint(1, 10) for _ in range(3)]
   print(len(nums))
   ```
   - A) `10`
   - B) `3`
   - C) `42`
   - D) Random number between 1 and 10

**23. What does `isinstance(x, int)` check?**
   - A) If x is an integer type
   - B) If x equals an integer
   - C) If x is greater than an integer
   - D) If x can be converted to an integer

**24. How would you find the index of the first occurrence of a value in a list?**
   ```python
   fruits = ['apple', 'banana', 'cherry', 'banana']
   index = fruits.index('banana')
   ```
   - A) `0`
   - B) `1`
   - C) `3`
   - D) Error

**25. What is the result of the following code?**
   ```python
   text = "Python is fun"
   word_count = len(text.split())
   print(word_count)
   ```
   - A) `13`
   - B) `3`
   - C) `14`
   - D) Error

---

## Advanced Quiz Answer Key

| Q | Answer | Q | Answer | Q | Answer |
|---|--------|---|--------|---|--------|
| 1 | A | 9 | B | 17 | C |
| 2 | C | 10 | B | 18 | B |
| 3 | B | 11 | A | 19 | A |
| 4 | C | 12 | C | 20 | B |
| 5 | B | 13 | A | 21 | B |
| 6 | A | 14 | B | 22 | B |
| 7 | C | 15 | B | 23 | A |
| 8 | A | 16 | C | 24 | B |
|  |  |  |  | 25 | B |

## Python Dictionaries Quiz

### Question 1: What will be the output of the following code?

```python
my_dict = {"name": "Alice", "age": 25}
print(my_dict["name"])
```

a) Alice  
b) 25  
c) KeyError  

---

### Question 2: What will happen if you try to access a key that doesn't exist in the dictionary?

```python
my_dict = {"name": "Bob"}
print(my_dict["age"])
```

a) None  
b) KeyError  
c) 0  

---

### Question 3: How can you add a new entry to a dictionary?

```python
my_dict = {}
my_dict["color"] = "blue"
print(my_dict)
```

a) {}  
b) {"color": "blue"}  
c) KeyError  

---

### Question 4: What does this code do?

```python
my_dict = {"name": "Charlie"}
my_dict["name"] = "David"
print(my_dict)
```

a) {"name": "Charlie"}  
b) {"name": "David"}  
c) KeyError  

---

### Question 5: What will be the output after executing this code?

```python
my_dict = {"a": 1, "b": 2, "c": 3}
del my_dict["b"]
print(my_dict)
```

a) {"a": 1, "b": 2, "c": 3}  
b) {"a": 1, "c": 3}  
c) KeyError  

---

### Question 6: What will this code print?

```python
my_dict = {"x": 100, "y": 200}
for key in my_dict:
    print(key)
```

a) 100 200  
b) x y  
c) {'x': 100, 'y': 200}  

---

### Question 7: How do you loop through both keys and values in a dictionary?

```python
my_dict = {"name": "Eve", "age": 30}
for key, value in my_dict.items():
    print(key, value)
```

a) Only keys  
b) Only values  
c) Both keys and values  

---

### Question 8: What will be the result of the following code?

```python
my_dict = {"a": 1, "b": 2}
print(my_dict.get("b"))
```

a) 1  
b) 2  
c) KeyError  

---

### Question 9: How can you check if a key exists in a dictionary?

```python
my_dict = {"name": "Frank"}
if "name" in my_dict:
    print("Exists")
else:
    print("Does not exist")
```

a) Exists  
b) Does not exist  
c) KeyError  

---

### Question 10: What will be the output of this code?

```python
my_dict = {"one": 1, "two": 2}
for value in my_dict.values():
    print(value)
```

a) one two  
b) 1 2  
c) {'one': 1, 'two': 2}  

---

### Question 11: What does the following code do?

```python
my_dict = {"item": "pen", "quantity": 10}
del my_dict["quantity"]
print(my_dict)
```

a) {"item": "pen", "quantity": 10}  
b) {"item": "pen"}  
c) KeyError  

---

### Question 12: What will the following code print?

```python
my_dict = {"name": "Grace", "age": 28}
my_dict["age"] += 1
print(my_dict["age"])
```

a) 28  
b) 29  
c) KeyError  

---

### Question 13: What will this code output?

```python
my_dict = {"a": 1, "b": 2, "c": 3}
print(len(my_dict))
```

a) 2  
b) 3  
c) KeyError  

---

### Question 14: What does this code output?

```python
person = {"name": "Helen", "age": 22}
person["city"] = "Paris"
print(person)
```

a) {"name": "Helen", "age": 22}  
b) {"name": "Helen", "age": 22, "city": "Paris"}  
c) KeyError  

---

### Question 15: What is the output of this code?

```python
my_dict = {"key": "value"}
my_dict["new_key"] = "new_value"
print(my_dict.items())
```

a) dict_items([('key', 'value')])  
b) dict_items([('key', 'value'), ('new_key', 'new_value')])

## Python While Loop Quiz

### Question 1: What will be printed by this code?

```python
count = 0
while count < 3:
    print(count)
    count += 1
```

a) 0 1  
b) 0 1 2  
c) 1 2 3  

---

### Question 2: What will happen when the following code runs?

```python
x = 5
while x > 0:
    print(x)
    x -= 1
```

a) It will print 5, 4, 3, 2, 1  
b) It will print 4, 3, 2, 1, 0  
c) It will result in an infinite loop  

---

### Question 3: How many times will the following loop execute?

```python
i = 0
while i < 5:
    i += 1
```

a) 4  
b) 5  
c) 6  

---

### Question 4: What will be the output of this code?

```python
n = 2
while n < 10:
    n += 2
print(n)
```

a) 8  
b) 10  
c) 12  

---

### Question 5: What does this code do?

```python
counter = 0
while counter < 3:
    print("Hello")
    counter += 1
```

a) Prints "Hello" 3 times  
b) Prints "Goodbye"  
c) Causes an infinite loop  

---

### Question 6: What will be printed by the following code?

```python
y = 1
while y <= 5:
    if y == 3:
        break
    print(y)
    y += 1
```

a) 1 2 3  
b) 1 2  
c) 1 2 3 4 5  

---

### Question 7: What will the output be for the following code?

```python
a = 0
while a < 3:
    a += 1
print(a)
```

a) 0  
b) 2  
c) 3  

---

### Question 8: What will happen if this code is executed?

```python
count = 3
while count > 0:
    print("Count:", count)
    count -= 1
else:
    print("Done")
```

a) Count: 3 Count: 2 Count: 1 Done  
b) Count: 3 Count: 2 Count: 1
c) Infinite loop  

---

### Question 9: In the following code, what is the value of `x` after loop execution?

```python
x = 0
while x < 5:
    x += 1
    if x == 3:
        continue
    print(x)
```

a) 1 2 3 4 5  
b) 1 2 4 5  
c) 3 4 5  

---

### Question 10: What will this code output?

```python
n = 0
while n < 2:
    print("Python")
    n += 1
print("Done")
```

a) Python Done  
b) Python Python Done  
c) Done  

---

### Answers

1. b) 0 1 2
2. a) It will print 5, 4, 3, 2, 1
3. b) 5
4. b) 10
5. a) Prints "Hello" 3 times
6. b) 1 2
7. c) 3
8. a) Count: 3 Count: 2 Count: 1 Done
9. b) 1 2 4 5
10. b) Python Python Done

## Python Functions Quiz

### Question 1: What will be the output of the following code?

```python
def add(a, b):
    return a + b

print(add(3, 5))
```

a) 8  
b) 35  
c) Error  

---

### Question 2: How do you define a function with default values for parameters?

```python
def multiply(a, b=2):
    return a * b
```

What will `multiply(3)` return?
a) 6  
b) 3  
c) Error  

---

### Question 3: What will this code output?

```python
def subtract(a, b):
    return a - b

print(subtract(b=5, a=10))
```

a) 5  
b) 15  
c) Error  

---

### Question 4: What is the result of executing this function call?

```python
def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

display_info(age=25, name="Alice")
```

a) Name: Alice, Age: 25  
b) Name: 25, Age: Alice  
c) Error  

---

### Question 5: What will be printed by this code snippet?

```python
def greet(name="User"):
    print(f"Hello, {name}!")

greet()
```

a) Hello!  
b) Hello, User!  
c) Hello, None!  

---

### Question 6: What does the following function do?

```python
def power(base, exponent):
    return base ** exponent
```

What will `power(2, 3)` return?
a) 5  
b) 6  
c) 8  

---

### Question 7: What is the output of this code?

```python
def calculate(a, b=10, c=5):
    return a + b + c

print(calculate(2))
```

a) 7  
b) 12  
c) 17  

---

### Question 8: How can you pass an arbitrary number of arguments to a function?

```python
def print_all(*args):
    for arg in args:
        print(arg)
```

What can `print_all(1, 2, 3)` do?
a) Print each argument  
b) Return a tuple  
c) Both a and b  

---

### Question 9: What will be the output of the following code?

```python
def add(a, b=5, c=3):
    return a + b + c

print(add(2, c=10))
```

a) 15  
b) 12  
c) Error  

---

### Question 10: In the following code, what is returned?

```python
def get_full_name(first, last):
    return f"{first} {last}"

print(get_full_name(last="Smith", first="John"))
```

a) John Smith  
b) Smith John  
c) Error  

---

### Question 11: How many parameters does this function have?

```python
def example(a, b=2, *args, **kwargs):
    pass
```

a) 2  
b) 4  
c) 3  

---

### Question 12: What will this code print?

```python
def divisor(x):
    return 10 / x

print(divisor(2))
```

a) 2  
b) 5  
c) 20  

---

### Question 13: What will be the output of this function?

```python
def func(x, y=1, z=2):
    return x + y + z

print(func(3, z=4))
```

a) 8  
b) 9  
c) 10  

---

### Question 14: What does the following code do?

```python
def counter(n=0):
    while n < 5:
        print(n)
        n += 1

counter()
```

a) Prints 0 to 4  
b) Prints 1 to 5  
c) Prints 1 to 4  

---

### Question 15: What will this code output?

```python
def calculate_total(price, tax=0.05):
    return price + (price * tax)

print(calculate_total(100))
```

a) 105  
b) 100  
c) 95  

---

### Question 16: In this code, how many arguments does `my_func` take?

```python
def my_func(a, *args, **kwargs):
    pass
```

a) Variable arguments  
b) Two arguments  
c) One positional argument  

---

### Question 17: What will be printed by the following code?

```python
def info(name, age=20):
    print(f"Name: {name}, Age: {age}")

info("Alice", 25)
```

a) Name: Alice, Age: 20  
b) Name: Alice, Age: 25  
c) Error  

---

### Question 18: How can you call a function with keyword arguments?

```python
def book(title, author):
    print(f"{title} by {author}")

book(author="J.K. Rowling", title="Harry Potter")
```

What will be printed?
a) Harry Potter by J.K. Rowling  
b) Error  
c) J.K. Rowling by Harry Potter  

---

### Question 19: What will this code output?

```python
def print_multiple(*args):
    for arg in args:
        print(arg)

print_multiple("Hello", "World", 123)
```

a) Hello World 123  
b) Error  
c) Hello\nWorld\n123  

---

### Question 20: What does the following code return?

```python
def function_example(x):
    return x * 2

result = function_example(5)
print(result)
```

a) 10  
b) 5  
c) Error  

---

### Answers

1. a) 8
2. a) 6
3. a) 5
4. a) Name: Alice, Age: 25
5. b) Hello, User!
6. c) 8
7. b) 12
8. c) Both a and b
9. a) 15
10. a) John Smith
11. c) 3
12. b) 5
13. b) 9
14. a) Prints 0 to 4
15. a) 105
16. a) Variable arguments
17. b) Name: Alice, Age: 25
18. a) Harry Potter by J.K. Rowling
19. c) Hello\nWorld\n123
20. a) 10

## Python Scopes Quiz

### Question 1: What will be the output of the following code?
```python
x = "global"

def my_function():
    print(x)

my_function()
```
a) global  
b) Error  
c) None  

---

### Question 2: What will happen if you try to access a variable defined inside a function from the global scope?
```python
def my_function():
    y = "local"
    
my_function()
print(y)
```
a) local  
b) None  
c) Error  

---

### Question 3: In the following code, which variable is being modified?
```python
x = 10

def my_function():
    global x
    x += 5

my_function()
print(x)
```
a) Local `x`  
b) Global `x`  
c) None  

---

### Question 4: What will be printed by the following code?
```python
def outer_function():
    a = "outer"

    def inner_function():
        nonlocal a
        a = "inner"

    inner_function()
    return a

print(outer_function())
```
a) outer  
b) inner  
c) Error  

---

### Question 5: What is the scope of the variable `z` in this code?
```python
def test():
    z = 5
    return z

print(z)  # This will try to access z
```
a) Local to `test()`  
b) Global  
c) Error  

---

### Question 6: What will the below code output?
```python
def my_function():
    global x
    x = 15

my_function()
print(x)
```
a) 15  
b) 0  
c) Error  

---

### Question 7: In the following code, which `a` will be printed?
```python
a = 1

def my_function():
    a = 2
    print(a)

my_function()
print(a)
```
a) 1  
b) 2  
c) Both values  

---

### Question 8: What will be the output of this code?
```python
def outer():
    outer_var = "outer"

    def inner():
        nonlocal outer_var
        outer_var = "inner"
    
    inner()
    return outer_var

print(outer())
```
a) outer  
b) inner  
c) Error  

---

### Question 9: What is the purpose of the `nonlocal` keyword?
a) To declare a variable as global  
b) To refer to a variable in the nearest enclosing scope  
c) To define a module-level variable  

---

### Question 10: What will happen if you run this code?
```python
def func():
    x = 5
    def inner_func():
        return x + 1
    return inner_func()

print(func())
```
a) 6  
b) 5  
c) Error  

---

### Answers:
1. a) global
2. c) Error
3. b) Global `x`
4. b) inner
5. c) Error
6. a) 15
7. b) 2
8. b) inner
9. b) To refer to a variable in the nearest enclosing scope
10. a) 6

## Python Map, Filter, and Reduce Quiz

### Question 1: What does the `map` function do in Python?
a) Transforms a list into a dictionary  
b) Applies a function to every item in an iterable  
c) Filters items from an iterable  

---

### Question 2: What will be the output of the following code?
```python
numbers = [1, 2, 3]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)
```
a) [1, 4, 9]  
b) [1, 2, 3]  
c) [2, 4, 6]  

---

### Question 3: What is the main purpose of the `filter` function?
a) To remove elements from a list  
b) To apply a function and return items that evaluate to True  
c) To sort a list  

---

### Question 4: What will this code output?
```python
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
```
a) [1, 3, 5]  
b) [2, 4]  
c) [1, 2, 3]  

---

### Question 5: What does the `reduce` function do?
a) Reduces the number of elements in a list to one  
b) Applies a binary function cumulatively to the items of an iterable  
c) Filters items in an iterable  

---

### Question 6: What will be the output of this code?
```python
from functools import reduce

result = reduce(lambda x, y: x + y, [1, 2, 3, 4])
print(result)
```
a) 10  
b) 24  
c) 12  

---

### Question 7: Which of the following will return the sum of a list using `reduce`?
```python
from functools import reduce
numbers = [1, 2, 3, 4]
```
a) 
```python
reduce(sum, numbers)
```
b) 
```python
reduce(lambda x, y: x + y, numbers)
```
c) 
```python
map(lambda x: x + 1, numbers)
```  

---

### Question 8: What will be the output of the following code snippet?
```python
names = ["alice", "bob", "charlie"]
capitalized_names = list(map(str.capitalize, names))
print(capitalized_names)
```
a) ['Alice', 'Bob', 'Charlie']  
b) ['ALICE', 'BOB', 'CHARLIE']  
c) ['alice', 'bob', 'charlie']  

---

### Question 9: If you want to filter out odd numbers from a list, which of the following would be correct?
```python
numbers = [1, 2, 3, 4, 5]
```
a) 
```python
filter(lambda x: x % 2 == 1, numbers)
```
b) 
```python
filter(lambda x: x % 2 == 0, numbers)
```  
c) 
```python
map(lambda x: x % 2 == 0, numbers)
```  

---

### Question 10: What will the following code print?
```python
numbers = [0, 1, 2]
result = list(map(lambda x: x > 0, numbers))
print(result)
```
a) [False, True, True]  
b) [0, 1, 2]  
c) [True, True, True]  

---

### Question 11: What will be the output of this code?
```python
from functools import reduce

data = [1, 2, 3, 4]
result = reduce(lambda x, y: x * y, data)
print(result)
```
a) 10  
b) 24  
c) 6  

---

### Question 12: What does the following code return?
```python
list(filter(None, [0, "", [], {}, 1, "test"]))
```
a) [1, "test"]  
b) [0, "", [], {}, 1, "test"]  
c) [0, 1, "test"]  

---

### Question 13: What does `map` return if you provide it an empty iterable?
a) An empty list  
b) None  
c) An error  

---

### Question 14: What will this code output?
```python
data = ['1', '2', '3']
nums = list(map(int, data))
print(nums)
```
a) [1, 2, 3]  
b) ['1', '2', '3']  
c) [1, 4, 9]  

---

### Question 15: Combining `filter` and `map`, what will the result of the following code be?
```python
data = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, data)))
print(result)
```
a) [4, 8]  
b) [2, 4, 6, 8, 10]  
c) [8]  

---

### Answers:
1. b) Applies a function to every item in an iterable
2. a) [1, 4, 9]
3. b) To apply a function and return items that evaluate to True
4. b) [2, 4]
5. b) Applies a binary function cumulatively to the items of an iterable
6. a) 10
7. b) 
```python
reduce(lambda x, y: x + y, numbers)
```
8. a) ['Alice', 'Bob', 'Charlie']
9. b) 
```python
filter(lambda x: x % 2 == 0, numbers)
```
10. a) [False, True, True]
11. b) 24
12. a) [1, "test"]
13. a) An empty list
14. a) [1, 2, 3]
15. a) [4, 8]

## Object-Oriented Programming (OOP) Quiz

### Question 1: What is a class in Python?

a) A blueprint for creating objects  
b) A built-in data type  
c) A function definition  

---

### Question 2: What is an object in OOP?

a) An instance of a class  
b) A type of variable  
c) A function that belongs to a class  

---

### Question 3: How do you create a class in Python?

```python
class MyClass:
    pass
```

a) MyClass()  
b) class MyClass()  
c) class MyClass:  

---

### Question 4: Which keyword is used to define a method within a class?

a) def  
b) function  
c) method  

---

### Question 5: What is an instance attribute?

a) A variable defined within a class  
b) A variable defined within an instance of a class  
c) A variable that belongs to the class itself  

---

### Question 6: What will the following code output?

```python
class Car:
    def __init__(self, make):
        self.make = make

my_car = Car("Toyota")
print(my_car.make)
```

a) Car  
b) make  
c) Toyota  

---

### Question 7: What does `self` refer to in a class?

a) The class itself  
b) The instance of the class  
c) A static variable  

---

### Question 8: How do you call an instance method?

```python
class Dog:
    def bark(self):
        return "Woof!"
```

What is the correct way to call the `bark` method on an instance `my_dog`?
a) Dog.bark()  
b) my_dog.bark()  
c) bark(my_dog)  

---

### Question 9: What is a static method?

a) A method that depends on instance variables  
b) A method that belongs to the class rather than an instance  
c) A method that changes the state of an instance  

---

### Question 10: What will be the output of the following code?

```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(5, 3))
```

a) 8  
b) 5  
c) Error  

---

### Answers

1. a) A blueprint for creating objects
2. a) An instance of a class
3. c) class MyClass:
4. a) def
5. b) A variable defined within an instance of a class
6. c) Toyota
7. b) The instance of the class
8. b) my_dog.bark()
9. b) A method that belongs to the class rather than an instance
10. a) 8
