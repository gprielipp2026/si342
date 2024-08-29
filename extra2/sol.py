#!/usr/bin/env python3

def sum(A: list) -> float:
    total = 0.0
    for num in A:
        total += num
    return total

def wsum(G: list, W: list) -> float:
    assert len(G) == len(W)
    total = 0.0
    for grade, weight in zip(G, W):
        total += grade * weight
    return total

def nwsum(G: list, W: list) -> float:
    assert len(G) == len(W)
    
    totalSum = wsum(G, W)
    totalWeight = sum(W)
   
    assert totalWeight != 0
    return totalSum / totalWeight

def grademap(x: float) -> str:
    assert x >= 0 and x <= 100
    if x >= 90:
        return 'A'
    elif x >= 78:
        return 'B'
    elif x >= 66:
        return 'C'
    elif x >= 50:
        return 'D'
    else:
        return 'F'

def grade(G: list, W: list) -> str:
    return grademap(nwsum(G, W))


