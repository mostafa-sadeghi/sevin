# "157"

# 890 => bagels # یعنی هیچ کدام از ارقام درست نیستند
# 321 => Pico # رقم درست است اما جای آن درست نیست

# 521 => Pico Pico

# 123 => Fermi رقم درست است و در جای درست قرار دارد
# 156 => Fermi Fermi

import random
import string


def create_secret_number(num_of_digits=3):
    """
    This function is used to create a 3 digits random number.
    Parameters:
    :num_of_digits : int
    """
    all_digits = list(string.digits)  # ['0', '1', '2', '3', ...., '9']
    random.shuffle(all_digits)
    secret = all_digits[:num_of_digits]
    secret = ''.join(secret)
    return secret


def check_user_guess(user_guess, secret_number):
    if user_guess == secret_number:
        return 'Won'
    res = ''
    for i in range(len(user_guess)):
        if user_guess[i] == secret_number[i]:
            res += "Fermi, "
        elif user_guess[i] in secret_number:
            res += "Pico, "
    if not res:
        return "Bagels"
    return res
    

MAX_GUSSES = 10


# create secret number
secret_number = create_secret_number()
number_of_user_guess = 0
while number_of_user_guess < MAX_GUSSES:
    number_of_user_guess += 1
    print(f"guess number {number_of_user_guess}/{MAX_GUSSES}")
    user_guess = input("Enter a three digits number: ")
    print(check_user_guess(user_guess, secret_number))
    if user_guess == secret_number:
        break

