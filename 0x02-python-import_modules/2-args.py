#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    i = 0
    if len(argv) == 1:
        print("{} arguments.".format(i))       
    else:
        for agr in argv[1:len(argv)]:
            if i == 0:
                print("{} arguments.".format(len(argv) - 1))
                i +=1 
            print("{}: {}".format(i, agr))
            i += 1
