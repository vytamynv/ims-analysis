import math
"""
Calculating baseline and standard deviation

Author: Vytamyn
Date: July 13, 2027,
cvn
"""


def baseline_cal(rms_values):
    """
    Calculating baseline and standard deviation

    Args:
        rms_values (list): a list of RMS values

    Returns:
        list: a list of baseline_start, baseline_end, baseline_mean,
        baseline_std, alert1, alert2, danger
    """
    baseline_start = 542    # manually picked
    baseline_end = 2118     # manually picked

    baseline_rms = rms_values[baseline_start:baseline_end]

    # Calculate baseline mean
    sLength = len(baseline_rms)
    sigma = 0
    for k in baseline_rms:
        sigma += k

    baseline_mean = sigma / sLength

    # Calculate the variance
    squared_diff = [(x - baseline_mean)**2 for x in baseline_rms]
    tot = 0
    for i in squared_diff:
        tot += i
    variance = tot/sLength
    baseline_std = math.sqrt(variance)  # Standard Deviation

    # Calculate thresholds
    alert1 = baseline_mean + (2 * baseline_std)
    alert2 = baseline_mean - (2 * baseline_std)

    danger = baseline_mean + (5 * baseline_std)

    # print(f'Baseline Mean {baseline_mean}\nVariance {baseline_std}\n'
    #       f'Alert threshold (Upper) {alert1}\nAlert threshold (Lower) '
    #       f'{alert2}\nDANGER {danger}\n\n')

    return [baseline_start, baseline_end, baseline_mean, baseline_std, alert1,
            alert2, danger]
