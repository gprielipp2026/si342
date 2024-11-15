from rroots import setThreshold, getRealRoots
from ex1a import quadraticFormula
from random import randint

def randCoeffs():
    return [randint(-99,99) for _ in range(3)]

def randPolyTwoRealRoot():
    coeffs = randCoeffs()
    
    while any([x == 0 for x in coeffs]) or len(getRealRoots(*coeffs)) != 2:
        #print("trying: " + str(coeffs))
        coeffs = randCoeffs()
            
    return coeffs

print("coeffs: " + str(randPolyTwoRealRoot()))
