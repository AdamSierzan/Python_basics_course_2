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
