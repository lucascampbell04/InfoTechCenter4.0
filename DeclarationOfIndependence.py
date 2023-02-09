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


# VRS() to respond to the weather conditions
def vehicleResponseSystem():
    print("Placeholder")