# Programmer: Aaron Arce
# Date Merged: 2.6.2023
# Merged Welcome Screen and Gasoline Branches - Stable

"""
Our Welcome Screen will start our Program letting
drivers know that the InfoTech Center 4.0 OS is loading
"""

#Import Libraries Here
import time
import sys
import random
from time import sleep

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
        print ('\n\n\033[1;32;40mMission Accomplished - Retina Scanned - Access Granted\n')




# Programmer: Aaron Arce
# Date: 1.30.2023
# Program: Infotech Center 4.0 - Gasoline







# Gas Level Function
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

# Variable calling gasLevelGauge function to store its value
gasLevelIndicator = gasLevelGauge()

# List of Gas Stations Function
def listOfGasStations():
   gasStations = ["Shell","Costco","Buc-ee's","Speedway","7-11","Circle-K","Meijer","Marathon"]
   gasStationNearby = random.choice(gasStations)
   return gasStationNearby

# Determine Gas Level & Closest Gas Station
def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1, 25), 2)
    milesToGasStationQuartTank = round(random.uniform(26, 50), 2)
    if gasLevelIndicator == "Empty":
        print("***WARNING YOU ARE ON EMPTY***")
        sleep(1)
        print("Calling Emergency Contact")
    elif gasLevelIndicator == "Low":
        print("****Warning****")
        sleep(1)
        print("Your gas tank is extremely low, checking Google Maps for the closest gas station.")
        sleep(1)
        print("The closest gas station is",listOfGasStations(),"which is",milesToGasStationLow,"miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("***Warning***")
        sleep(1)
        print("Your gas tank is at a Quarter Tank and the closest gas station is",listOfGasStations(),"which is",milesToGasStationQuartTank,"miles away.")
    elif gasLevelIndicator == "Half":
        print("Your gas tank is a half of a tank which is plenty of gas to make it to your destination today")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is a three quarter of a tank which is "
              "plenty of gas to make it to your destination today.")
    else:
        print("Your gas tank is full - Yeah! - Congratulations - Vroom Vroom.")



# Programmer: Aaron Arce
# Date: 2.8.2023
# Program: Weather System Updates


# Import Libraries Here
import random

# Create a weather conditions in a list and choose it randomly
def weather():
    weatherForecast = ["Snowing","Blizzard","Rain","Foggy","Windy","Icy","Sunshine"]
    weatherCondition = random.choice(weatherForecast)
    return weatherCondition

# Variable to call weather() once in our VRS()
weatherAlert = weather()



# VRS() to respond to the weather conditions
def vRS():
    if weatherAlert == "Snowing":
        print("\nNWS has changed your Alarm by 15 minutes because of the weather forecast of",weatherAlert)
        print("Your VRS has been engaged only allowing your vehicle to go 45 MPH.")
    elif weatherAlert == "Blizzard":
        print("\nNWS has changed your Alarm by 30 minutes because of the weather forecast of",weatherAlert)
        print("Your VRS has been engaged only allowing your vehicle to go 35 MPH.")
    elif weatherAlert == "Rain":
        print("\nNWS is calling for,",weatherAlert,"please drive extra carefully.")
    elif weatherAlert == "Foggy":
        print("\nNWS is calling for",weatherAlert,"conditions, please drive extra careful.")
    elif weatherAlert == "Windy":
        print("\nNWS is calling for",weatherAlert,"conditions, please drive extra careful.")
    elif weatherAlert == "Icy":
        print("\nNWS has changed your Alarm by 60 minutes because of the weather forecast of",weatherAlert)
        print("Your VRS has been engaged only allowing your vehicle to go 25 MPH.")
    else:
        print("\nNWS is calling for",weatherAlert,"drive safely and have a wonderful day.")








# Call functions here
vRS()
gasLevelAlert()