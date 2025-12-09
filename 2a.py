print('hello world')
print("hello World")

#Quote inside single quote
print("Quote inside single quote")
print("He is called 'Johnny'")

#Multiline string
print("\n")
print("Multiline string")
a = """Lorem ipsum dolor sit amet
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


#String array
print()
print("String array")
a="hello world"
print(a[1])
print(len(a)) 

#String in Loop
print()
print("String in Loop")
for x in "banana":
    print(x)

#Check String
print()
print("Check String")
txt = "I love you manu"
print("manu" in txt) 
if "ninu" in txt:
    print("Yes, 'manu' is present.")
else:
    print("No, 'manu' is not present.")        

#Modify String
print()
A= "Deepu "
print(A.upper())
print(A.lower()) 
print(A.strip())
print(A.replace("D", "J"))  
print(A.split("e"))

#String formatting
print()
print("String formatting")
age = 36
tx = "my name deepu", age  ,"years old"
print(tx)

age = 37
tx = "my name deepu " + str(age) + " years old"
print(tx)

age= 38
txt = f"My name is Deepu,{age} years old"
print(txt)

#String methods
print()
print("String methods")
txt = "hello world deepu"
print(txt.capitalize())
print(txt.casefold())
print(txt.center(20))
print(txt.count("o"))
print(txt.encode())
print(txt.endswith("depu"))
tx = "He\tllo\tWorl\td!"
print(tx.expandtabs(10))
print(txt.find("r"))