import random
import string

length = int(input("Enter the desired password length: "))

letters = input("Include letters? (y/n): ").lower()
digits = input("Include digits? (y/n): ").lower() 
special = input("Include special characters? (y/n): ").lower()

characters= ""

if letters == 'y':
    characters += string.ascii_letters
if digits == 'y':
    characters += string.digits
if special == 'y':
    characters += string.punctuation

if not characters:
    print("No character types selected. Cannot generate password.")
    exit()

password = ''.join(random.choice(characters) for _ in range(length))
print(f"Generated password: {password}")
