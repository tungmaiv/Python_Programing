import sys
import math
import time
import calendar
print (sys.version)
print (sys.executable)
print ("\n")

ticks = time.time()
print ("Numeber of ticks since 12:00 am, January 1st, 1970:", ticks)
localtime = time.localtime(time.time())
print ("Local current time:", localtime)
localtime = time.asctime(time.localtime(time.time()))
print ("Local current time:", localtime)
cal = calendar.month (2018,10)
print ("The calendar of this month is:")
print (cal)
