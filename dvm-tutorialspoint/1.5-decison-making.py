import sys
print (sys.version)
print (sys.executable)

hungerlevel = 80
if (hungerlevel > 60 ) : print ("I am full.")
else : print ("Let's go eat")

streetlight = "red"
if (streetlight == "green") : print ("Go.")
else :
    if (streetlight == "yellow") : print ("Slow down.")
    else : print ("Stop.")
