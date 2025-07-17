'''
Dictionary is a collection of key-value pairs. It is ordered, mutable, and indexed.
It is also known as associative array or hash map in other programming languages.
Dictionary is special variable that can hold huge amount of data in a single variable. 

'''

MyInfo = {
    "Name"   : "Md.Kajol Sarker",
    "Age"    : 24,
    "Gender" : "Male"
}
print(MyInfo["Name"])      #print(variable name[key])


#Other way is
Myself = {
    "Student1":{                                  #this is a key
        "Name"   : "Md.Kajol Sarker",       #create key value pair under key in dictionary. This is also known nasted dictionary, dictionary modde dictionary
        "Age"    : 24,
        "Gender" : "Male",
        "Study"  : "Green University",
        "Subject" : "CSE",
        "Id"      : "221902165"
    },
    "Student2":{
        "Name"  : "Tamanna Riva",
        "Age"   : 23,
        "Gender" : "Female",
        "Study"  : "Green University",
        "Subject" : "CSE",
        "Id"      : "221902166"

    },

    "Student3":{
        "Name"   : "Sayma Akater",
        "Age"    : 22,
        "Gender" : "Female",
        "Study"  : "Green University",
        "Subject" : "CSE",
        "Id"      : "221902099"
    }
}

# print(Myself["Student2"]["Name"])
# print(Myself["Student2"]["Id"])



# #Access Dictionary. get(). keys(), values() method.
# #get() method
# x = Myself.get("Student3")      #get function er moddde key er nam dite hobe
# print(x)   #or we may do print(Myself.get("Student3"))

# #keys() method
# y = Myself.keys()      #no parameter need
# print(y)               #show all key name in dictionary. only for parent keys


# #values() method
# z = Myself.values()    #no parameter need
# print(z)               #show all value in dictionary.



# #Dictionaries Change.
# a = Myself["Student2"]["Id"] = 221902099    #dictionary k variable a rekhe korte pari abar na rekheo korte pari.
# print(a)

# #using updaet() method
# Myself.update({"Student3": "This is Kajol's wife tamanna"})      #dictionary name.update({})
# print(Myself["Student3"])


# #remove dictionary items or values
# #pop() method
# Myself.pop("Student3")        #remove the key with its nasted dictionary.
# print(Myself)


# #popitem() method
# Myself.popitem()       #by default it removes the last items 
# print(Myself)


# #also other methods like clear(), remove(), del() etc.


# # #Loop in Dictionary.
# for i in Myself:        #print the nasted key only
#     print(i)             

# for k in Myself.keys():
#     print(k)                #print the nasted key only.


# for l in Myself.values():    #print the values only.
#     print(l)


# for j in Myself.items():     #print the nasted key with its key value pair.
#     print(j)


# #Copy Dictionary by using copy() and dict() methods.
# #copy() method
# new_dic = Myself.copy()
# print(new_dic)
# print('\n')
# print(Myself)


# #dict() method
# new_di = dict(Myself)
# print(new_di)
# print('\n')
# print(Myself)


