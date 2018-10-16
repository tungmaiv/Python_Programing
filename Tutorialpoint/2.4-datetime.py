import sys
import calendar
import time  # This is required to include time module.

print(sys.executable)
print(sys.version)


ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970:", ticks)

localtime = time.localtime(time.time())
print("Local current time :", localtime)

localtime = time.asctime(time.localtime(time.time()))
print("Local current time :", localtime)

cal = calendar.month(2008, 11)
print("Here is the calendar:")
print(cal)
