"""
Name: {Supisara Kongthong}
SID: {364211760017}
Group: {MIT211}

เขียนฟังก์ชัน Calculator(a,b,op) โดยรับ parameter 3 ตัว ได้แก่ a, b ซึ่งเป็นจำนวนใดๆ และ op ซึ่ง
เป็นสายอักขระที่เป็นไปได้ 4 แบบ คือ +, -, *, /
• ถ้า op เป็น + ให้ return a+b
• ถ้า op เป็น - ให้ return a-b
• ถ้า op เป็น * ให้ return a*b
• ถ้า op เป็น / ให้ return a/b
"""

op = ['+', '-', '*', '/']
def calculator():
    a = input('Enter A : ')
    b = input('Enter B : ')
    op = input('Enter OP :')
    if op == '+':
        return 'a+b'
    elif op == '-':
        return 'a-b'
    elif op == '*':
        return 'a*b'
    else:
        return 'a/b'

cal = calculator()
print(cal)

