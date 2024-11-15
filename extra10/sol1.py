#!/usr/bin/python3

class CountdownIterator:
    def __init__(self,N, lower):
        self.count = N
        self.lower = lower

    def __next__(self):
        if self.count == self.lower - 1:
            raise StopIteration
        res = self.count
        self.count -= 1
        return res

class Countdown:
    def __init__(self,N, lower=1):
        if lower > N:
            raise Exception("lower bound is greater than upper bound")
        self.N = N
        self.lower = lower

    def __iter__(self):
        return CountdownIterator(self.N, self.lower)

class Fiberator:
    def __init__(self, numVals):
        self.seq = {0: 1, 1: 1} 
        self.count = 0 
        self.max = numVals

    def fib(self, x):
        if x in self.seq:
            return self.seq[x]
        else:
            self.seq[x] = self.fib(x-1) + self.fib(x-2)
            return self.seq[x]

    def __next__(self):
        if self.count == self.max:
            raise StopIteration
        ret = self.fib(self.count)
        self.count += 1
        return ret 

class Fibseq:
    def __init__(self, lenSeq):
        self.lenSeq = lenSeq

    def __iter__(self):
        return Fiberator(self.lenSeq)

def first2(itr):
    itr = iter(itr)
    return (next(itr), next(itr))


A = ['u','b','w','p','k','z']
B = [5,9,2,7,1,6]

A2B = {x:y for x,y in zip(A, B)}
print(A2B)

with open("in1.txt", "r") as f:
    data = [x.strip() for i,x in zip(range(1,7), f) if i in [2,5,6]]
    print(data)

