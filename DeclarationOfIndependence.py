# Programmer: Lucas Campbell
# Date 2.8.2023
# Program: Weather System Updates


# Import Libraries here
import random
from time import sleep


# Create weather conditions from in a list and choose it randomly
def weather():
    weatherForecast = ["Snowing", "Blizzard", "Raining", "Foggy", "Windy", "Icy", "Sunshine", "Cloudy", "Tornado"]
    weatherCondition = random.choice(weatherForecast)
    return weatherCondition


# Variable to call weather() function once in our VRS()
weatherAlert = weather()

weatherAlert = "Snowing"


# VRS() to respond to the weather conditions
def vehicleResponseSystem():
    if weatherAlert == "Sunshine":
        print("\nNWS is calling for", weatherAlert, " drive safely and have a wonderful day!")
    elif weatherAlert == "Blizzard":
        print("\nNWS has changed your alarm for 30 minutes in advance to account for the recent", weatherAlert)
        print("\nVRS has been engaged. Your vehicle has been limited to 35MPH for safety.")
    elif weatherAlert == "Raining":
        print("\nNWS is calling for", weatherAlert, " make sure to be extra careful of your surroundings.")
    elif weatherAlert == "Foggy":
        print("\nNWS is calling for", weatherAlert, " keep your fog lights on and drive slowly.")
    elif weatherAlert == "Windy":
        print("\nNWS is calling for", weatherAlert, " please be careful for flying objects.")
    elif weatherAlert == "Icy":
        print("\nNWS has changed your alarm for 15 minutes in advance to account for the recent", weatherAlert)
        print("\nVRS has been engaged. Your vehicle has been limited to 45MPH for safety.")
    elif weatherAlert == "Snowing":
        print("\nNWS is calling for", weatherAlert," VRS has engaged and your vehicle has been limited to 45MPH for safety.")
        print("\nVRS has been engaged. Your vehicle has been limited to 55MPH for safety.")
    elif weatherAlert == "Cloudy":
        print("\nNWS is calling for", weatherAlert, " drive safely and have a wonderful day!")
    else:
        print("\nNWS is calling for a ", weatherAlert, " your vehicle has been disabled due to natural disaster")


# Call function here

print("\nNational weather service is checking conditions")
sleep(1)
vehicleResponseSystem()
