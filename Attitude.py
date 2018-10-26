
att = "Attitude"
itl = "Intelligent"
klg = "Knowledge"

total_att = 0; total_itl = 0; total_klg = 0

for letter in att.upper():
    total_att += ord(letter)
for letter in itl.upper():
    total_itl += ord(letter)
for letter in klg.upper():
    total_klg += ord(letter)

print("Hello")
print("Total of Attitude is: {}".format(total_att/len(att)))
print("Total of Intelligent is: {}".format(total_itl/len(itl)))
print("Total of Knowledge is: {}".format(total_klg/len(klg)))
