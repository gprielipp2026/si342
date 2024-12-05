#!/usr/bin/env python3



if __name__ == '__main__':
    import sys
    import os

    if len(sys.argv) != 3 and len(sys.argv) != 4:
        print("usage: python3 sol2 <-s?> <input file | - = stdin> <output file | - = stdout>")
        sys.exit(0)

    inFile = outFile = isShow = None
    # process argument inputs 
    # allows "-s" to be anywhere in the arguments
    # first file will always be interpreted as the input file
    # second file will always be interpreted as the output file
    for arg in sys.argv[1:]:
        if arg == '-s':
            isShow = True
        elif os.path.isfile(arg):
            if inFile == None:
                inFile = open(arg, 'r')
            elif outFile == None:
                outFile = open(arg, 'w')
        elif arg == '-':
            if inFile == None:
                inFile = sys.stdin 
            elif outFile == None:
                outFile = sys.stdout 

    from redactor import process, T

    # i'm not sure if we are allowed to do this
    if isShow:
        for key in T.keys():
            value = T[key]
            if 'redact' in value:
                T[key] = (value[0], 'copy')
    
    process(inFile, outFile)

