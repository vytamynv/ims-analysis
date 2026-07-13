import os
# To execute files
import files_control as fc
# To calculate RMS
import rms_cal as rms
# To plot the data points
import ims_plot as plt
# To convert raw data into .csv
import convert_files as cf
# To write a report
import report as rp
"""
This project aims to analyze and predict the trend of IMS bearing from NASA.

To be more specific, the main goal is to produce a single plot of RMS 
vibration vs. time for Bearing 1 illustrating the 
moment degradation starts. 

Source:
https://data.nasa.gov/dataset/ims-bearings

Date: July 13, 2027 (updated),
Author: Vytamyn
cvn
"""


def main():
    """
    Run the program

    Args:
        None

    Return:
        None

    """
    # Getting all the files and having a list of filepaths
    source_path = cf.source_path()[0]
    filepath = sorted([os.path.join(source_path, f)
                       for f in os.listdir(source_path)
                       if os.path.isfile(os.path.join(source_path, f))])

    all_rms = []
    for f in filepath:
        raw = fc.load_raw_data(f)
        val = fc.format_data(raw)
        rms_val = rms.rms(val)
        all_rms.append(rms_val)

    plt.plot(all_rms)

    report_ask = input("Do you want to have a brief report? [Y/N]: ")
    while (report_ask.lower().strip() != 'y' and report_ask.lower().strip() !=
           'n'):
        report_ask = input("Do you want to have a brief report? [Y/N] only: ")

    if report_ask == 'y':
        rp.report(all_rms, filepath)
    else:
        print("FINISHED")


if __name__ == "__main__":
    main()
# cvn


