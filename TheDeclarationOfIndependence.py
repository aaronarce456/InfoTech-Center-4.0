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


vRS()