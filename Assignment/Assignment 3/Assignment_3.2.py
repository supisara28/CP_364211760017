"""
Name: {Supisara Kongthong}
SID: {364211760017}
Group: {MIT211}

เขียนฟังก์ชันเพื่อยกกำลังสองสมาชิกทุกตัวใน list และ return list ที่เป็นผลลัพธ์จากการยกกำลังสอง
ออกมา กำหนดให้ฟังก์ชันนี้รับ parameter 1 ตัว คือ listA ที่มีสมาชิกเป็นจำนวนใด ๆ
"""


def getNumber():
    listA = []
    for x in range(3):
        listA.append(int(input(f'Enter integer {x+1}: ')))
    return listA
def myfunction(var):
    total = 0
    for x in var:
        e = x ** 2
        total = total + e
    return total


mylist = getNumber()
print(f'The data from user: {mylist}')
print(f'The result of squaring is: {myfunction(mylist)}')