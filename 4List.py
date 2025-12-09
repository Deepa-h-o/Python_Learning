#List - Ordered, Mutable, Allows Duplicates, Indexed

list = [1, 2, 3, 4, 5] #Homogeneous Data Types
list2 = ['a', 'b', 'c', 'd', 'e'] #Homogeneous Data Types
list3 = [1, 'a', 2.5, True, None] #Mixed Data Types
list4 = [] #Empty List

print("Original List:", list)

#Accessing Elements
print("First Element:", list[0])    
print("Last Element:", list[-1])

#Slicing    
print("Sliced List (2nd to 4th):", list[1:4])

#Modifying Elements
list[2] = 10
print("Modified List:", list)

#Adding Elements
list.append(6)
print("List after Append:", list)
list.insert(0, 0)
print("List after Insert at beginning:", list)

#Removing Elements
list.remove(10)
print("List after Removing 10:", list)
popped_element = list.pop()
print("Popped Element:", popped_element)
print("List after Pop:", list)

#List Operations - Matrix
combined_list = list + list2
print("Combined List:", combined_list)
repeated_list = list * 2
print("Repeated List:", repeated_list)

#List Methods
print("Length of List:", len(list))
print("Index of element 4:", list.index(4))
print("Count of element 2:", list.count(2))
list.sort()
print("Sorted List:", list)
list.reverse()
print("Reversed List:", list)

#Iterating through List
print("Iterating through List:")
for item in list:
    print(item)

#Nested Lists
nested_list = [[1, 2], [3, 4], [5, 6]]
print("Nested List:", nested_list)
print("Accessing element 4 from Nested List:", nested_list[1][1])
