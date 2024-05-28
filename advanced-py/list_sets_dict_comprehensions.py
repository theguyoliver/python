
n = [1, 4, 5, 5, 7]
odd = [i for i in n if i%2 !=0]
print(odd)

s = set(n)
s_odd = {i for i in n if i%2 !=0}
print(s_odd)

cities = ['Uyo', 'Asaba', 'Lokoja']
states = ['Akwa Ibom', 'Delta', 'Kogi']

z = zip(cities, states)
print(z)
d = {cities: states for cities, states in z}
print(d)