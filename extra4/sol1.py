#!/usr/bin/env python3

def inchToFootInch(inches: int) -> str:
    ft = inches // 12
    in_= inches %  12
    return f'{inches}" = {ft}\' {in_}"'

def vowelCount(s: str) -> int:
    return len([x for x in s.lower() if x in "aeiou"])

def matchCase(s: str, r: str) -> str:
    assert len(s) == 1 and len(r) == 1

    if s.isupper():
        return r.upper()
    else:
        return r.lower()

def vowelSwap(s: str) -> str:
    lookup = { "a":"u", "u":"i", "i":"a", "o":"e", "e":"o"  }
    return "".join(map(lambda c: matchCase(c, lookup[c.lower()]) if c.lower() in lookup else c, s))

