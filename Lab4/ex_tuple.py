# Tuple

mytuple = ('apple','banana','cherry')
print(mytuple)
print(type(mytuple))
print(f'Lenght of mytuple is : {len(mytuple)}')

# access data in tuple
# index
print(mytuple[0])  # apple
print(mytuple[1])  # banana
print(mytuple[2])  # cherry
# negative index
print(mytuple[-1])  # cherry
print(mytuple[-2])  # banana
print(mytuple[-3])  # apple
# range index
mynum = (10, 20, 30, 40, 50)
print(mynum[1:3])  # index 1-2 --> 20, 30
print(mynum[:3])  # index 0-2 --> 10, 20, 30
print(mynum[1:])  # index 1-end
print(mynum[-5:-2])
# loop
# for
for x in mynum:
    print(x)  # แนวตั้ง
for x in mynum:
    print(x, end=" ")  # แนวนอน

print('MIT211')

# for with index
for x in range(len(mynum)):
    print(mynum[x])

# while
i = 0
while i < len(mynum):
    print(mynum[i])
    i += 1
