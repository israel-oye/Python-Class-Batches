# def greet_person(country='World', person="Lagbaja"):
#     print(f"Hello {person} from {country}")


# greet_person('Jamaica', 'Tim')

# greet_person('Luxembourg')

# greet_person()

def foo():
    print('Fooo..')


foo_copy = foo

# foo_copy()

bar = lambda: print("Bar...")
bar()

# bar = def ():
#           return print("Bar...")

def double(x: int):
    return x * 2

double_ = lambda x: x * 2
print(double(8))
print(double_(4))

# Higher Order Functions
# g(f)

def executor(f):
    print("Executing function...")
    # print(f)
    f()


executor(f=foo)
executor(f=bar)
executor(f=lambda: print('Anon function...'))