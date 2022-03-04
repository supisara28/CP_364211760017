# function and return statement


# validate integer --> Even or Odd
def validateInteger(var):
    if var % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

def validateInteger2(*var):
    resultlist = []
    for x in var:
        if x % 2 == 0:
            #return 'Even'
            resultlist.append('Even')
        else:
            #return 'Even'
            resultlist.append('Odd')
    return resultlist

# calling function
print(validateInteger(10))
print(validateInteger(33))
myresult = validateInteger(101)
print(myresult)
print(validateInteger2(10, 11, 12, 13, 14, 15))