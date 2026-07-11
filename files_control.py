"""
These functions manipulate files.
"""


def load_raw_data(source):
    rawData = []
    file = open(source, "r")
    tmp = file.readline().strip()

    while tmp:
        rawData.append(tmp)
        tmp = file.readline().strip()
    file.close()
    return rawData


def format_data(rdata):
    val = []
    for dline in rdata:
        dline = dline.split("\t")
        tmp = dline[0].replace('\U00002013', '-')   # Take negative numbers
        val.append(float(tmp))
    return val









