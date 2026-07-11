import os
import shutil

"""
Converting files into .csv
"""


def source_path():
    sf = r"<folderpath>"

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
    return csv_folder






