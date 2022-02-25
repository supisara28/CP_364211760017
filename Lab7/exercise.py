"""
เขียนโปรแกรม Lofin โดยรับ Input จากผู้ใช้
คือ username และ password หากผู้ใช้กรอกข้อมูล
ถูกต้องให้แสดงข้อความ "Welcome {name}"
แต่ถ้าไม่ถูกต้องให้ผู้ใช้กรอกข้อมูลใหม่
หากกรอกข้อมูลผิดครบ 3 ครั้ง ให้แสดงข้อความ
"Your account has been locked, please contact admin."

"""
user = 'admin'
password = '1234'

count = 0
while count <3:
    u = input('Enter username: ')
    p = input('Enter password: ')
    if u == user and p == password:
        print(f'Hello, {u}')
        break
    else:
        print(f'username or password is not correct. {count+1}')
        if count < 2:
            print(f'please, login again.')
            count+=1
else:
    print('your account has been locked,'
          'please contact admin')

