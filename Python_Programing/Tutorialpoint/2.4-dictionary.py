import sys

print(sys.executable)
print(sys.version)

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First', 'Name': 'Naomi'}
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])


dict['Age'] = 8  # update existing entry
dict['School'] = "DPS School"  # Add new entry

print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])
