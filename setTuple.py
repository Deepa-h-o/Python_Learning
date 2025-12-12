'''Tuple and Set Comparison:

Create a list of elements and convert it into both a tuple and a set.
Print both the tuple and the set.
Try to add new elements to the tuple and set. What differences do you observe?
'''

print("Create a list of elements and convert it into both a tuple and a set.")
list = [1,2,3,4,"six"]
tuple = tuple(list)
set = set(list)
print(tuple)
print(type(tuple))
print(set)

list[1] = "kiwi"
print(list)
tuple1 = tuple(list)
set1 = set(list)
print(tuple1)
print(type(tuple1))
print(set1)

