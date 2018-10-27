import sys
import math
print (sys.version)
print (sys.executable)
print ("\n")
dict = {"name":"Jeff","age":15,"school":"VAS","class":"10S3"}
print ( "My name is", dict["name"], "and i am ", dict["age"])
dict["age"] = 21
dict["school"] = "Waterloo University"
dict["class"] = "data science"
print ("My name is", dict["name"], ",i'm", dict["age"], "and i study", dict["class"], "at", dict["school"],".")
print ("name" in dict)
