import argparse
import os
import time


# Example of argparser and getting parse values
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
parser.add_argument("-m", "--mtime", help="gives the last time the file was changed", action="store_true")
parser.add_argument("-d", "--dir", help = "gets the file path")
args = parser.parse_args()
file = args.dir
print(file)
st = os.stat(file)
if args.mtime:
    print("last modified: %s" % time.ctime(st.st_mtime))
