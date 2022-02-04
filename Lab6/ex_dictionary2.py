# dictionary - copy

x = {'item1': 10, 'item2': 20, 'item3': 30}
print(x)

y = x
print("y=", y)
y['item4'] = 40
print(x)

# copy()
z = x.copy()
print("z=", z)
z.popitem()
print("x=", x)
print("z=", z)
