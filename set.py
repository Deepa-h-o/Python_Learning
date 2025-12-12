'''Set Operations:

Create two sets: one with your favorite fruits and another with your friend’s favorite fruits.
Find the union, intersection, and difference between the two sets.
Add a new fruit to your set.
Remove a fruit from your set using both remove() and discard(). What happens when the fruit doesn’t exist?
'''

print("Create two sets: one with your favorite fruits and another with your friend’s favorite fruits.")
set = {"mango", "banana", "dragonfruits"}
set1 = {"orange","pineappa","papaya","banana"}

print("Find the union, intersection, and difference between the two sets.")
union = set | set1
print("union:", union)

intersection = set & set1
print("intersectiom:",intersection )

difference = set - set1
print("difference:",difference)
print("\n")
print("Add a new fruit to your set.")
set.add("garden")
print(set)

print("\n")
print("Remove a fruit from your set using both remove() and discard(). What happens when the fruit doesn’t exist?")
set.remove("gar")
set.discard("gar")
print(set)

