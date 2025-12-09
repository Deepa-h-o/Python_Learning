'''Membership Operator Exercise: Write a Python program that:

Takes a string as input from the user.
Checks if the letter 'a' is in the string (using in).
Checks if the string doesn't contain the word "Python" (using not in).
'''

name = input("Enter your name:" )
if 'a' in name:
    print(f"The letter 'a' is present in your name: {name}")
else:
    print(f"The letter 'a' is not present in your name: {name}  ")

if "Python" not in name:
    print(f"The word 'Python' is not present in your name: {name}")
else:
    print(f"The word 'Python' is present in your name: {name}")    
