import os
import shutil
"""
Converting files into .csv

Date: July 12, 2027,
Author: Vytamyn
cvn
"""


def source_path():
    """
    Convert all files to .csv

    Args:
        None

    Returns:
        str: a path to the folder containing all the csv files
    """
    # sf = r"<folderpath>"
    sf = r"D:\Astronomy\nasa-ims-bearing\IMS\IMS\1st_test\1st_test"
    csv_folder = os.path.join(os.path.dirname(sf), "csv_files")
    os.makedirs(csv_folder, exist_ok=True)  # surpass existed folder

    # Getting all files
    all_files = sorted([f for f in os.listdir(sf) if os.path.isfile(os.path.join(
        sf, f))])

    # Tracking
    count = 0
    for f in all_files:
        old_path = os.path.join(sf, f)
        new_path = os.path.join(csv_folder, f + ".csv")
        shutil.copy2(old_path, new_path)
        count += 1

    print(f"Done. {count} files copied to: {csv_folder}")
    return csv_folder, count






