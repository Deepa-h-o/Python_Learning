# Arthimatic, logical,bitwise, relational operators in python
'''Logical Operator Practice: Write a Python program that takes two numbers as input from the user and checks if:

Both numbers are greater than 10 (using and).
At least one of the numbers is less than 5 (using or).
The first number is not greater than the second (using not).
'''
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))

#"Both numbers are greater than 10 (using and).")
print("\n" )
if num1 > 10 and num2 > 10:
    print(f"Both numbers are greater than {num1} {num2} 10")
else:
    print(f"Both numbers are not greater than {num1} {num2} 10") 

print("\nAt least one of the numbers is less than 5 (using or).")
if num1 < 5 or num2 < 5:
    print(f"any one condition meets to make true {num1} {num2} 10")
else:
    print(f"Both numbers are not met condition than {num1} {num2} 10")

#The first number is not greater than the second (using not).    
print("\nThe first number is not greater than the second (using not).")
if not num1 > num2:
    print(f"first number is not greater than second number {num1} {num2}")