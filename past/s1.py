# import random
# frequency_1 = 0
# frequency_2 = 0
# frequency_3 = 0
# frequency_4 = 0
# frequency_5 = 0
# frequency_6 = 0
# for i in range(10_000):
#     face = random.randint(1, 6)
#     if face == 1:
#         frequency_1 += 1
#     elif face == 2:
#         frequency_2 += 1
#     elif face == 3:
#         frequency_3 += 1
#     elif face == 4:
#         frequency_4 += 1
#     elif face == 5:
#         frequency_5 += 1
#     elif face == 6:
#         frequency_6 += 1
#     if i % 1_000_000 == 0:
#         print("..."*10)
# print("Face\tFrequency")
# print(f"1\t{frequency_1}")
# print(f"2\t{frequency_2}")
# print(f"3\t{frequency_3}")
# print(f"4\t{frequency_4}")
# print(f"5\t{frequency_5}")
# print(f"6\t{frequency_6}")


# frequency = {
#     1:0,
#     2:0,
#     3:0,
#     4:0,
#     5:0,
#     6:0,
# }
# for i in range(10_000):
#     face = random.randint(1,6)
#     if face == 1:
#         frequency[1] += 1
#     elif face == 2:
#         frequency[2] += 1
#     elif face == 3:
#         frequency[3] += 1
#     elif face == 4:
#         frequency[4] += 1
#     elif face == 5:
#         frequency[5] += 1
#     elif face == 6:
#         frequency[6] += 1


"""
get_cost_of_coffee(7, 2) => 14
get_cost_of_coffee(8, 2) => 16
get_cost_of_coffee(9, 2) => 16
get_cost_of_coffee(10, 2) => 18
"""


# def get_cost_of_coffee(numbers_of_coffee, price_per_coffee):
#     number_of_free_coffee = numbers_of_coffee // 9
#     number_of_paid_coffee = numbers_of_coffee - number_of_free_coffee
#     return number_of_paid_coffee * price_per_coffee

# print(get_cost_of_coffee(7, 2))
# print(get_cost_of_coffee(8, 2))
# print(get_cost_of_coffee(9, 2))
# print(get_cost_of_coffee(10, 2))


import random
import string

LOWER_CASE_LETTERS = string.ascii_lowercase
UPPERS_CASE_LETTERS = string.ascii_uppercase
NUMBERS = string.digits
SPECIAL = '~!@#$%^&*()_+'
ALL_CHARS = LOWER_CASE_LETTERS + UPPERS_CASE_LETTERS + NUMBERS + SPECIAL


def generate_password(length):
    if length < 12:
        length = 12

    password = []
    password.append(LOWER_CASE_LETTERS[random.randint(0, 25)])
    password.append(UPPERS_CASE_LETTERS[random.randint(0, 25)])
    password.append(NUMBERS[random.randint(0, 9)])
    password.append(SPECIAL[random.randint(0, 12)])

    while len(password) < length:
        password.append(ALL_CHARS[random.randint(0, 74)])

    random.shuffle(password)

    return password


print(generate_password(13))
