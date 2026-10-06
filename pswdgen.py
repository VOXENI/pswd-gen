import random
import string

length = int(input("9"))

characters = string.ascii_letters + string.digits + "!@#$%^&*"

password = ""

for _ in range(length):
    password += random.choice(characters)

print("Your password is:", password)