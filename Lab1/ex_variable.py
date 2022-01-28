# comment

# 1 line
# this is test for comment in python

# multi-lines
"""
This is test for comment multi-lines
Hello, MIT212
Hello, MT
Hello, RUTS
"""

# Variable - ตัวแปร
# integer (int) - จำนวนเต็ม
x = 100  # ประกาศตัวแปรชื่อ x มีค่าเท่ากับ 100
print(x)  # พิมพ์ค่าตัวแปร x
print('The value of x is', x)
print('ตัวแปร x มีค่าเท่ากับ', x)
# display type of x
print('Type of x is ', type(x)) # type x
y = 200
print(x, y)
print('The summation of x and y is ', x+y)

# float - จำนวนจริง
x = 12.12
print(x)
print(type(x))

# String (str) - ข้อความ
x = 'Python'
y = "is the best"
print(x)
print(type(x))
print(y)
print(type(y))
print(x+y)
print(x+' '+y)

# bool - ค่าความจริง True,Flase
a = True
b = False
print(a, b)
print(type(a), type(b))

# multiple variale
a, b, c = 10, 20, 30
print(a)
print(b)
print(c)

a = b = c = 100
print(a)
print(b)
print(c)