# # Python program to demonstrate dictionary
#
# Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
# print("Dictionary")
# print(Dict)
# print(Dict[1])
#
#
# # Uncommenting this print(Dict[4])
# # will raise a KeyError as the
# # 4 is not present in the dictionary
#
#
# print("defaultdict")
#
# # Python program to demonstrate defaultdict
# from collections import defaultdict
# # Function to return a default
# # values for keys that is not present
#
# def def_value():
#     return "not present"
#
# # Defining the dict
# d = defaultdict(def_value)
# d["a"] = 1
# d["b"] = 2
#
# print(d["a"])
# print(d["b"])
# print(d["c"])
#
#
# print("Inner Working of defaultdict")
#
#
##Python program to demonstrate default_factory argument of defaultdict
# from collections import defaultdict
# # defining the dict and passing lambda as default_factory argument
# d = defaultdict(lambda :"no present")
# d["a"]=1
# d["b"]=2
#
# print(d["a"])
# print(d["b"])
# print(d["c"])


print("The _missing_() function")
# python program to demonstrate defaultdict
from collections import defaultdict
# defining the dict
d = defaultdict(lambda :"not present")
d["a"]=1
d["b"]=2

# Provides the default value
# for the key
print(d.__missing__('a'))
print(d.__missing__('d'))