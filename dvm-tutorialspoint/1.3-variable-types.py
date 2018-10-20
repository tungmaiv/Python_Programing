import datetime

name = ("Jonathan")
number = ("100")
favoriteFood = ("pasta")
a,b,c = 1,2,3
list = (2,3,5,7,11,13)
anotherlist = (4,6,8,9,10,12)
tuples = ("john","mark","kevin")

print (name)
print (number)
print (favoriteFood)
print (a)
print (b)
print (c)

dt = datetime.date(2018,10,20)
wk = dt.isocalendar()[1]
print(wk)

print (name [0])
print (name [3:7])
print (name [2:])
print (name * 2)
print (name + " is funny !")

print (list)
print (list [2:6])
print (list [0])
print (list * 2 )
print (list + anotherlist)

print (tuples)
print (tuples [0])
print (tuples [1:3])

dict = {}
dict ["8"] = "eight"
dict ["zero"] = "0"
pocketdict = ["banana" : "yellow","bike's lock code" : 237,"programming" : "easy"]
print (dict ["8"])
print (dict ["zero"])
print (pocketdict.keys)
