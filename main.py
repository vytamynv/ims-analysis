import os
import files_control as fc
import rms_cal as rms
import ims_plot as plt
import convert_files as cf


"""
This project aims to analyze and predict the trend of IMS bearing from NASA.

To be more specific, the main goal is to produce a single plot of RMS 
vibration vs. time for Bearing 1 illustrating the 
moment degradation starts. 

Source:
https://data.nasa.gov/dataset/ims-bearings

Author: Vytamyn
cvn
"""


def main():
    # Getting all the files and having a list of filepaths
    source_path = cf.source_path()
    print(source_path)
    filepath = sorted([os.path.join(source_path, f)
                       for f in os.listdir(source_path)
                       if os.path.isfile(os.path.join(source_path, f))])

    all_rms = []
    for f in filepath:
        raw = fc.load_raw_data(f)
        val = fc.format_data(raw)
        rms_val = rms.rms(val)
        all_rms.append(rms_val)

    # print("Bearing 1's values", val)
    # print(all_rms)
    # print("Length of rms values list ", len(all_rms))
    plt.plot(all_rms)





if __name__ == "__main__":
    main()



