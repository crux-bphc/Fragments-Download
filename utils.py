import os
import sys
import time


def catall(title, num, path):
    # Consolidate fragments into one file
    file = path + title
    fp = open(file, "wb")
    for i in range(num):
        ftemp = open(file + ".frag" + str(i), "rb")
        fragdata = ftemp.read()
        fp.write(fragdata)
        ftemp.close()
    fp.close()
    print("Done Merging the fragments")
    for i in range(num):
        os.remove(file + ".frag" + str(i))
    print("Removed the fragments!")

def clearfragments(title, num, path):
    # Clear old fragments
    for i in range(num):
        try:
            os.remove(path + title + ".frag" + str(i))
        except:
            pass
    print("Removed the old fragments") 

def removeslash(title):
    # Generate title from URL
    try:
        return title.replace("/", " ")
    except:
        return title
