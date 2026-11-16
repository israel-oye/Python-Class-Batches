# values = [5, 10, 15, 20, 25]

# palindrome_values = values[:4] + values[-1:]

# print

mon = {"John", "Mary", "Steve"}
tues = {"Mary", "Steve", "Sam"}

attended_both_days = mon & tues

print(attended_both_days)

attended_only_one_day = mon.symmetric_difference(tues)

print(attended_only_one_day)

print(mon | tues)

