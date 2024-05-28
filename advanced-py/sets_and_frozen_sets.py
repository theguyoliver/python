
# sets and frozen sets sre used in python to create a unique collection of unordered elements. While we can
# modify the content of sets, frozen sets are immutable, meaning we can't add or remove elements
# We can also perform operations such as union and intersection possible in sets in mathematics here.

x = {i for i in range(1, 11)}
print(x)
y = {1, 2, 3, 4, 5, 33, 27}
z = [i for i in range(25, 37) if i%2 != 0]

# How to convert a list to set
new_z = set(z)

# How to convert a list to frozen set
f_z = frozenset(z)

# How to find the union of sets: It is worth noting that if we have a list we have tp turn it into a set
# to be able to perform these operations
a = y.union(new_z)          # We can use this or
b = y|new_z                 # this
print(a)
print(b)

# Intersection
inter = y & new_z
inter1 = y.intersection(new_z)
if inter:
    print(inter)
else:
    print('There is no intersection between the two sets')
# print(inter1)

# Check if one set is a subset of the other
print(x<y)
print(y<x)
# This shows that x is not subset of y but that y is a subset of x

# We can find the difference between two sets. If a comes before b means we are looking for elements in
# a that are not in b, but if be comes before a then it is the reverse
print(y - f_z)
# print(y.difference(f_z))
print(f_z - y)
# print(f_z.difference(y))
# They both don't give the same output

# We can perform functions like iterate, add, remove, pop, e.t.c. on sets see full list of methods using
print(dir(x))
 
