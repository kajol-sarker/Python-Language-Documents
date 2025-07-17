
"""
Built-in Data Types
Variables can store data of different types, and different types can do different things.
Python has the following data types:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""

modhu = 'Md.Kajol Sarker'  # string type /text type data with single or double quotes
print(modhu)
print("My Name is:" + ' ' + modhu)

kodu1 = 'string'
kodu_1 = 'string'
# 1kodu = 'string'  not allowed
print(kodu_1)
print(kodu1)


#String Formatting
num1 = 10
num2 = 10
print(f"The sum of these value is: {num1 + num2} ")  #Concatenation of string and variable value.
# use f in print function to format string with variable value with {} carle bracket.


#Setting the Data Type
a = "Hello World"	
b = 20	
c = 20.5		
d = 1j		
e = ["apple", "banana", "cherry"]		
f = ("apple", "banana", "cherry")		
g = range(6)	
h = {"name" : "John", "age" : 36}		
i = {"apple", "banana", "cherry"}	
j = frozenset({"apple", "banana", "cherry"})		
k = True	
l = b"Hello"		
m = bytearray(5)		
n = memoryview(bytes(5))	
o = None	

print(type(a))  # <class 'str'>
print(type(b))  # <class 'int'>
print(type(c))  # <class 'float'>
print(type(d))  # <class 'complex'> 
print(type(e))  # <class 'list'>
print(type(f))  # <class 'tuple'>
print(type(g))  # <class 'range'>
print(type(h))  # <class 'dict'>    
print(type(i))  # <class 'set'>
print(type(j))  # <class 'frozenset'>
print(type(k))  # <class 'bool'>
print(type(l))  # <class 'bytes'>
print(type(m))  # <class 'bytearray'>
print(type(n))  # <class 'memoryview
print(type(o))  # <class 'NoneType'>



#Setting the Specific Data Type
a = str("Hello World")	
b = int(20)	
c = float(20.5)		
d = complex(1j)		
e = list(("apple", "banana", "cherry"))	
f = tuple(("apple", "banana", "cherry"))		
g = range(6)	
h = dict(name="John", age=36)		
i = set(("apple", "banana", "cherry"))	
j = frozenset(("apple", "banana", "cherry"))		
k = bool(5)	
l = b"Hello"		
m = bytes(5)		
n = bytearray(5)
o = memoryview(bytes(5))	

print(a)  # Hello World
print(b)  # 20
print(c)  # 20.5
print(d)  # 0j
print(e)  # ['apple', 'banana', 'cherry']
print(f)  # ('apple', 'banana', 'cherry')
print(g)  # range(0, 6)
print(h)  # {'name': 'John', 'age': 36}
print(i)  # {'apple', 'banana', 'cherry'}
print(j)  # frozenset({'apple', 'banana', 'cherry'})
print(k)  # True
print(l)  # b'Hello'
print(m)  # b'\x00\x00\x00\x00\x00'
print(n)  # bytearray(b'\x00\x00\x00\x00\x00')
print(o)  # <memory at 0x7f8c1c0b



#Boolean Data Type
x = True
y = False
a = 5
b = 10

print(x)  # True
print(y)  # False
print(a > b)  # False
print(a < b)  # True
print(type(x))  # <class 'bool'>
print(type(y))  # <class 'bool'>
print(type(a))  # <class 'int'>
print(type(b))  # <class 'int'>



#byte Type Data
#bytes. It is immutable, means not changeable.
list = [1, 2, 3, 4, 5,255]     #byte or byte array size is 0 to 255.so this list can to not store more than 255.
con = bytes(list)              #Convert list to bytes
# b[0] = 10                    # This will raise an error because bytes are immutable.
print(f" {type(con)} : {con}")                
#image related data is stored in bytes format.


#bytearray. It is mutable, means changeable.
list1 = [1, 2, 3, 4, 5, 255]
con1 = bytearray(list1)         #Convert list to bytearray
con1[0] = 100
print(con1[0])
print (type(con1))


#List type data
lis = [1, 2, 3, 4, 5, 255]  #List is mutable, means changeable. it is under third  bracket [].
print(f" {type(lis)}: {lis}")
lis1 = ["kajol", "kawser","kakon","Mina", "Rafiqul"]
print(f"{type(lis1)}: {lis1}")
# we can check index of list, we can change the value of list, we can add new value in list, we can remove value from list.
# print(lis1[0])  #Accessing the first element of the list
# lis1[0] = "Kajol Sarker"  #Changing the first element
# lis1.append("New Name")  #Adding a new element to the list
# lis1.remove("Mina")  #Removing an element from the list
# print(lis1)  #Printing the modified list


#Tuple type data
#Tuple is immutable, means not changeable. it is under first bracket ().    
tup = (1, 2, 3, 4, 5, 255)
print(f" {type(tup)}: {tup}")
tup1 = ("kajol", "kawser", "kakon", "Mina", "Rafiqul")
print(f"{type(tup1)}: {tup1}")
#we can check index of tuple, we can not change the value of tuple, we can not add new value in tuple, we can not remove value from tuple.
# print(tup1[0])  #Accessing the first element of the tuple
# print(tup1[0] + " Sarker")  #Concatenating a string to the first element of the tuple


#Rage type data
#Range is used to generate a sequence of numbers. It is under range() function.
ran = range(10)  # Generates numbers from 1 to 9
for i in ran:
    print(i)
#print(f" {type(ran)}: {ran}")# Prints the type and the range object
