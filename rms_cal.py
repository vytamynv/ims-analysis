import math
"""
Take in values to calculate RMS
"""


def rms(source):
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
