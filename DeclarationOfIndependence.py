# Programer: Lucas Campbell
# Date: 1.20.2023
# Program: InfoTech Center Upgrades

"""
Our Welcome Screen will start our program letting
drivers know that the InfoTech Center 4.0 OS is loading
"""

# Import Libraries Here
import time
import sys
import random
from time import sleep

timeToSleep = 2
x = 0
a = 0

print("\n\nWelcome - InfotechCenter 4.0\n")
time.sleep(timeToSleep)
# print("\nInfoTech Center 4.0 OS is now loading")

while x != 20:
    x += 1
    b = ("\033[1;33;40mInfotech center is now loading" + "." * a)
    a = a + 1
    sys.stdout.write('\r' + b)
    time.sleep(0.5)
    if a == 4:
        a = 0
    if x == 20:
        print('\033[1;32;40;40m Retina Scan Complete - Access Granted!\n')

# Program: Infotech Center 4.0 - Gasoline

"""
We will create a Function that will tell us our Fuel gauge level
   - Create a list with Gas Levels
   - Randomize and choose from the list to determine our gas level
create a Function to determine our closest Gas Station
   - Create a list of gas stations
   - Randomly choose a gas station from the list
Create s Function to determine our gas level and closest gas station
   - Print Gas level
   - Print Closest Gas Station
"""


# Gas Level Function


def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel


# Variable calling gasLevelGauge function to store its value


gasLevelIndicator = gasLevelGauge()


# List of gas stations Function


def listOfGasStations():
    gasStations = ["Shell", "Costco", "Buc-ee's", "Speedway", "7-11", "Circle-K", "Meijer", "Marathon"]
    gasStationNearby = random.choice(gasStations)
    return gasStationNearby


# Determine Gas Level & closest gas station
def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1, 25), 2)
    milesToGasStationQuarterTank = round(random.uniform(26, 50), 2)
    if gasLevelIndicator == "Empty":
        print("\n***WARNING YOU ARE ON EMPTY***")
        sleep(1)
        print("\nCalling Emergency Contact")
    elif gasLevelIndicator == "Low":
        print("\n***Warning***")
        sleep(1)
        print("\nYour gas tank is extremely low, checking Google Maps for the closest gas station.")
        sleep(1)
        print("\nThe closest gas station is", listOfGasStations(), "which is", milesToGasStationLow, "miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("\n***Warning***")
        sleep(1)
        print("\nYour gas tank is only a quarter full.")
        sleep(1)
        print("\nThe closest gas station is", listOfGasStations(), "which is", milesToGasStationQuarterTank,
              "miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("\nYour gas tank is half full, which is enough gas to safely make it to your destination")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("\nYour gas tank is three quarters full, which is more than enough to safely make it to your destination")
    else:
        print("\nYour gas tank is full, Good Job, Vroom Vroom")


# Create weather conditions from in a list and choose it randomly
def weather():
    weatherForecast = ["Snowing", "Blizzard", "Raining", "Foggy", "Windy", "Icy", "Sunshine", "Cloudy", "Tornado"]
    weatherCondition = random.choice(weatherForecast)
    return weatherCondition


# Variable to call weather() function once in our VRS()
weatherAlert = weather()


print("\nChecking current gas levels")
sleep(1)
gasLevelAlert()
