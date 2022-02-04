# input multiple value

# x = int(input("Enter any number: "))
# print(x, type(x))

# x, y, z = input("Enter 3 number: ").split()
# print(x)
# print(y)
# print(z)

# x, y, z = input("Enter 3 number: ").split()  # .split(',')
# print(x)
# print(y)
# print(z)

# input into list
# mylist = list(input('Enter any number: ').split())
# print(mylist)

# input multi integer into list
# mylist = list(map(int, input('Enter any number: ').split()))
# print(mylist)

# list comprehension
# mylist = [int(x) for x in input('Enter any number: ').split()]
# print(mylist)

myEven = [int(x) for x
          in input('Enter any number: ').split() if int(x) % 2 == 0]
print(myEven)

