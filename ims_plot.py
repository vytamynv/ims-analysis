import matplotlib.pyplot as plt
import detector as dt
"""
Plotting the data points

Date: July 12, 2026,
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
    # Add axis' labels
    plt.xlabel('index')
    plt.ylabel('RMS Vibration')

    # Add title
    plt.title('Bearing 1 RMS Trend')

    # Plot
    plt.plot(data, 'b', linewidth=0.5)
    plt.xlim(left=0)    # x-axis root
    plt.grid(True, alpha=0.3)

    # Getting baseline values
    # Data from all_rms[]; idx value
    # #0 baseline_start, #1 baseline_end, #2 baseline_mean, #3 baseline_std,
    # #4 alert1, #5 alert2, #6 danger
    base_num = dt.baseline_cal(data)

    # Baseline Zone
    plt.axvspan(base_num[0], base_num[1], alpha=0.1, color='green',
                label=f'Baseline Zone (files {base_num[0]}-{base_num[1]})')

    # Adding variance lines
    plt.axhline(y=base_num[2], color='green', linestyle='-',
                label=f'Baseline Mean: {base_num[2]:.4f}')
    plt.axhline(y=base_num[4], color='orange', linestyle='--',
                label=f'Alert (mean + 2σ): {base_num[3]:.4f}')
    plt.axhline(y=base_num[5], color='orange', linestyle='--',
                label=f'Alert (mean - 2σ): {base_num[4]:.4f}')
    plt.axhline(y=base_num[6], color='red', linestyle='-.',
                label=f'Danger: {base_num[5]:.4f}')

    plt.legend()    # Add legends
    plt.show()






