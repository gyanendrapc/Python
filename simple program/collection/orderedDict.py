# # A Python program to demonstrate working of OrderedDict
# from collections import OrderedDict
#
# print("This is a Dict:\n")
# d = {}
# d['a'] = 1
# d['b'] = 2
# d['c'] = 3
# d['d'] = 4
#
# for key, value in d.items():
#     print(key, value)
#
# print("\n This is an Ordered Dict:\n")
#
# od = OrderedDict()
# od['a'] = 1
# od['b'] = 2
# od['c'] = 3
# od['d'] = 4
#
# for key, value in od.items():
#     print(key, value)
#

print("""
1. Key value Change: If the value of a certain key is changed, 
the position of the key remains unchanged in OrderedDict.

""")

from collections import OrderedDict

print("Before:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

for key, value in od.items():
    print(key, value)
print("\n After : \n")
od['c']=5
for key, value in od.items():
    print(key,value)


print("""
2. Deletion and Re-Inserting: Deleting and re-inserting the same key will push it to the back as OrderedDict, 
however, 
maintains the order of insertion.
""")

# A Python program to demonstrate working of deletion re-insertion in OrderdDict
from collections import OrderedDict
print("Before deleting: \n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
for key, value in od.items():
    print(key, value)
print("\nAfter deleting:\n")
od.pop('c')
for key, value in od.items():
    print(key, value)

print("\nAfter re-inserting:\n")
od['c'] = 3
for key, value in od.items():
    print(key, value)