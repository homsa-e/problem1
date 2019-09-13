import argparse
import os
import time


# Example of argparser and getting parse values
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
parser.add_argument("-m", "--mtime", help="gives the last time the file was changed, possible formats: DD.MM.YY, DD.MM.YY HH:MM or full info as a default. To choose print -f=1 or -f=2 as a next command", action="store_true")
parser.add_argument("-f", "--format", help="chooses the time format")
parser.add_argument("-d", "--dir", help="gets the file path")
parser.add_argument("-s", "--size", help="gives the size of the file", action="store_true")
parser.add_argument("-r", "--rename", help="gives the file a new name (type it)")
args = parser.parse_args()
file = args.dir
st = os.stat(file)
if args.mtime:
    t = time.gmtime(st.st_mtime)
    if args.format == "1":
        t = time.strftime("%d.%m.%y", t)
    elif args.format == "2":
        t = time.strftime("%d.%m.%y %H:%M", t)
    else:
        t = time.ctime(st.st_mtime)
    print(t)
if args.size:
    print("file size: %s" % st.st_size)
if args.rename:
    os.rename(file, args.rename)
