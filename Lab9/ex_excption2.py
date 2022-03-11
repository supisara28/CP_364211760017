# raise exception

def myfunc():
    # input 1 integer
    x = input('Enter an integer: ')
    if not type(x) is int:
        raise TypeError('Invalid input', x)
    else:
        return x*2

# calling function
try:
    myfunc()
except Exception as e:
    print(e)
    print('Somthing went wrong.')