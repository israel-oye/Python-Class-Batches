# from package_2.main import description

# from ..input_class import team_name
# from ..package_2.main import description
# from my_package import operators
import random as eyije_eyi_oje

from operators import add as adding_machine
from operators import divide

eyije_eyi_oje.randint(1, 10)


def calculator(func, *operands):
    return func(*operands)

user_entry = input("Choose an operation\n 1. Add 2. Divide")
operand_a = int(input("Enter a first number: "))
operand_b = int(input("Enter second number: "))

if user_entry == '1':
    print(calculator(adding_machine, 2, 3))
elif user_entry == '2':
    print(calculator(divide, operand_a, operand_b))
# print("Running in calculator module")
# print(__name__)
# print(__name__)
