#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print("usage: python3 sol1.py <file1> <file2>")
    sys.exit(0)


def fitStrInSize(s, N):
    return s + ' '*(N-len(s))

if __name__ == '__main__':
    data1 = data2 = None
    with open(sys.argv[1], 'r') as file1:
        data1 = file1.read().split("\n")
    with open(sys.argv[2], 'r') as file2:
        data2 = file2.read().split("\n")
   
    # clean the data
    data1 = [x.strip() for x in data1]
    data2 = [x.strip() for x in data2]
    
    # find the space needed for proper alignment 
    max1 = max([len(x) for x in data1])

    # make data sets the same size
    if len(data1) < len(data2):
        data1.extend( [fitStrInSize("", max1) for _ in range(len(data2)-len(data1))] )
    elif len(data2) < len(data1):
        data2.extend( ["" for _ in range(len(data1)-len(data2))] )

    # make the first dataset a uniform string length
    data1 = [fitStrInSize(x, max1) for x in data1]

    # print the two files out
    for s1, s2 in zip(data1, data2):
        print(s1 + " " + s2)

