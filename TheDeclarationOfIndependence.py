# Programmer: Aaron Arce
# Date: 2.8.2023
# Program: Weather System Updates

# Import Libraries Here
import random

# Create a weather conditions in a list and choose it randomly
def weather():
    weatherForecast = ["Snowing","Blizzard","Raining","Foggy","Windy","Icy","Sunshine"]
    weatherCondition = random.choice(weatherForecast)
    return weatherCondition

# Variable to call weather() once in our VRS()
weatherAlert = weather()

print(weatherAlert)

# VRS() to respond to the weather conditions
def vrs():
    print("Howdy")