import matplotlib.pyplot as plt
"""
Plotting the data points

Date: July 12, 2027,
Author: Vytamyn
cvn
"""


def plot(data):
    """
    Plot the data points

    Args:
        data (list): a list contains all the RMS vibration data points

    Returns:
        None
    """
    plt.xlabel('index')
    plt.ylabel('RMS Vibration')
    plt.title('Bearing 1 RMS Trend')
    plt.plot(data, 'r', linewidth=1.0)
    plt.xlim(left=0)
    plt.grid(True, alpha=0.3)
    plt.show()





