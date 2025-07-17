# #Tuple is immutable means unchangeable. and must use parentheses means first bracket ().

# mytuple = (2,4,5,6, 'kajol','sarker',True)
# print(f"The class type is:{type(mytuple)}:and the tuple is: {mytuple}")     #print the tuple type with its values
# # mytuple[2] = 10                                                           # this line will give an error because tuple is immutable
# # print(mytuple)           

# print(mytuple[-1])          #print the last element of the tuple. we can use + means ascending, - means descending order
# print(mytuple[2:5])         #print the elements from index 2 to 4 (5 is not included)

# #Update Tuple. convert the tuple to a list, update the list value or whatever you want, then convert it back to a tuple,
# #Ekta variable create kore = list(tuple name) korbo, then append/insert/extend korbo. then convert it back to tuple.
# lis = list(mytuple)  #convert tuple to list
# lis[3] = "Md."             #update the 4th element of the list
# lis.append("Good Job")     #append a new value to the list
# mytuple = tuple(lis)       #convert list back to tuple
# print(f"The updated tuple is:{mytuple}")

# #Unpacking a Tuple. ekta tuple er value ba item k different variable a assign kore korake unpacking bole.
# #Two ways to unpack a tuple, with or without asterisk (*).
# (a, b, c, d, e, f, g, h) = mytuple       #unpacking the tuple
# # print(f"The unpacked values are: {a}, {b}, {c}, {d}, {e}, {f}, {g}")
# # print(a)     #print 2
# # print(b)     #print 4
# # print(c)     #print 5 
# # print(d)     #print 6
# # print(e)     #print kajol
# # print(f)     #print sarker
# # print(g)     #print True
# # print(h)     #print Good Job   


# #we can use asterisk (*) to unpack multiple values into a single variable. only * will take all iteams except the last one.
# (*a,) = mytuple   # *a will take all the values except the last one. (a,*b,c) evabe dite  different way te kora jay. FIFO type.
# print(a)    #print all the values except the last one
# print('\n') 


# #Loop Tuples. two ways to loop through a tuple.
# for i in mytuple:          #using for loop 
#     print(i)         #print each element of the tuple
# print('\n')

# for j in range(len(mytuple)):
#     print(mytuple[j])
# print('\n')


# #While loop

# X = 0
# while X < len(mytuple):    #using while loop
#     print(mytuple[X])      #print each element of the tuple
#     X += 1                 #increment the value of X by 1



# #Tuple Joining. we can join two or more tuples using the + operator.
# tuple1 = (1,2,3)
# tuple2 = (4,5,6)
# tuple3 = tuple1 + tuple2  #join two tuples
# print(tuple3)
# #or print (tuple1 + tuple2)  #join two tuples and print it directly

# #Tuple Multiplication. we can multiply a tuple by an integer to repeat its elements.
# print(tuple1 * 5)   #repeat the elements of tuple1 two times



#Tuple Methods. Two methods are available for tuples: count() and index().
#count() method er kaj holo, tuple er modde koto bar kono value ache ta count kore dekhano.
#index() method er kaj holo, tuple er modde kono value ache kina ta check kore, thakle tar index number ta dekhano.

tup = (1,2,5,5,6,7,5,3)
#v1 = tup.count(5)   #count the number of times 5 appears in the tuple
print(tup.count(5))  #print the count of 5 in the tuple
#vs = tup.index(5)   #find the index of the first occurrence of 5 in the tuple
print(tup.index(6))   #print the index of 6 in the tuple




