# Programmer: Aaron Arce
# Date: 2.20.2023
# Program: Infotech Center Upgrades


"""
We will make a function that chooses from multiple songs
and shows that it is playing
"""


# Libraries here
import random


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



songOn()