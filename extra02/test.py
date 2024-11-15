#!/usr/bin/env python3

from sol import grade, nwsum 
def extract(s):
    import ast
    els = [x for x in ast.literal_eval(s)]
    return els

def test(t):
    G, W, expected = t 
    tG = grade(G, W)
    tS = nwsum(G, W)

    eG = expected[0]
    eS = expected[1]

    assert tG == eG and tS == eS

"""
This is the format, 
grade([...],[...]) = G (normsum is _.__)
"""
def cleantests(test):
    grades = extract(test[0][6:test[0].find(']')+1])
    weights = extract(test[0][test[0].find('[', test[0].find(']')):-1])
    letter = test[1][0]
    value  = float(test[1][len('x (normsum is '):test[1].find(')')])
    return (grades, weights, (letter, value))

tests = None
# I could make this a cmd line arg 
with open("tests.txt", "r") as fh:
    tests = [x.split(' = ') for x in fh.readlines()]

tests = list(map(cleantests, tests))
for t in tests:
    test(t)
