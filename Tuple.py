'''Tuple Operations:

Create a tuple with 5 elements.
Try to modify one of the elements. What happens?
Perform slicing on the tuple to extract the second and third elements.
Concatenate the tuple with another tuple.'''

print("Create a tuple with 5 elements.")
tuple = (1,2,3,'deepa','logs')
print(tuple)

print("Try to modify one of the elements. What happens?")
#tuple[1] = 'kiwi'
#print(tuple) # Gives error
x = list(tuple)
print(x)
x[1] = 'kiwi' # Replace
x.append('goods') # add at end
print(x)

print("Perform slicing on the tuple to extract the second and third elements.")
print(x[1:4])

print("Concatenate the tuple with another tuple.")
x2 = (2,3,4,"kiwi")
x3 = ("love","hate")
print(x2 + x3)