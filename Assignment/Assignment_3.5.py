"""
Name: {Supisara Kongthong}
SID: {364211760017}
Group: {MIT211}

เขียนโปรแกรมไพธอนเพื่อนำเลขบัตรประชาชนมาบวกันเพื่อทำนายดวงชะตาดังนี้
• สร้างฟังก์ชันเพื่อหาผลรวมของเลขบัตรประชาชน โดยใช้ชื่อฟังก์ชั่นว่า sumPID()
• สร้างฟังชั่นชื่อ getFortune() เพื่อทำนายดวงชะตา ถ้าเป็นเลขคู่ให้ทำนายว่า your fortune is good
• ถ้าเป็นเลขคี่ ให้ทำนายว่า your fortune is very good
"""


def getPTD():
    sumPID = [int(x) for x in input(f'Enter PID : ').split()]
    return sumPID

def getFortune(*var):
    resultlist = []
    for x in var:
        if x % 2 == 0:
            resultlist.append('Your fortune is good')
        else:
            resultlist.append('Your fortune is very good')
    return resultlist

PID = getPTD()
print(f'The data from user: {sum(PID)}')
print(f'The prediction result is: {getFortune(sum(PID))}')
