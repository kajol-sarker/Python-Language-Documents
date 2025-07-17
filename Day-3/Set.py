# #Set is unorderd,unchangable but we can add or remove items. must use curly brackets {}. Duplicate values are not allowed.
# # create a set like---  variable_name = { int, float,string etc}. 
# my_set = {1,3,True,"Hello","Kajol",False, 0.5}     #create a set
# print(f" The type of the set is:{type(my_set)} and the set is: {my_set}")     #True not print 
# print(len(my_set))
# print("\n")



# #Access set items.# we cannot access set items directly like list or tuple. we can use for loop to access set items.
# #Rules 1
# for items in my_set:
#     print(items)

# #Rules 2
# print("Kajol" in my_set)           # print(value name, in , set name). # it will return True or False.



# #Add Set Item. We can add items using add() and update() method.
# #add () method
# my_set.add("MD.")
# print(my_set)

# #update () method. it is a iterable object means we can add  list, tuple, set, dictionary, string into set.
# my_set2 = {2,4,6,7,8}
# my_set.update(my_set2)     #join two sets
# print(my_set)


# #add  list, tuple, set, dictionary, string into set.
# list= [99,65]
# my_set2.update(list)  #add list into set
# print(my_set2)
# print("\n")

# tuple = (26,25)
# my_set2.update(tuple)  #add tuple into set
# print(my_set2)



# #remove item from set. We can remove items using remove(), discard(), pop(), clear() method.
# #remove() method. It will raise an error if the item is not found.
# my_set.remove("Hello")   #remove item from set
# print(my_set)

# #discard() method. It will not raise an error if the item is not found.
# my_set.discard("Tamanna")  #discard item from set, if item is not found it will not raise an error.
# print(my_set)

# #pop() method. It will remove a random item from the set.
# my_set.pop()    #remove a random item from set, we dont know which item will be removed. no parameter is required.
# print(my_set)

# #clear() method. It will remove all items from the set.
# my_set.clear()
# print(my_set)      #clear() method. It will remove all items from the set.



# #Loop for set.
# for kajol in my_set2:
#     print(kajol)



#Join two sets. We can join two sets using union() method or update() method. and many more methods.
set1 = {1,2,3,4,5}
set2 = {6,7,8,9,10}
#union() method. It will return a new set that contains all items from both sets.
set3 = set1.union(set2)   #join two sets using union() method
print(set3)
#update() method. It will add all items from set2 to set1.
set1.update(set2)
print(set1)  #set1 is updated with set2 items.