#This program will get a directory path as input
#under that directory, if it finds .txt file, It will be changed to .doc file
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
