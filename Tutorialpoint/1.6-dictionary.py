import sys
print(sys.executable)
print(sys.version)

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print("\n")
print(dict['one'])       # Prints value for 'one' key
print(dict[2])           # Prints value for 2 key
print(tinydict)          # Prints complete dictionary
print(tinydict.keys())   # Prints all the keys
print(tinydict.values())  # Prints all the values
tinydict['name'] = 'tungmaiv'
print(tinydict['name'])
# print(tinydict.values(2))
