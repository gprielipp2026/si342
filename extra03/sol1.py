#!/usr/bin/env python3
import numbers

def writish(A: list) -> list:
    B = []
    for x in A:
        # https://stackoverflow.com/questions/4187185/how-can-i-check-if-my-python-object-is-a-number
        # ^ was used to figure out below line
        if isinstance(x, numbers.Number):
            c = B.pop()
            B.extend([c]*x)
        else:
            B.append(x)
    return B

def modsetsize(N: int) -> int:
    X_N = set()
    x = 0
    for i in range(1, N+1):
        x = (x*x + x + 1) % N
        if x in X_N:
            break
        else:
            X_N.add(x)
    return len(X_N)

def convert(amt: float, curFrom: str, curTo: str) -> float:
    cfactor = {
            'Dollars US': 1.0,
            'Dollars Canadian': 1.3156,
            'Euros': 0.9018,
            'Pounds': 0.7614
            }

    cRatio = cfactor[curTo] / cfactor[curFrom]
    return amt * cRatio
