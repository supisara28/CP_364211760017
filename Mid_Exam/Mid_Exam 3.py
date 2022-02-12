"""
Name: {นางสาวศุภิสรา คงทอง}
SID: {364211760017}
Group: {MIT211}
"""

"""
Question 3:
จงเขียนโปรแกรมจาก dictionary ที่กำหนดให้
(10 คะแนน)
"""

mydict = {'brand':'toyota','model':'cross','year':'2021'}

# แสดงข้อมูลทั้งหมดใน dicionary mydict
print(mydict)
# แสดงชนิดข้อมูลตัวแปร mydict
print(type(mydict))
# แสดงชนิดข้อมูลค่า value ทุกตัวใน mydict
print(type(mydict.values()))
# เพิ่มข้อมูล 'color':['white','black'] ใน mydict
mydict['color'] = ['white', 'black']
# เพิ่มข้อมูล 'hp': 150 ใน mydict
mydict['hp'] = ['150']
# แสดงข้อมูลเฉพาะ keys ใน mydict
print(mydict.keys())
# แสดงข้อมูลเฉพาะ values ใน mydict
print(mydict.values())
# คัดแยกข้อมูล keys จาก mydict มาเก็บไว้ใรตัวแปรชนิด list ชื่อ mykeys และแสดงข้อมูลทางหน้าจอ
mykeys = list(mydict.keys())
print(mykeys)
# คัดแยกข้อมูล values จาก mydict มาเก็บไว้ใรตัวแปรชนิด list ชื่อ myvalues และแสดงข้อมูลทางหน้าจอ
myvalues = list(mydict.values())
print(myvalues)
# ลบข้อมูล key: 'hp'
del mydict['hp']
# เปลี่ยนแปลงข้อมูลจากเดิม 'color': ['white','black'] เป็น 'Red'
mydict.update({'color': 'Red'})
# แสดงข้อมูล mylist ทางหน้าจอภาพ
print(mydict)
