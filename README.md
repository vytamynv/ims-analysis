# Early Degradation Detection in Rotating Machinery using Vibration RMS Trend Analysis
Author: Vytamyn (CVN)\
Date: July 13, 2027
## Abstract
This project aims to visualize early signals of potential degradation of the bearing by processing 2000+ of accelerometer vibration data files from the NASA IMS bearing dataset. RMS values are computed to plot over moments of time and they produce a continuous sharp rise above baseline before failure.
## Introduction
Rolling element bearings are crucial components in industrial machinery. Vibration analysis is the standard method for condition monitoring, with RMS (root-mean-square) acceleration serving as a proxy for vibration energy. A rising RMS trend indicates developing defects (spalling, cracking, wear etc.)
## Composition
There are 6 support files and 1 main file to run the program as shown below:

1. convert_files.py
2. files_control.py
3. rms_cal.py
4. ims_plot.py
5. detector.py
6. report.py
7. main.py

All of them are written in Python. Version 3.0+ is strongly recommended. 
## Execution
To run the program, first of all, a user needs to navigate the folder path leading to the IMS vibration data and paste it as the variable for "sf" in "convert_files.py". This way, they can convert all the files to csv files, which are convenient to execute and if they want to check things manually with Excel, csv can also help. 

Then, run the "main.py".

It might take some seconds to minutes (it shouldn't last more than 5 minutes 
unless your device is ancient or you don't run the proper file) due to the heavy load of data points.
## Methodology
1. Converted raw files to CSV
2. Extracted Bearing 1, 1st test
3. Computed RMS per file
4. Established baseline from stable operating region
5. Applied statistical thresholds for alert and danger
## Results
## Conclusion
