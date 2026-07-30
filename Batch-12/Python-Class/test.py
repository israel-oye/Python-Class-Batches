def my_function():
    global x
    x = 15


my_function()
print(x)

import threading
import time
from string import ascii_uppercase

numbers = list(range(1, 10))
alphabets = list(ascii_uppercase)[:10]

def print_numbers():
    for i in numbers:
        print(i)
        time.sleep(1)

def print_alphabets():
    for char in alphabets:
        print(char)
        time.sleep(1)

# st = time.perf_counter()
# print_numbers()
# print_alphabets()
# end = time.perf_counter()

# print(f"Time taken: {end - st}")


t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_alphabets)

st = time.perf_counter()
t1.start()
t2.start()
end = time.perf_counter()

t1.join()
t2.join()

if not t1.is_alive() and not t2.is_alive():
    print(f"Time taken: {end - st:.2f}")
# t1.join()