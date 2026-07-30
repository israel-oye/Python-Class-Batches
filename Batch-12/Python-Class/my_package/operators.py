def add(*operands):
    return sum(operands)

def divide(a, b):
    return a / b


if __name__ == "__main__":
    print(add(10, 5))
    print("Running in operators module")
    print(__name__)
