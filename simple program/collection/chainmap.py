print('ChainMap')
# # python program to demonstrate ChainMap

# from collections import ChainMap
# d1={'a':1,'b':2,'c':3}
# d2={'a':4,'b':5,'c':6}
# d3={'a':7,'b':8,'c':9}
# d4={'a':10,'b':11,'c':12}

# # Defining the ChainMap
# c = ChainMap(d1,d2,d3,d4)
# print(c)


# print("Various operations in ChainMap")
# print("Access operation")

# # Python code to demonstrate ChainMap and
# # keys(), values() and maps

# # importing collections for ChainMap operations
# import collections
# from typing import ChainMap

# # initializing dictionaries
# dic1 = { 'a' : 1, 'b' : 2 }
# dic2 = { 'b' : 3, 'c' : 4 }

# # initializing ChainMap
# chain = collections.ChainMap(dic1,dic2)
# # printing ChainMap using maps
# print(chain.maps)


# # printing keys using keys()
# print("All keys of ChainMap are: ")
# print(list(chain.keys()))

# # printing values using values()
# print("All values of ChainMap are : ")
# print(list(chain.values()))

print("Mainpulating Operations")

# new_child(): adds new dictionary in the begining of  the ChainMap
# reversed(): this function reverses the order of the dictionary in the ChainMap

# importing collections for ChainMap operation
import collections
from ctypes.wintypes import PINT

# initializing dictionary
dic1 = { 'a' : 1, 'b' : 2 }
dic2 = { 'b' : 3, 'c' : 4 }
dic3 = { 'f' : 5 }

# initializing ChainMap

chain = collections.ChainMap(dic1,dic2)

# printing ChainMap using using maps
print(chain.maps)

# using new_child to add new dictionary
chain1 = chain.new_child(dic3)


# printing ChainMap using maps
print(chain1.maps)

# displaying value associated with b before reversing
print("Value associated with b before reversing is : ", end=" ")

print(chain['b'])

# reverse the ChainMap
chain1.maps = reversed(chain1.maps)


# displaying value associated with b after reversing
print("Values associated with b after reversing is : ", end=" ")
print(chain1['b'])


  