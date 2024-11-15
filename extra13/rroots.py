from ex1a import quadraticFormula
from math import fabs, floor

_threshold = 0.0000001

def setThreshold(val):
    global _threshold
    _threshold = val

def getRealRoots(a, b, c):
    global _threshold
    # ax^2 + bx + c
    ret = []
    #print(quadraticFormula(a,b,c))
    try:
        for x in quadraticFormula(a,b,c):
            #print(fabs(x), abs(floor(x)))
            testval = (fabs(x) - abs(floor(x))) 
            if  (testval >= _threshold or testval == 0) and x not in ret: 
                ret.append(x)
    except ValueError as e:
        pass

    return ret

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print(sys.argv)
        print("usage: python3 rroots.py <a>,<b>,<c>")
        print("ex:    python3 rroots.py 1,2,1")
        sys.exit(1)
    
    nums = [float(x) for x in sys.argv[1].split(",")]
    print(getRealRoots(*nums))

