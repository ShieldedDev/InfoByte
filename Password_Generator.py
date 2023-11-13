# Task 1 - Password Generator in Python - (By Vaibhav Mulak).
import string # Importing the 'string' module for accessing character sets.
import random # Importing the 'random' module for generating random values.

# Defining a function called 'generate_password' that takes a 'length' parameter.
def generate_password(length):
    # Defining character sets
    lowercase_alphabets = string.ascii_lowercase
    uppercase_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    # Combining all character sets.
    combination = lowercase_alphabets + uppercase_alphabets + numbers + special_characters

    # Generating a random password using for loop.
    password = ""# Creating an empty string variable named 'password' to store our password.
    for _ in range(length):
        random_char = random.choice(combination)
        password += random_char

    return password

if __name__ == "__main__":
    # Prompting the user for the desired password length.
    password_length = int(input("Enter the length of the password: "))
    
    # Generating the password using the function generate_password().
    password = generate_password(password_length)
    
    # Displaying the generated password.
    print("Generated Password:", password)