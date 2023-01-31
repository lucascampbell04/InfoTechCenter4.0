# Programmer: Lucas Campbell
# Date: 1.31.2023
# Program: InfoTech Center 4.0 - Gasoline

"""
We will create a Function that will tell us out Fuel Gauge level
- Create a List with Gas Levels
- Randomize and choose from the list to determine our gas level
- Create a Functon to determine our closest Gas Station
- Create a List of gas stations
- Randomly choose a gas station from the list.
- Create a Function to determine our gas level and closest gas station
- PrintGas level
- Print Closest Gas Station
"""

import random
import time

# Gas Level Function


def gasLevelGauge():
    gasLevelList = ["Empty", "Running on Fumes", 'low', "Halfway there", "alllll good", "Full"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel


# Variable calling gasLevelGauge function to store its value
gasLevelIndicator = gasLevelGauge()

# List of Gas Stations Function


def listOfGasStations():
    gasStations = ["Shell", "Costco", "Buc-ee's", "Speedway", "7-11", "Circle-K", "Meijer", "Marathon"]
    gasStationNearby = random.choice(gasStations)
    return gasStationNearby

# Determine Gas Level & Closest Station


def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1, 25), 2)
    milesToGasStationQuarterTank = round(random.uniform(26, 50), 2)
    if gasLevelIndicator == "Empty":
        print("***WARNING YOU ARE ON EMPTY***")
        time.sleep(1)
        print("Calling emergency contact")
