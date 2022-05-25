# # A Python program to show different ways to create Counter
# from collections import Counter
#
# print("Counters")
# # With sequence of items
# print(Counter(['B', 'B', 'A', 'B', 'C', 'A', 'B', 'B', 'A', 'C']))
#
# # With dictionary
# print(Counter({'A': 3, 'B': 5, 'C': 2}))
#
# # With keyword arguments
# print(Counter(A=3, B=5, C=2))
#
# print("OrderedDict")
#
# # A Python program to demonstrate working of OrderDict
# from collections import OrderedDict
#
# print("This is a Dict : \n")
# d = {}
# d['a'] = 1
# d['b'] = 2
# d['c'] = 3
# d['d'] = 4
#
# for key, value in d.items():
#     print(key, value)
#
# print("\nThis is an Ordered Dict:\n")
# od = OrderedDict()
# od['a']=1
# od['b']=2
# od['c']=3
# od['4']=4
#
# for key,value in od.items():
#     print(key,value)

#
# '''
# While deletin and re-installing the same key will push the key to the last to maintain the order of insertion of the key.
# '''
#
# # A Python program to demonstrate working of OrderDict
#
# from collections import OrderedDict
#
# od = OrderedDict()
# od['a'] = 1
# od['b'] = 2
# od['c'] = 3
# od['4'] = 4
#
# print("Before Deleting")
# for key, value in od.items():
#     print(key, value)
#
# # deleting element
# od.pop('a')
#
# # re-inserting the same
#
# od['a'] = 1
#
# print('\nAfoter re-inserting')
# for key, value in od.items():
#     print(key,value)

# print("DefaultDict")

# # Python program to demonstrate defaultdict
# from collections import defaultdict
#
# # Defining the dict
# d = defaultdict(int)
# L = [1, 2, 3, 4, 2, 4, 1, 2]
#
# # Iterate through the list for keeping the count
# for i in L:
#     # The default value is 0 so there is no need to enter the key first
#
#     d[i] += 1
# print(d)

# # Python program to demonstrate defaultdict
# from collections import  defaultdict
#
# # Defining a dict
# d = defaultdict(list)
# for i in range(5):
#     d[i].append(i)
#
# print("Dictionary with values as list:")
# print(d)

print("ChainMap")
'''
A ChainMap encapsulates many dictionaries into a single unit and returns a list of dictionaries
'''

# Python program to demonstrate ChainMap
# from collections import  ChainMap
#
# d1 = {'a': 1, 'b': 2}
# d2 = {'c': 3, 'd': 4}
# d3 = {'e': 5, 'f': 6}
#
# # Defining the chainmap
# c = ChainMap(d1, d2, d3)
#
# print(c)

# print("Accessing Key & Values From ChainMap")
#
# '''
# Values from ChainMap can be accessed using the key name.
# They can also be accessed by using the key() ad values() method.
# '''
#
# # Pythonprogram to demonstrate ChainMap
# from collections import ChainMap
#
# d1 = {'a': 1, 'b': 2}
# d2 = {'c': 3, 'd': 4}
# d3 = {'e': 5, 'f': 6}
#
# # Defining the chainmap
# c = ChainMap(d1, d2, d3)
#
# # Accessing Values using key name
# print(c['a'])
# # Accessing values using values() method
# print(c.values())
#
# # Accessing keys using keys() method
# print(c.keys())

#
# print("Adding new dictionary")
#
# '''
# A new dictionary can be added by using the new_child() method.
# The newly added dictionary is added at the beginning of the ChainMap
# '''
#
# # Python code to demonstrate ChainMap and new_child()
# import collections
#
# # initializing dictionaries
# dic1 = {'a': 1, 'b': 2}
# dic2 = {'b': 3, 'c': 4}
# dic3 = {'f': 5}
#
# # initializing ChainMap
# chain = collections.ChainMap(dic1, dic2)
#
# # printing ChainMap
# print("All the ChainMap contents are : ")
# print(chain)
#
# # Using new_child() to add new dictionary
# chain1 = chain.new_child(dic3)
#
# # printing chainMap
# print("Displaying new ChainMap")
# print(chain1)


print("NamedTuple")

# # Python code to demonstrate namedtuple()
#
# from collections import namedtuple
#
# # Declaring namedtuple()
#
# Student = namedtuple('Student', ['name', 'age', 'DOB'])
#
# # Adding values
# S = Student('paro','22','9845914378')
#
# # Access using index
# print("The Student age using index is : ", end=" ")
# print(S[1])
#
# # Accessing using name
# print("The Student name using keyname is : ", end=" ")
# print(S.name)
#
#
# print("Conversion Operation")
# '''
# 1._make(): This function is used to return a namedtuple() from the iterable passed as argument.
# 2._asdict(): This function returns the OrderDict() as constructed from the mapped values of namedtuple()
# '''
#
# # Python code to demonstrate namedtuple() and _make() _asdict()
#
# from collections import namedtuple
#
# # Declaring namedtuple()
#
# Student = namedtuple('Student', ['name', 'age', 'DOB'])
#
# # Adding values
# S = Student('Nandini', '19', '12312313')
#
# # initializing iterable
# li = ['Manjeet', '19', '432434']
#
# # initializing dict
# di = {'name': 'nikhil', 'age': 19, 'DOB': '7389473284'}
#
# # using _make() to return namedtuple()
#
# print("The namedtuple instance using iterable is : ")
# print(Student._make(li))
#
# # using _asdict() to return namedtuple()
#
# print("The OrderedDic instance using namedtuple is : ")
# print(S._asdict())

# # Python program to demonstrate deque
# from collections import deque
#
# # Declaring deque
#
# queue = deque(['name', 'age', 'DOB'])
# print(queue)
#
#
# print("Inserting Elements")
# # Python code to demonstrate working of append(), appendleft()
#
# from collections import deque
#
# # initializing deque
#
# de = deque([1, 2, 3, 4])
#
# # using append() to insert element at right end inserts 4 at the end of deque
# de.append(de)
#
# # printing modified deque
# print("The deque after appending at right is : ")
# print(de)
#
# # using appendleft() to insert element at right end inserts 6 at the begining of deque
#
# de.appendleft(6)
#
# # print modified deque
# print("The deque after appending at left is : ")
# print(de)
#
# # Python code to demonstrate working of pop() and popleft()
#
# from collections import deque
#
# # initializing deque
# de = deque([6, 1, 2, 3, 4, ])
#
# # using pop() to delete element from right end
# # deletes 4 from the right end of deque
# de.pop()
#
# # printing modified deque
# print("The deque after deleting from right is : ")
# print(de)
#
# # using popleft() to delete element from left end deletes 6 from the left end of deque
# de.popleft()
#
# # printing modified deque
# print("The deque after deleting from left is : ")
# print(de)

#
# print("UserDict")
# '''
# UserDict is a dictionalry-like container that acts as a wrapper around the dictionary objects.
# This container is used when someone wants to create their own dictionary with some modified or new functionality.
# '''
#
# # Python program to demonstrate userDict
# from collections import UserDict
# # Create a dictionary where
# # deletion is not allowed
# class MyDict(UserDict):
#     # Function to stop deletion from dictionary
#     def __del__(self):
#         raise RuntimeError("Deletion is not allowed")
#
#     # functon to stop pop from dictionary
#     def pop(self, s=None):
#         raise RuntimeError("Deletion is not allowed")
#
#     # functin to stop popitem from dictionary
#     def popitem(self, s=None):
#         raise RuntimeError("Deletion is not allowed")
#
#
# d = MyDict({'a': 1, 'b': 2, 'c': 3})
# print(d.pop(1))

#
# print("UserList")
# '''
# UserList is a list like container that acts as a wrapper around the list objects.
# This is useful when someone wants to create their own list with some modification or additional functionality.
# '''
# # Python progra to demonstrate userlist
# from collections import UserList
#
#
# # create a List where deletion is not allowed
# class MyList(UserList):
#     # funcion to stop deletion from list
#     def remove(self, s=None):
#         raise RuntimeError("Deletion not allowed")
#
#     # Function to stop pop from List
#     def pop(self, s=None):
#         raise RuntimeError("Deletion not allowed")
#
#
# # Driver's code
# L = MyList([1, 2, 3, 4, 5])
# print("Origional List")
#
# # Inserting to List
# L.append(5)
# print("After Insertion")
#
# print(L)
#
# # Deleting from list
# L.remove()

print("UserSring")
'''
UserString is a string like container ad just like UserDict and UserList it acts as a
wrapper around string objects.
it is sed when someone wants to create their own string with some modification or additional functionality.
'''

# Python program to demonstrate userstring

from collections import UserList


# Creating a Mutual String
class Mystring(UserList):
    # Functon to append to string
    def append(self, s):
        self.data += s

    # Function to remove from string
    def remove(self, s):
        self.data = self.data.replace(s, "")


# Driver's code
s1 = Mystring("Geeks")
print("Origional String", s1.data)

# Append to string
s1.append("s")
print("String After Appending : ", s1.data)

# Removing from string
print("String after Removing : ", s1.data)



