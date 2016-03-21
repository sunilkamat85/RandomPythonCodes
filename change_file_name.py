import os, glob
from sys import argv
dir_path = argv[1]
files_in_dir = glob.glob(dir_path + "/*.txt")
if len(files_in_dir) > 0:
        for i in files_in_dir:
                new = i.split('.')[0]
                new = new + ".doc"
                os.rename(i, new)
        print "renamed all files"
else:
        print " No files starting with .txt "
