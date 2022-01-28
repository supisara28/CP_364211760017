# set

myset = {'apple', 'banana', 'cherry'}
print(myset)
print(type(myset))
print(len(myset))

# access data in set
# for
for x in myset:
    print(x)

# keyword in
print('apple' in myset)  # True
print('mango' in myset)  # False

# add data to set
# add()
myset.add('mango')
print(myset)
# update()
mynum = {10, 20, 30}
print(mynum)
myset.update(mynum)
print(myset)

# remove data in set
# remove()
myset.remove('banana')
if 'papaya' in myset:
    myset.remove('papaya')
else:
    print('Set has no item "papaya"')
print(myset)

# discard()
myset.discard(20)
print(myset)
# pop()
x = myset.pop()
print(x)
print(myset)
# del keyword
del mynum
# print(mynum)

# clear data in set
# clear()
myset.clear()
print(myset)

myset.add(100)
print(myset)
