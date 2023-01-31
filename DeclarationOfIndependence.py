# Programmer: Lucas Campbell
# Date: 1/23/2023
# Program: InfoTech Center 4.0

"""
Our Welcome Screen will start our program letting
drivers know that the InfoTech Center 4.0 OS is loading
"""

import time
import sys


print("Welcome - InfoTech Center 4.0")
print("")

time.sleep(2)

x = 0
a = 0

while x != 20:
    x += 1
    b = ("\033[1;33;40m InfoTech Center is Loading" + "." * a)
    a = a + 1
    sys.stdout.write('\r'+b) # \r prints a carriage return first, so `b` is printed on top of the previous line.
    time.sleep(0.5)
    if a == 4:
        a = 0
    if x == 20:
        print('\033[1;32;40m Complete!')


