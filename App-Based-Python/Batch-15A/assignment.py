# # values = [5, 10, 15, 20, 25]

# # palindrome_values = values[:4] + values[-1:]

# # print

# mon = {"John", "Mary", "Steve"}
# tues = {"Mary", "Steve", "Sam"}

# attended_both_days = mon & tues

# print(attended_both_days)

# attended_only_one_day = mon.symmetric_difference(tues)

# print(attended_only_one_day)

# print(mon | tues)

sentence = "the quick brown fox jumps over the lazy dog"
prices = [1200, 450, 3000, 799, 5600, 150]

words = sentence.split()

words_length = [len(word) for word in words]
print(words_length)

words_starts_with_vowels = [word for word in words if word.startswith(('a', 'e', 'i', 'o', 'u'))]

words_capitalised = [word.capitalize() for word in words]

labels = ['expensive' if p > 1000 else 'cheap' for p in prices]
print(labels)

students = [
    {"name": "Ade", "scores": [70, 85, 90]},
    {"name": "Bola", "scores": [45, 50, 38]},
    {"name": "Chidi", "scores": [88, 92, 79]},
    {"name": "Dayo", "scores": [60, 55, 72]},
]

student_names = [s['name'] for s in students]
print(student_names)

def avg(nums: list):
    return sum(nums) / len(nums)

avg_scores = [avg(s['scores']) for s in students]
print(avg_scores)