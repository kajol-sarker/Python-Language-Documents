#Python Matrix. Ekta list er moddhe onk list thake, jeta matrix ba nasted list bole. list er protita value alada alda item.

list = [
    [1,2,3],     #index 0
    [4,5,6],     #index 1
    [7,8,9],     #index 2
    10           #index 3
 ]
print(list[0][1])   #0 index er 2nd item print korbe, output: 2
print(list[1][2])   #1 index er 3rd item print korbe, output: 6
print(list[2][0])   #2 index er 1st item print korbe, output: 7
print(list[3])      #3 index er item print korbe, output: 10
# or we can do another way like
print("\n")
x = list[0][2]
print(x)