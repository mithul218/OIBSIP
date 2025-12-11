import random
import string

length = int(input("Enter the desired password length: "))

include_letters = input("Include letters? (y/n): ").lower() == 'y'
include_digits = input("Include digits? (y/n): ").lower() == 'y'
include_special = input("Include special characters? (y/n): ").lower() == 'y'

character_pool = ""

if include_letters:
    character_pool += string.ascii_letters
if include_digits:
    character_pool += string.digits
if include_special:
    character_pool += string.punctuation

if not character_pool:
    print("No character types selected. Cannot generate password.")
    exit()

password = ''.join(random.choice(character_pool) for _ in range(length))
print(f"Generated password: {password}")