# Programmer: Aaron Arce
# Date: 1.20.2023
# Program: Infotech Center Upgrades

"""
Our Welcome Screen will start our Program letting
drivers know that the InfoTech Center 4.0 OS is loading
"""

#Import Libraries Here
import time
import sys

print ('\n\033[1;33;40m Weclcome to InfoTechCenter 4.0')

x = 0
a = 0

time.sleep(2)
print ('')

while x != 20:
    x += 1
    b = ("\033[1;33;40m InfoTechCenter 4.0 is Loading" + "." * a)
    a = a + 1
    sys.stdout.write('\r' + b)  # \r prints a carriage return first, so `b` is printed on top of the previous line.
    time.sleep(0.5)
    if a == 4:
        a = 0
    if x == 20:
        print ('\n\n\033[1;32;40mMission Accomplished - Retina Scanned - Access Granted')
