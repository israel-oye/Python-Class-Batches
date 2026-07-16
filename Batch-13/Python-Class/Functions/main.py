# # username = input("Name: ")
# # print(f"Hello {username}")

# def greet_person(name):
#     print(f"Hello {name}")


# greet_person("Oba")
# greet_person("Akeem")
# greet_person("Feyi")
# greet_person(name="Dammy")

# for name in ['Dele', 'Elisa', 'Fridolfo']:
#     greet_person(name)


# def favorite_book(title):
#     print(f"One of my favourite books is {title.title()}")

# favorite_book("Things fall apart")
# favorite_book(title="In Dependence")


# def simple_func():
#     print("This is a parameterless function")


# # simple_func()

# def describe_pet(animal_type, name):
#     print(f"I have a/an {animal_type} named {name}")

# describe_pet("dog", "Bullet")


# def custom_range(start, step=1):
#     pass

# for j in custom_range():
#     pass

students = [
    {"name": "Alice", "grade": 92.5},
    {"name": "Bob", "grade": 78.0},
    {"name": "Charlie", "grade": 88.5},
    {"name": "David", "grade": 65.0},
    {"name": "Eve", "grade": 95.0},
]

def is_above_85(student: dict):
    return student['grade'] > 85

students_above_85 = list(filter(is_above_85, students))
print(students_above_85)