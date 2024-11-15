#!/usr/bin/python3
import math
import sys
import re

class NotInt(Exception):
    def __init__(self, val):
        self.val = val
    def getval(self):
        return self.val

class NegativeNumber(Exception):
    pass

class InvalidFormat(Exception):
    pass

def compute(B):
    sum = 0
    for x in B:
        sum += 1/x
        try:
            ssum = math.sqrt(sum/len(B))
        except ValueError:
            raise NegativeNumber()
    return int(100*ssum)

def getSF(A):
    B = [ ]
    for s in A:
        try:
            B.append(int(s))
        except ValueError:
            raise NotInt(s)
    return compute(B)

def arg2list(arg):
    match = re.search(r'(^[^,]+(,[^,]+)*$)', arg)
    if not match:
        raise InvalidFormat() 
    return match.group(0).split(",")
        
try:
    print(getSF(arg2list(sys.argv[1])))
except ZeroDivisionError:
    print("Error! no zeros allowed")
except IndexError:
    print("Usage: ./ex1.py <numlist>")
except ValueError:
    print("Error! there was a problem")
except NotInt as e:
    print(f'Error! element \'{e.getval()}\' not an integer')
    #print("Error! non-numeric in argument list")
except NegativeNumber:
    print("Error in compute function!")
except InvalidFormat:
    print("Error! not a comma-separated list")

