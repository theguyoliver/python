# Question 1
the_olives = {'Emmanuel', 'Favour', 'Ubong', 'Sophia', 'Mum', 'Dad', 'Ethan'}
f_the_olives = frozenset(the_olives)
the_olives.add('New Grand Child')
# f_the_olives.add('New Grand Child')
print(the_olives)
print(f_the_olives)

# Question 2
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

s1_and_s2 = set1.union(set2)
s1_ands2 = set1|set2
print(s1_ands2)
print(s1_and_s2)


in_s1_s2 = set1 & set2  #set1.intersection(set2)
print(in_s1_s2)
s1_butnot_s2 = set1-set2 #set1.difference(set2)
print(s1_butnot_s2)
s2_butnot_s1 = set2-set1
print(s2_butnot_s1)
print(set1<set2)
print(set2<set1)
