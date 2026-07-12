"""
Manipulating files

Date: July 12, 2027,
Author: Vytamyn
cvn
"""


def load_raw_data(source):
    """
    Load/Read files

    Args:
        source (str): a string of folder/files path

    Returns:
        list: a list of raw data
    """
    rawData = []
    file = open(source, "r")
    tmp = file.readline().strip()

    while tmp:
        rawData.append(tmp)
        tmp = file.readline().strip()
    file.close()
    return rawData


def format_data(rdata):
    """
    Format data obtained from files

    Args:
        rdata (list): a list of raw data

    Returns:
        list: a list of formatted (float) values
    """
    val = []
    for dline in rdata:
        dline = dline.split("\t")
        tmp = dline[0].replace('\U00002013', '-')   # Take negative numbers
        val.append(float(tmp))
    return val









