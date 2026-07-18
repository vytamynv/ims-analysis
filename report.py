import os
from datetime import datetime
import detector as dt
"""
Reporting the analysis

Author: Vytamyn
Date: July 14, 2026, (updated)
cvn
"""


def report(data, source_path):
    """
    Generating a report on essential indicators

    Args:
        data (list): a list of RMS values
        source_path (str): a string of source/folder path

    Returns:
        None
    """
    base_num = dt.baseline_cal(data)    # Calculating baseline

    # Calculating warning period
    warning_idx = 2118  # Manually
    warning_file = os.path.basename(source_path[warning_idx])
    warning_file = warning_file.replace('.csv','')
    warning_time = datetime.strptime(warning_file, "%Y.%m.%d.%H.%M.%S")

    # Critical time
    failure_file = os.path.basename(source_path[len(source_path)-1]) # last file
    failure_file = failure_file.replace('.csv','')
    failure_time = datetime.strptime(failure_file, "%Y.%m.%d.%H.%M.%S")

    warning_period_hour = (failure_time - warning_time).total_seconds()/3600
    warning_period_day = warning_period_hour/24

    current_date = datetime.now()   # Get current time
    filename = (f"Report-Early-Degradation-"
                f"{current_date.strftime('%Y-%m-%d-%H-%M-%S')}.txt")

    # Make a report
    with open(filename, "w") as f:
        f.write(f"""
EARLY BEARING DEGRADATION REPORT\n
Generated: {current_date.strftime('%Y-%m-%d %H:%M:%S')}\n
{"=" * 100 + "\n\n"}
DATASET: NASA IMS BEARING DATASET, Test 1, BEARING 1\n
TOTAL OF FILES: {len(data)}\n\n
RESULTS\n
Baseline Range: Files {base_num[0]}-{base_num[1]}\n
Baseline Mean: {base_num[2]:.6f}\n
Variance: {base_num[3]:.6f}\n\n
THRESHOLDS\n
Alert threshold (Upper): {base_num[4]:.6f}\n
Alert threshold (Lower): {base_num[5]:.6f}\n
DANGER THRESHOLD: {base_num[6]:.6f}\n\n\n
FINDINGS\n
RMS crossed the upper alert threshold at file index 2118-2119 and continued rising. At the file index 2129, it passed the danger threshold.
\nThis provided an early warning of approximately {warning_period_hour:.1f} hours or {warning_period_day:.1f} days before catastrophic failure.\n\n
ACTIONS\n
Schedule inspection immediately.\n\n"""
                )
    print("Done. The report is created.")

