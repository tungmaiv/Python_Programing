import sys
print(sys.executable)
print(sys.version)


print("\n")
var = 101
if (var == 100):
    print("Value of expression is: " + str(var))
else:
    print("Value of expression is not equal to :" + str(var))


print("\n")

i = 0
while(i <= 5):
    print(i)
    i += 1
else:
    print("Exist")
print("Good bye!")
for letter in "Python":
    print("current letter is: {}".format(letter))
fruits = ["Apple", "Banana", "Grape", "Cherry"]
for fruit in fruits:
    print("current fruit is: " + fruit)

print("\n")
for index in range(len(fruits)):
    print("Current fruit is: " + fruits[index])

count = 0
for num in range(10, 200):  # to iterate between 10 to 20
    for i in range(2, num):  # to iterate on the factors of the number
        if num % i == 0:  # to determine the first factor
            j = num/i  # to calculate the second factor
            print('%d equals %d * %d' % (num, i, j))
            break  # to move to the next number, the #first FOR
    else:                  # else part of the loop
        print(num, 'is a prime number')
        count += 1

print("Total prime number in range is: " + str(count))
print("Good bye!!!")
