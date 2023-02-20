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
        print ('\n\n\033[1;32;40mMission Accomplished - Retina Scanned - Access Granted')




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
        print("Calling Emergency Contact\n")
    elif gasLevelIndicator == "Low":
        print("****Warning****")
        sleep(1)
        print("Your gas tank is extremely low, checking Google Maps for the closest gas station.\n")
        sleep(1)
        print("The closest gas station is",listOfGasStations(),"which is",milesToGasStationLow,"miles away.\n")
    elif gasLevelIndicator == "Quarter Tank":
        print("***Warning***")
        sleep(1)
        print("Your gas tank is at a Quarter Tank and the closest gas station is",listOfGasStations(),"which is",milesToGasStationQuartTank,"miles away.\n")
    elif gasLevelIndicator == "Half":
        print("Your gas tank is a half of a tank which is plenty of gas to make it to your destination today\n")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is a three quarter of a tank which is "
              "plenty of gas to make it to your destination today.\n")
    else:
        print("Your gas tank is full - Yeah! - Congratulations - Vroom Vroom.\n")



# Programmer: Aaron Arce
# Date: 2.8.2023
# Program: Weather System Updates




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
        print("Your VRS has been engaged only allowing your vehicle to go 45 MPH.\n")
    elif weatherAlert == "Blizzard":
        print("\nNWS has changed your Alarm by 30 minutes because of the weather forecast of",weatherAlert)
        print("Your VRS has been engaged only allowing your vehicle to go 35 MPH.\n")
    elif weatherAlert == "Rain":
        print("\nNWS is calling for,",weatherAlert,"please drive extra carefully.\n")
    elif weatherAlert == "Foggy":
        print("\nNWS is calling for",weatherAlert,"conditions, please drive extra careful.\n")
    elif weatherAlert == "Windy":
        print("\nNWS is calling for",weatherAlert,"conditions, please drive extra careful.\n")
    elif weatherAlert == "Icy":
        print("\nNWS has changed your Alarm by 60 minutes because of the weather forecast of",weatherAlert)
        print("Your VRS has been engaged only allowing your vehicle to go 25 MPH.\n")
    else:
        print("\nNWS is calling for",weatherAlert,"drive safely and have a wonderful day.\n")









# Date: 2.20.2023
# Program: Infotech Center Upgrades



"""
We will make a function that chooses from multiple songs
and shows that it is playing
"""





def songs():
    songList = ["Bad Habit","Smells Like Teen Spirit","505","Beat It","24k Magic","Here Comes the Sun"]
    songPlaying = random.choice(songList)
    return songPlaying

currentSong = songs()


def songOn():
    if currentSong == "Bad Habit":
        print("Bad Habit by Steve Lacy is currently playing.")
    elif currentSong == "Smells Like Teen Spirit":
        print("Smells Like Teen Spirit by Nirvana is currently playing.")
    elif currentSong == "505":
        print("505 by Arctic Monkeys is currently playing.")
    elif currentSong == "Beat It":
        print("Beat It  by Michael Jackson is currently playing.")
    elif currentSong == "24k Magic":
        print("24k Magic by Bruno Mars is currently playing.")
    else:
        print("Here Comes the Sun by The Beatles is currently playing.")






# Date: 2.16.2023
# Program: Infotech Center Upgrades

"""
We will make a function that shows contacts
- Create a list of contacts
-Print all contacts
"""





def contacts():
    contactList = ["Mom","Dad","Brother","Sister","Grandma","Grandpa","Aunt","Uncle"]
    currentContact = random.choice(contactList)
    return currentContact





"""
We will make a tempeerature function that changes with the temperature
to the temperature ouside
"""





def temperature():
    tempRangeList = ["10-30","-9","31-50","51-59","60-70","+70"]
    currentTempRange = random.choice(tempRangeList)
    return currentTempRange

weatherTemp = temperature()




def carTemp():
    if weatherTemp == "10-30":
        print("The car temperature has increased 15 degrees due to the colder temperature.\n")
    elif weatherTemp == "-9":
        print("The car temperature has increased by 20 degrees due to freezing temperature.\n")
    elif weatherTemp == "31-50":
        print("The car temperature has increased by 5 degrees due to temperature.\n")
    elif weatherTemp == "51-59":
        print("The car temperature has remained the same due to the temperature.\n")
    elif weatherTemp == "60-70":
        print("The car temperature has remained the same due to temperature.\n")
    else:
        print("The car temperature has decreased by 5 degrees due to temperature.\n")



carTemp()

# Call functions here
print("\nNational Weather Service is checking conditions....")
sleep(2)
vRS()
print("Checking current gas levels...")
sleep(2)
gasLevelAlert()
sleep(2)
carTemp()
sleep(2)
songOn()
sleep(2)
print("\nAlert!", contacts(),"is calling.")