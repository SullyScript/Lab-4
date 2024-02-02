# ECOR 1041 Lab 4

__author__                =                   "Emily              Causi"
__student_number__ = "101236902"

import math
# =====================================================
# Exercise 1

# Type your function definition for Exercise 1 here.
def area_of_disk(radius: float) -> float:
    """ Return the area of a disk with the specified radius.
    Parameters: radius > 0.
    >>> area_of_disk(3.0) 
    28.27
    >>> area_of_disk(5.3) 
    88.25
    >>> area_of_disk(7.9) 
    196.07
    """
    return round(math.pi * radius ** 2,2)

# =======================================================
# Exercise 2

# Type your function definition for Exercise 2 here.
LITRES_PER_GALLON = 4.54609
KMS_PER_MILE = 1.60934
def convert_to_litres_per_100_km(mpg: float) -> float:
    """ Convert miles per gallon into litres per 100 kilimetre. 
    Parameters: mpg != 0.
    >>> convert_to_litres_per_100_km(27.2)
    10.39
    >>> convert_to_litres_per_100_km(34.1)
    8.28
    >>> convert_to_litres_per_100_km(17.4)
    16.23
    """
    return round((100 * LITRES_PER_GALLON) / (KMS_PER_MILE * mpg),2)

# =======================================================
# Exercise 3

# Type your function definition for Exercise 3 here.
def accumulated_amount(principal: float, rate: float, n: int, time: int) -> float:
    """ Calculates future amount of money from interest rate over specified amount of time.
    Parameters: principal > 0, rate > 0, time > 0, n > 0.
    >>> accumulated_amount(1200, 0.02, 2, 3)
    1273.82
    >>> accumulated_amount(900, 0.07, 4, 1)
    964.67
    >>> accumulated_amount(1350, 0.03, 2, 3)
    1476.15
    """
    return round(principal * ((1 + (rate / n)) ** (n * time)),2)

# =======================================================
# Exercise 4

# Type your function definition for Exercise 4 here.
def area_of_cone(height: float, radius: float) -> float: 
    """ Return area of cone provided a height and radius.
    Parameters: height > 0, radius > 0.
    >>> area_of_cone(3.3, 4.2)
    182.88
    >>> area_of_cone(2.0, 7.1)
    316.74
    >>> area_of_cone(5.5, 8.4)
    1219.19
    """
    return round((math.pi * radius) * math.sqrt((radius ** 2) * (height ** 2)),2)

# =======================================================
# Exercise 5

# Type your function definitions for Exercise 5 here.
def distance(x1: int, y1: int, x2: int, y2: int) -> float:
    """ Return distance between 2 points.
    Parameters: x1 < x2, y1 < y2, x2 < 0, y2 < 0.
    >>> distance(2.3, 1.7, 5.8, 9.4)
    8.46
    >>> distance(3.0, 4.8, 5.2, 7.2)
    3.26
    >>> distance(6.2, 1.3, 7.0, 5.0)
    3.79
    """
    return round(math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2)),2)

def area_of_circle(xc: int, yc: int, xp: int, yp: int) -> float:
    """ Return area of a circle by calling on 2 already defined functions.
    Parameters: xc < xp, yc < yp.
    >>> area_of_circle(3, 5, 7, 9)
    100.64
    >>> area_of_circle(2, 1, 6, 4)
    78.54
    >>> area_of_circle(5, 3, 8, 6)
    56.48
    """
    return area_of_disk(distance(xc, yc, xp, yp))