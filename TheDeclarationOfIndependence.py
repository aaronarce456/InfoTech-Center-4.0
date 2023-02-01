# Programmer: Aaron Arce
# Date: 1.30.2023
# Program: Infotech Center 4.0 - Gasoline

"""
We will create a Function that will tell us our Fuel Gauge level
   - Create a list with Gas Levels
   - Randomize and choose from the list to determine our gas level

Create a Function to determine our closest Gas Station
   - Create a list of gas stations
   - Randomly choose a gas station from the list

Create a Function to determine our gas level and closest gas station
   - Print Gas Level
   - Print Closest Gas Station
"""

# Import Libraries Here
import random
from time import sleep


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
        print("****Warning***")
        sleep(1)
        print("Your gas tank is extremely low, checking Google Maps for the closest gas station.")
        sleep(1)
        print("The closest gas station is",listOfGasStations(),"which is",milesToGasStationLow,"miles away.")





gasLevelAlert()