"""
Name: {Supisara Kongthong}
SID: {364211760017}
Group: {MIT211}

เขียนฟังก์ชันเพื่อค่าหาต่ำสุด และค่าสูงสุด ให้ return ผลลัพท์ทั้ง 2 ออกมากำหนดให้ฟังก์ชันนี่รับ
parameter 1 ตัว คือ listA ที่มีสมาชิกเป็นจำนวนใดๆ
"""

def getNumber():
    listA = []
    for x in range(5):
        listA.append(int(input(f'Enter integer [{x+1}]: ')))
    return listA

mynum = getNumber()
print(f'The data from user: {mynum}')
print(f'The lowest number is: {min(mynum)}')
print(f'The maximum number is: {max(mynum)}')
