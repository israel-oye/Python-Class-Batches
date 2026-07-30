attempts = 3
password = "Password123"

while attempts > 0:
    user_password = input("Enter your password: ").strip()
    attempts -= 1


    if user_password != password:
        if attempts == 0:
            print("You're out of attempts")
            break
        print(f"Invalid password. You have {attempts} trials left before you're locked\n")
    else:
        print("Login success! ✅")
        break
        