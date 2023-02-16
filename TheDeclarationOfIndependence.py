# Programmer: Aaron Arce
# Date: 2.16.2023
# Program: Infotech Center Upgrades

"""
We will make a function that shows contacts
- Create a list of contacts
-Print all contacts
"""

# Libraries Here
import random



def contacts():
    contactList = ["Mom","Dad","Brother","Sister","Grandma","Grandpa","Aunt","Uncle"]
    currentContact = random.choice(contactList)
    return currentContact

print("Alert!", contacts(),"is calling.")