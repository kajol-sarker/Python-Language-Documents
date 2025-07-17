#There are two loop in python. For loop & while loop.
#For loop is used to iterate over a sequence (such as a list, tuple, dictionary) we know the iteration number.
#while loop is use to we don't know the iteratin number.For loop is faster than while loop.

# kajol = 1

# while kajol > 0:
#     print("Kajol 0 theke Boro.")
#     kajol = kajol - 1



kajol = 0

while kajol < 5:
    print("Kajol 0 theke choto", kajol)
    kajol = kajol + 1


print('\n')

#For loop. first we need to create a list, tuple, set, dictionary. then put it into for loop.
fruits =[99,'Tamanna',True,165,'Kajol',True]
for i in fruits:
    print(i)
    if i == 'Tamanna':
        break
    print(i)