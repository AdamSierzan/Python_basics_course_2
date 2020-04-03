#When you want to use a text, whith 
# use the special symbols, it's good to use "r" before them
txt = r"For new line we use \n and for tab use 't"
print(txt)

#Lists

#Lists are made to storage different elements in a []. 
#The elements can have different types

exp_list = [5,3,"Boom", 4,3 ]
print(exp_list)
#the elements on the list are accesable
#to change the element on the list 
exp_list[0] = 3
print(exp_list)

#Tuples

#Tuples are the lists, that can't be modified
#We can access them as lists, but we can't change them
tuple_1 = (3, 4, "Coffee")
print(tuple_1)
print(tuple_1[1])

#Dictionaries

# KEY : VALUE
# Key is unmutuble and unique

ex_1 = { "Cofee" : "black", "Tea": "green", "Sugar" : "no-sugar"}
print(ex_1)
#Dictionries are not originized, so we can't access their elements by index
print(ex_1.keys())
print(list(ex_1.keys()))
print(ex_1.values())

#Is we want to check the key of the value, we can do it like this
if "Cofee" in ex_1.keys(): 
        print("Present, ", end =" ") 
        print("value =", ex_1["Cofee"])
#If we want to add and element to dictionary 
ex_1["Beer type"] = "Ale"
print(ex_1)

#We can also add a list to the dicionary
ex_1["Wine type"] = ["White", "Red"]
print(ex_1)

#We can also add an element to the list 
ex_1["Wine type"].append("Rose")
print(ex_1)

#If we try to check if the element is in the dictionary,
# we can type 
#ex_1("Cider")
#but if it's not it will crash the program

#so it's better to do it like this
ex_1.get("Cider", "Sorry the element is not on the list")
#now the program will return the value or the information that the 
#element is not on the list

#Now something really usefull
#let's say we have variable called "Key"
key = "Cofee"
print(ex_1[key])
#we will get the property
#it's the same as
print(ex_1["Cofee"])

#toclear the dictonary ex_1.clear()