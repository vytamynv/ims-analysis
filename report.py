import os
from datetime import datetime
import detector as dt
"""
Reporting the analysis

Author: Vytamyn
Date: July 14, 2027, (updated)
cvn
"""


def report(data, source_path):
    base_num = dt.baseline_cal(data)

    warning_idx = 2118  # Manually
    warning_file = os.path.basename(source_path[warning_idx])
    warning_file = warning_file.replace('.csv','')
    warning_time = datetime.strptime(warning_file, "%Y.%m.%d.%H.%M.%S")

    failure_file = os.path.basename(source_path[len(source_path)-1]) # last file
    failure_file = failure_file.replace('.csv','')
    failure_time = datetime.strptime(failure_file, "%Y.%m.%d.%H.%M.%S")

    warning_period_hour = (failure_time - warning_time).total_seconds()/3600
    warning_period_day = warning_period_hour/24

    current_date = datetime.now()
    filename = (f"Report-Early-Degradation-"
                f"{current_date.strftime('%Y-%m-%d-%H-%M-%S')}.txt")
    with open(filename, "w") as f:
        f.write("EARLY BEARING DEGRADATION REPORT\n")
        f.write(f"Generated: "
                f"{current_date.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 100 + "\n\n")
        f.write("DATASET: NASA IMS BEARING DATASET, Test 1, BEARING 1\n")
        f.write(f"TOTAL OF FILES: {len(data)}\n\n")
        f.write("RESULTS\n")
        f.write(f"Baseline Range: Files {base_num[0]}-{base_num[1]}\n")
        f.write(f"Baseline Mean: {base_num[2]:.6f}\n")
        f.write(f"Variance: {base_num[3]:.6f}\n\n")
        f.write("THRESHOLDS\n")
        f.write(f"Alert threshold (Upper): {base_num[4]:.6f}\n")
        f.write(f"Alert threshold (Lower): {base_num[5]:.6f}\n")
        f.write(f"DANGER THRESHOLD: {base_num[6]:.6f}\n\n\n")
        f.write(f"FINDING\n")
        f.write(f"RMS crossed the upper alert threshold at file index "
                f"2118-2119 and continued rising. At the file index 2129, "
                f"it passed the danger threshold. This provided an early "
                f"warning of approximately {warning_period_hour:.1f} hours "
                f"or "
                f"{warning_period_day:.1f} days "
                f"before catastrophic failure.\n\n")
        f.write("ACTIONS\n")
        f.write("Schedule inspection immediately.\n\n")

    print("Done. The report is created.")

