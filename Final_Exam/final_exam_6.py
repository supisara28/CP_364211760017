"""
Name: {นางสาวศุภิสรา คงทอง}
SID: {364211760017}
Group: {MIT211}
"""
"""
Quesiton 6:
เขียนโปรแกรมเพื่อนับสระในภาษาอังกฤษ (Vowels: a e i o u) 
โดยรับข้อความจากผู้ใช้ จากนั้นให้โปรแกรมแสดงผลว่าจากข้อความดังกล่าว
มีสระแต่ละตัวมีจำนวนเท่าไร

Example:

Input message:  The National Vaccine Board approved a 
policy with the additional target of procuring 150 million 
doses of COVID-19 vaccines by 2022

Result:
a = 10
e = 7
I = 11
o = 11
u = 1 

"""

while(True):
    phrase = input('Enter message: ')
    if phrase == 'end':
        quit()
    lower = str.lower(phrase)
    convert = list(lower)
    a = convert.count('a')
    e = convert.count('e')
    i = convert.count('i')
    o = convert.count('o')
    u = convert.count('u')

    vowel = a + e + i + o + u
    break
print ('\n''Total vowels = ', vowel)
print ('a = ', a)
print ('e = ', e)
print ('i = ', i)
print ('o = ', o)
print ('u = ', u)
