# Operators

x = 10
y = 20

# math operators
print('x + y = ', x+y)  # 10+20 = 30
print(f'x + y = {x+y}')

print(f'{x}+{y}={x+y}')
print(x, '+', y, '=', x+y)

print(f'{x}-{y}={x-y}')  # 10-20 = -10
print(f'{x}/{y}={x/y}')
print(f'{x}*{y}={x*y}')  # 10 * 20 = 200
print(f'{x}**{y}={x**y}')
print(f'{x}%{y}={x%y}')
print(f'{x}//{y}={x//y}') # 10 // 20
print(f'{3}%{15}={3%15}')

# comparasion operators
print(f'{x}=={y} = {x==y}')
print(f'{x}!={y} = {x!=y}')
# >, <, >=, <=
print(f'{x}>{y} = {x>y}')
print(f'{x}<{y} = {x<y}')
print(f'{x}>={y} = {x>=y}')
print(f'{x}<={y} = {x<=y}')

# logical operators -- > True, False
# and , or , not
print(f'x>20 and x<10 = {20 < x and 10 > x}')
print(f'x>20 or x<10 = {x>20 or x<10}')
print(f'not(x>20 or x<10) = {not(x>20 or x<10)}')

# identity operators
# is, is not
x = 100
y = 100
print(f'x is y = {x is y}')
y = 200
print(f'x is y = {x is y}')
print(f'x is not y = {x is not y}')

list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]
print(f'list1 is list2 = {list1 is list2}')
newlist = list1
print(f'newlist is list1 = {newlist is list1}')

# bitwise operators
x = 100
y = 200
print(x & y )
print(f'x & y = {x & y}')
print(f'{x} & {y} = {x & y}')
print(f'{x} | {y} = {x | y}')
# ^, >>2, <<2, ~
print(f'{x} ^ {y} = {x ^ y}')
print(f'{x}<<2 = {x<<2}')
print(f'{x}>>2 = {x>>2}')
print(f'~{x} = {~x}')


