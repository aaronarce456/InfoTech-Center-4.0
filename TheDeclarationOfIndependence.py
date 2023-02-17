# Programmer: Aaron Arce
# Date: 1.20.2023
# Program: Infotech Center Upgrades

"""
We will make a tempeerature function that changes with the temperature
to the temperature ouside
"""


# Libraries here
import random


def temperature():
    tempRangeList = ["10-30","-9","31-50","51-59","60-70","+70"]
    currentTempRange = random.choice(tempRangeList)
    return currentTempRange

weatherTemp = temperature()




def carTemp():
    if weatherTemp == "10-30":
        print("The car temperature has increased 15 degrees due to the colder temperature.")
    elif weatherTemp == "-9":
        print("The car temperature has increased by 20 degrees due to freezing temperature.")
    elif weatherTemp == "31-50":
        print("The car temperature has increased by 5 degrees due to temperature.")
    elif weatherTemp == "51-59":
        print("The car temperature has remained the same due to the temperature.")
    elif weatherTemp == "60-70":
        print("The car temperature has remained the same due to temperature.")
    else:
        print("The car temperature has decreased by 5 degrees due to temperature.")



carTemp()