"""
Name: {นางสาวศุภิสรา คงทอง}
SID: {364211760017}
Group: {MIT211}
"""
"""
Question 5:
เขียนโปรแกรมเพื่อคำนวณพลังงานที่เราใช้ในการดำรงชีวิตในช่วงเวลา 
24 ชั่วโมง (Basal Metabolic Rate: BMR) และ 
TDEE คือค่า BMR บวกกับจำนวนแคลอรี่ที่เกิดจากการทำกิจกรรม หรือการออกกำลังกาย

#สมการการหาค่า BMR
BMR เพศชาย = (10 x น้ำหนัก (kg)) + (6.25 x ส่วนสูง (cm)) - (5 x อายุ (ปี)) + 5
BMR เพศหญิง = (10 x น้ำหนัก (kg)) + (6.25 x ส่วนสูง (cm)) - (5 x อายุ (ปี)) - 161

#สมการสำหรับหาค่า TDEE
TDEE = BMR x Activity Factor 

•	Activity Factor คือ ปัจจัยในการทำกิจกรรมหรือออกกำลังกาย ยิ่งคุณออกกำลังกายมากเท่าไหร่ ค่าActivity Factor ยิ่งเพิ่มมากขึ้นเท่านั้น  
•	Activity Factor = 1.2 การออกกำลังกายน้อยมาก หรือไม่ออกกำลังกายเลย (No exercise)
•	Activity Factor = 1.375 การออกกำลังกายน้อย ออกกำลังกาย 1-3 วันต่อสัปดาห์ (1-3 day per week)
•	Activity Factor = 1.55 การออกกำลังกายปานกลาง ออกกำลังกาย 3-5 วันต่อสัปดาห์ (3-5 day per week)
•	Activity Factor = 1.725 การออกกำลังกายหนัก ออกกำลังกาย 6-7 วันต่อสัปดาห์ (6-7 day per week)
•	Activity Factor = 1.9 การออกกำลังกายออกกำลังกายหนักมากหรือเป็นนักกีฬา (heavy exercise or sportsman)
หมายเหตุ:  โปรแกรมต้องแสดงผลทั้ง BMR และ TDEE 
โดยต้องมีฟังก์ชั่นชื่อ cal_bmr() สำหรับคำนวณค่า BMR 
และฟังก์ชั่นชื่อ cal_tdee() สำหรับคำนวณค่า TDEE
(5 คะแนน)
"""

print("การคำนวณพลังงานที่เราใช้ในการดำรงชีวิตในช่วงเวลา")
print("Select Gender")
print("1.Male")
print("2.Female")
Choose = int(input("Enter Gender : "))
if Choose == 1 :
    Weight = int(input("Enter your weight : "))
    Height = int(input("Enter your height : "))
    Age = int(input("Enter your age : "))
    print("BMR = ","5+(10*Weight)+(6.25*Height)-(5*Age)")
    print("BMR = ","5+(10*",Weight,")+(6.25*",Height,")-(5*",Age,")")
    cal_bmr = 5+(10*Weight)+(6.25*Height)-(5*Age)
    print("BMR :",cal_bmr)
    print("<---Choose your exercise--->")
    print("1. การออกกำลังกายน้อยมาก หรือไม่ออกกำลังกายเลย")
    print("2. การออกกำลังกายน้อย ออกกำลังกาย 1-3 วันต่อสัปดาห์")
    print("3. การออกกำลังกายปานกลาง ออกกำลังกาย 3-5 วันต่อสัปดาห์")
    print("4. การออกกำลังกายหนัก ออกกำลังกาย 6-7 วันต่อสัปดาห์")
    print("5. การออกกำลังกายออกกำลังกายหนักมากหรือเป็นนักกีฬา")
    Choose_ex = int(input("Enter your exercise :"))
    if Choose_ex == 1:
        cal_tdee = 1.2*cal_bmr
        print("TDEE :",cal_tdee)
    elif Choose_ex == 2:
        cal_tdee = 1.375*cal_bmr
        print("TDEE :",cal_tdee)
    elif Choose_ex == 3:
        cal_tdee = 1.55*cal_bmr
        print("TDEE :",cal_tdee)
    elif Choose_ex == 4:
        cal_tdee = 1.725*cal_bmr
        print("TDEE :",cal_tdee)
    elif Choose_ex == 5:
        cal_tdee = 1.9*cal_bmr
        print("TDEE :",cal_tdee)
    print("ถ้าต้องการฟิตหุ่น(ลดไขมัน)เลือก1")
    print("ถ้าต้องการเพิ่มน้ำหนัก(กล้ามเนื้อ)เลือก2")
    Choose_2 = int(input("Enter your need :"))
    if Choose_2 == 1:
        x = cal_tdee - 500
        print("Your finale TDEE :",x)
    elif Choose_2 == 2:
        x = cal_tdee + 500
        print("Your finale TDEE :",x)
if Choose == 2 :
    Weight = int(input("Enter your weight : "))
    Height = int(input("Enter your height : "))
    Age = int(input("Enter your age : "))
    print("BMR = ","161-(10*Weight)+(6.25*Height)-(5*Age)")
    print("BMR = ","161-(10*",Weight,")+(6.25*",Height,")-(5*",Age,")")
    cal_bmr = 161-(10*Weight)+(6.25*Height)-(5*Age)
    print("BMR :",cal_bmr)
    print("<---Choose your exercise--->")
    print("1. การออกกำลังกายน้อยมาก หรือไม่ออกกำลังกายเลย")
    print("2. การออกกำลังกายน้อย ออกกำลังกาย 1-3 วันต่อสัปดาห์")
    print("3. การออกกำลังกายปานกลาง ออกกำลังกาย 3-5 วันต่อสัปดาห์")
    print("4. การออกกำลังกายหนัก ออกกำลังกาย 6-7 วันต่อสัปดาห์")
    print("5. การออกกำลังกายออกกำลังกายหนักมากหรือเป็นนักกีฬา")
    Choose_ex = int(input("Enter your exercise :"))
    if Choose_ex == 1:
        cal_tdee = 1.2*cal_bmr
        print("TDEE :",cal_tdee)
    elif Choose_ex == 2:
        cal_tdee = 1.375*cal_bmr
        print("TDEE :",cal_tdee)
    elif Choose_ex == 3:
        cal_tdee = 1.55*cal_bmr
        print("TDEE :",cal_tdee)
    elif Choose_ex == 4:
        cal_tdee = 1.725*cal_bmr
        print("TDEE :",cal_tdee)
    elif Choose_ex == 5:
        cal_tdee = 1.9*cal_bmr
        print("TDEE :",cal_tdee)
    print("ถ้าต้องการฟิตหุ่น(ลดไขมัน)เลือก1")
    print("ถ้าต้องการเพิ่มน้ำหนัก(กล้ามเนื้อ)เลือก2")
    Choose_2 = int(input("Enter your need :"))
    if Choose_2 == 1:
        x = cal_tdee - 500
        print("Your finale TDEE :",x)
    elif Choose_2 == 2:
        x = cal_tdee + 500
        print("Your finale TDEE :",x)
print("<---Thanks you--->")
