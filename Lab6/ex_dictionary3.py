# Nested Dictionary

car1 = {'brand':'Toyota', 'model':'Altis'}
car2 = {'brand':'Honda', 'model':'HRV'}
car3 = {'brand':'Mazda', 'model':'Mazda 3'}

mycar = {'c1':car1,
         'c2':car2,
         'c3':car3}
print(mycar['c1'])
print(mycar['c2'])
print(mycar['c3'])

print(mycar['c1']['model'])  # Altis

car1['color'] = ['Black', 'Red']
print(mycar['c1'])
print(mycar['c1']['color'][0])
