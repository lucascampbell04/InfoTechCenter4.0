# Programmer: Lucas Campbell
# Date 2.8.2023
# Program: Weather System Updates


# Import Libraries here
import random


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
    if weatherAlert == "Snowing":
        print("\nNWS has changed your alarm by 15 minutes because of the weather forecast of ", weatherAlert)
        print("VRS has been engaged only allowing your vehicle to go 45mph")


vehicleResponseSystem()
