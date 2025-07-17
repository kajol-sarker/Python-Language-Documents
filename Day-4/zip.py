#Zip function more than one set, tuple, list, dictionary niye kaj kore. tader k merge kore.
#1st list er 1st item then 2nd list er 1st item k merge korbe. evabe baki gula korbe. 
# zip(iterable1, iterable2, ...)

list1=['kajol','tamanna']
list2=['google','meta']
x= list(zip(list1,list2))
print(x)
print('\n')



names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 22]

# Zipping two lists then convert it into list.
zipped_data = list(zip(names, ages))
print(zipped_data) # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 22)]

# Using zip in a for loop
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")    #string formating

# Unzipping using the * operator
coordinates = [(1, 2), (3, 4), (5, 6)]
x_coords, y_coords = zip(*coordinates)
print(f"X coordinates: {list(x_coords)}") # Output: X coordinates: [1, 3, 5]
print(f"Y coordinates: {list(y_coords)}") # Output: Y coordinates: [2, 4, 6]