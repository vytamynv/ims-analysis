import math
"""
Take in values to calculate RMS

Date: July 12, 2027,
Author: Vytamyn
cvn
"""


def rms(source):
    """
    Calculate RMS values

    Args:
        source (list): a list contains raw collected data

    Returns:
        float: a calculated RMS vibration value
    """
    # Square the values
    squared = []
    for i in source:
        tmp = i**2
        squared.append(tmp)
    # print("squared values ", squared)

    # Mean calculation
    sLength = len(squared)
    total = 0
    for k in squared:
        total += k

    avg = total/sLength
    # print("mean ", avg)

    # Root
    r = math.sqrt(avg)
    return r



# exp = [1,2,3,4,5]
# print(rms(exp))
