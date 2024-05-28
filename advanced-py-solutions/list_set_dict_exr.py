# Question 1
integers = [0, 1, 2, 3, 4]
binary_int = ["0", "1", "10", "11", "100"]

dict_int = {}
for x, y in zip(integers, binary_int):
    dict_int[x] = y

print(dict_int)


# Question 2
integers1 = [1, -1, 2, 3, 5, 0, -7]
additive_inverse = [0-i for i in integers1]

print(additive_inverse)

# Question 3
integers2 = [1, -1, 2, -2, 3, -3]
int_sq = [i*i for i in integers2]
set_sq = set(int_sq)
print(set_sq)
