# tuple
# we can not change, add or remove data in tuple

mytuple = (10, 20, 30, 40, 50)
print(mytuple[0])  # 10
# mytuple[0] = 100 # error

# tuple --> list
mylist = list(mytuple)
print(mylist, type(mylist), len(mylist))
# change and add data in tuple
# change item at index 0 to 100
mylist[0] = 100
print(mylist)
# add 1000 to mylist
mylist.append(1000)
print(mylist)

# list --> tuple
mytuple = tuple(mylist)
print(mytuple, type(mytuple))

# remove data in tuple
# tuple --> list
mylist = list(mytuple)
# remove 50 in mylist
mylist.remove(50)
print(mylist)
# list --> tuple
mytuple = tuple(mylist)
print(mytuple)

# join tuple
x = (1, 2, 3, 4 ,5)
y = ('a', 'b', 'c')
print(f'x = {x} y = {y}')
# operator +
z = x+y
print(f'z = x+y = {z}')

# operator *
x = x*2
print(x)
y = y*3
print(y)
