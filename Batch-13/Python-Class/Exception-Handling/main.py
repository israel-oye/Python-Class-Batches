def add(x, y):
    try:
        result = x + y
    except TypeError:
        print("It seems you tried to add text and numbers")
    else:
        return result

add(4, 5)
print(add('4', 5))

# try:
#   soemething that can POTENTIALLY raise an error
# except ErrorName:
#   do sth if the error occurs
# else:
#   do sth if Error wasn't raised