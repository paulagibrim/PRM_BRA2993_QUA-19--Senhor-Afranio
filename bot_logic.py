import random


def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

# password = gen_pass(10)
# print(password)