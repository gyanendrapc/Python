# # example of collections
# # A Python program to show different ways to create Counter.
#
# from collections import Counter
#
# # With sequence of items
# print(Counter(['B', 'B', 'A', 'B', 'C', 'A', 'B', 'B', 'A', 'C']))
#
# # With dictionary
# print(Counter({'A': 3, 'B': 5, 'C': 2}))
#
# # With keyword arguments
# print(Counter(A=3, B=5, C=2))
#
# print("Updation:")
#
# # A Python program to demonstrate update()
# from collections import Counter
#
# coun = Counter()
#
# coun.update([1, 2, 3, 1, 2, 1, 1, 2])
# print(coun)
#
# coun.update([1, 2, 4])
# print(coun)

# print("Counts can be zero and negative also.")
# # Python program to demonstrate that counts in
# # Counter can be 0 and negative
# from collections import Counter
#
# c1 = Counter(A=4, B=3, C=10)
# c2 = Counter(A=10, B=3, C=4)
#
# c1.subtract(c2)
# print(c1)


print("We can use Counter to count distinct elements of a list or other collections.")

# An example program where different list items are counted using counter
from collections import Counter

# Create a list
z = ['blue','red','blue','yellow','blue','red']

# Count distinct elements and print Counter object
print(Counter(z))
