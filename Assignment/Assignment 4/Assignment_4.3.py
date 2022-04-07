"""
Name: {Supisara Kongthong}
SID: {364211760017}
Group: {MIT211}

จากข้อที่ 1 และ 2 ให้นำผลลัพท์ที่ได้จากการรันโปรแกรมเขียนลงไฟล์ต่อไปนี้
ข้อที่ 1 เขียนลงไฟล์ชื่อ A4Q1.txt โดยเขียนตัวเลขที่หารด้วย 5 ลงตัวในไฟล์ เช่น
5
10
15
20
ข้อที่ 2 เขียนลงไฟล์ชื่อ A4Q2.txt โดยเขียนตัวเลขที่รับค่ามาได้ทั้งหมดก่อนที่จะรับตัวเลขที่ซ้ำกัน
"""

# Assignment_4.1
f = open("A4Q1.txt", 'a')
i = int(input("Enter number: "))
count = 0
while count < i:
    if i % 5 == 0:
        count = count + 5
    f.write(str(count)+'\n')
f.close()

# Assignment_4.2
f = open("A4Q2.txt", 'a')
a = []
while True:
    x = int(input())
    if x == 1:
        break
    a.append(x)
f.write(str(a)+'\n')
f.close()
