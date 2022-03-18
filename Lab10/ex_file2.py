# File - create and write

"""
mode
x - create
a - create and write from end of file
w - create and overwrite
"""

# create file with mode 'x'
try:
    f = open('demo5.txt', 'x')  # empty file
    print(f.read())
except Exception as e:
    print(e)
    print('This file name is already exist.')
else:
    print('create file successfull.')

# create file with mode 'a'
try:
    f = open('demo6.txt', 'a')
    f.write("Writing contents with mode 'a' ...MIT211\n")
except Exception as e:
    print(e)
else:
    print('writing contents already.')
finally:
    f.close()

# create file with mode 'w'
try:
    f = open('demo7.txt', 'w')
    f.write("delete and writing contents with mode 'w'\n")
except Exception as e:
    print(e)
else:
    print('writing contents already.')
finally:
    f.close()
