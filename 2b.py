''' Simple Greeting Program: Write a Python program that asks the user for their name and age, 
then prints a personalized greeting message. Use both the + operator and f-strings for output.
'''

name = input("Enter your name: ")
age = int(input("enter you age: "))
txt = f"Hello, {name} you are {age} years old correct?"
print(txt)
     
'''String Manipulation Exercise: Write a Python program that:

Takes a sentence as input from the user.
Prints the sentence in all uppercase and lowercase.
Replaces all spaces with underscores.
Removes leading and trailing whitespace.
'''
txt = input("Give some input as hello mmmmm:" )
print(txt.upper())
print(txt.lower())
print(txt.replace(" ", "_"))
print(txt.strip())

#Escape Sequence Practice: Write a Python program that uses escape sequences to print the following 

txt = "hello world!"
print("She said, \"Hello!\"\nWelcome to the world of Python.\tEnjoy coding!")

