# global variable

print('Start')
x = 'MIT211'
print(x)

def myfunc():
    global x
    x = 'MT at RUTS'
    print(x)

myfunc()
print(x)
print('End')