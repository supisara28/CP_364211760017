# File - I/10

# read file
# r - read content in a file

f = open("demo.txt")  # -> read
print(f.read())
f.close()
# read 10 charecters from file
f = open("demo.txt")  # -> read
print(f.read(10))
f.close()
# read one line from file
f = open("demo.txt",'r')
print(f.readline())
print(f.readline())
print(f.readlines())
f.close()

# case error
try:
    f = open("demo.txt")
    print(f.read())
except Exception as e:
    print(e)
    print("colud not found a file.")
else:
    print("Opening a file....")
finally:
    f.close()
