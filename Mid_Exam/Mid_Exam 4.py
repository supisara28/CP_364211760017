"""
Name: {นางสาวศุภิสรา คงทอง}
SID: {364211760017}
Group: {MIT211}
"""

"""
Question 4:
เขียนโปรแกรมรับ input ที่เป็นจำนวนเต็ม 10 จำนวน และตรวจสอบว่าตัวเลขนั้นเป็นจำนวนคี่หรือไม่
ถ้าเป็นจำนวนคี่ ให้นำไปเก็บไว้ในตัวแปรชนิด List ชื่อ myOdd
จากนั้นแสดงผลทางหน้าจอ output

ตัวอย่างผลลัทพ์
Input 10 integer: 11 12 13 14 15 16 17 18
Output:
Odd: 11 13 15 17

(10 คะแนน)
"""
number = [int(x) for x
          in input('Input 10 integer: ').split() if int(x) % 2 == 1]
print(f'Odd:{number}')




