print("Namedtuple in Python")
# from collections import namedtuple

# # Declarin namedtuple()
# Student  = namedtuple('Student',['name','age','DOB'])

# # Adding values
# S = Student('gyanendrapc','25','1997-02-05')

# # Access using index

# print("My age using index is", end='')
# print(S[1])


# # Accessing using name
# print("My name using keyname is : ", end='')
# print(S.name)

# # Acessing using getattr()
# print("My name using getattr() is ", end='')
# print(getattr(S, 'DOB'))

# print("Conversion Operations")

# # Python code to demonstrate namedtuple() and
# # _make(), _asdict() and "**" operator
 
# # importing "collections" for namedtuple()
# import collections

# # Declaring namedtuple()
# Student = collections.namedtuple('Student',['name','age','DOB'])

# # Adding values
# S = Student('gyanendrapc', '25', '1997-02-05')

# # initializing iterable
# li = ['Manjeet', '19', '411997']
 
# # initializing dict
# di = {'name': "Nikhil", 'age': 19, 'DOB': '1391997'}

# # Using _make() to return namedtuple()

# print("The namedtuple instance using iterable is : ")
# print(Student._make(li))

# # Using _asdict() to return an OrderedDict()

# print("The OrderedDict instance using namedtuple is : ")
# print(S._asdict())


# # using ** operator to return namedtuple from dictionary

# print("The namedtuple instance from dict is : ")
# print(Student(**di))

print("Additional Operations")
# Python code to demonstrate namedtuple() and
# _fields and _replace()
 
# importing "collections" for namedtuple()
import collections
# Declare namedtuple
Student = collections.namedtuple('Student',['name','age','DOB'])

# Adding values
S = Student('gyanendrapc','25','1997-02-05')

# using _fields to display all the keynames of namedtuple()
print(S._fields)

# ._replace returns a new namedtuple, it does not modify the original
print("returns a new namedtuple : ")
print(S._replace(name='gyanendra'))

# origional namedtuple
print(S)