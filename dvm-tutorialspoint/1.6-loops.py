import sys
print (sys.version)
print (sys.executable)

num = 0
while (num < 10) :
   print("The number is", num)
   num += 2

count = 0
while (count < 7):
    count += 1
    print (count, "is less than 7.")
else :
    print (count, "is not less than 7.")

var = 0
while (var < 10) :
    var += 1
    if (var % 2 == 0):
       print (var, "is an even number.")
    elif (var % 2 != 0):
       print (var, "is an odd number.")
    else :
       pass

for letter in "Javascript" :
    print ("Letter is", letter)
    if (letter == "s"):
     break
fruits = ["apple","banana","watermelon"]
for index in range (len(fruits)):
    print ("My favorite fruit is", fruits[index])

count = 0
for num in range(10,20):
   for i in range(2,num):
      if (num%i == 0):
         j=num/i
         print ('%d equals %d * %d' % (num,i,j))
         break
   else:
      print (num, 'is a prime number')

int = 10
while (int > 0):
    int -= 1
    if (int == 5):
      continue
    print ("The number is ", int)
