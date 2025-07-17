#Python List/Array Methods:
# Python has a set of built-in methods that you can use on lists/arrays.

# Method	  Description
# append()	  Adds an element at the end of the list
# clear()	  Removes all the elements from the list
# copy()	  Returns a copy of the list
# count()	  Returns the number of elements with the specified value
# extend()	  Add the elements of a list (or any iterable), to the end of the current list
# index()	  Returns the index of the first element with the specified value
# insert()	  Adds an element at the specified position
# pop()	      Removes the element at the specified position
# remove()	  Removes the first item with the specified value
# reverse()	  Reverses the order of the list
# sort()	  Sorts the list





list = [1, 2, 3, 4, 5,True, " apple", "banana",False] #create a list. List is a speacial varialble that can store multiple values
print(list) #print the list.
#if we want to print a specific value from the list, we can use index,
print(list[6]) #print the first value from the list. Index starts from 0.
#if you change a specific value in the list, it will change the value in the list.
list[0] = "Hello" #change the first value in the list
print(list) #print the list again to see the change.



list.append("Kajol") #add a new value to the end of the list
print(list) #print the list again to see the change.
list.insert(1, True)
print(list)


#We can remove  values with multiple ways.
list.remove(5) #remove a specific value from the list
print(list) #print the list again to see the change.
list.pop() #remove the last value from the list. in this functin if a specific index is not given, it will remove the last value.
print(list) #print the list again to see the change.
list.clear() #remove all values from the list.
print(list) #print the list again to see the change.
del list[0] #remove a specific value from the list by index. del is a keyword tha is used to delete a value from the list.
print(list) #print the list again to see the change.

#But normal variable can store only one value at a time. So, if you want to store multiple values, you can use list.


#List in Loop. we can use different types of loops--for example
#for loop, while loop, range etc. to iterate through the list and print each value.
thislist = ["kajol", "tamanna", "riva", "sayma"]
for love in thislist:
    print(love)
for i in range(len(thislist)):
    print(i)



# #while loop
x = 0
while x < len(thislist):
    print(thislist[x])
    x += 1



#List Comprehension. This is a way to create a new list by applying an expression to each item in an existing list.
#to create comprehension, we use square brackets. In square brackets [expression(amra ki operation korte chai), Loop, ekta variable a rakhbo, list name]
# add, sub, mult, div, power korte pari, for i in list: print(i / 2) etc. eta comprehension kora.
numbers = [1, 2, 3, 4, 5]
squared = [number ** 2 for number in numbers]  # Create a new list with squared values. when create comprehension, we use square brackets.
print(squared)  # Output: [1, 4, 9, 16, 25]




#List Sorting. We can sort a list in ascending or descending order.
numbers = [5, 2, 9, 1, 5, 6]
print("The original list: ",numbers) 
numbers.sort()  # Sort the list in ascending order by default
print("Sort Them in Ascending Order: ",numbers) 
numbers.sort(reverse=True)  # Sort the list in descending order
print("Sort Them in Descending Order: ",numbers) 



#List copy. We can copy a list to another list.
#manual approach
num1 = [4,5,8,2,9,15,7]
num2 = [4,5,8,2,9,15,7]
print(num1)
print(num2)

#dynamic approach
num2 = num1.copy()  # Create a copy of the list
print(num2)




#Join two different lists. We can join two lists using the + operator.
num3 = [4,5,8,2,9,15,7]
num4 = ['a', 'b', 'c', 'd']
joined_list = num3 + num4  # Join two lists
print("Joined List: ", joined_list)  

#dynamic approach
num3.extend(num4)
print("Extended List: ", num3)  #we can exchane num3 with num4 to extend num4 with num3.