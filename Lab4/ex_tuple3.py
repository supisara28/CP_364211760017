# tuple - unpacking data in tuple

mytuple = ('apple', 'banana', 'cherry')
print(mytuple, len(mytuple))

# 1
(x, y, z) = mytuple
print(x, y, z)
print(type(x))

# 2 use asterisk *
mytuple = ('apple', 'banana', 'cherry', 'orange', 'mango')
(x, y, *z) = mytuple  # z--> class 'list'
print(x)
print(y)
print(z)

# 3 use asterisk at other position
(*x, y, z) = mytuple  # x --> list
print(x)
print(y)
print(z)
