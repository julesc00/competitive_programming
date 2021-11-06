"""
math
    This module contains mathematical functions and constants such as log,
    sqrt, pi, etc. Python operates on integers with arbitrary precision, thus there
    is no limit on their size. As a consequence, there is no integer equivalent to
    represent −∞ or +∞. For floating point numbers on the other hand, float(’-
    inf’) and float(’inf’) can be used. Beginning with Python 3.5, math.inf (or
    from math import inf) is equivalent to float(’inf’).
fractions
    This module exports the class Fraction, which allows computations
    with fractions without the loss of precision of floating point calculations. For
    example, if f is an instance of the class Fraction, then str(f) returns a string
    similar to the form “3/2”, expressing f as an irreducible fraction.
bisect
    Provides binary (dichotomous) search functions on a sorted list.
heapq
    Provides functions to manipulate a list as a heap, thus allowing an element
    to be added or the smallest element removed in time logarithmic in the size of
    the heap; see Section 1.5.4 on page 22.
string
    This module provides, for example, the function ascii_lowercase, which
    returns its argument converted to lowercase characters. Note that the strings
    themselves already provide numerous useful methods, such as strip, which
    removes whitespace from the beginning and end of a string and returns the
    result, lower, which converts all the characters to lowercase, and especially
    split, which detects the substrings separated by spaces (or by another separator
    passed as an argument). For example, “12/OCT/2018”.split(“/”) returns
    [“12”, “OCT”, “2018”].
Packages
"""
import os
from math import sqrt
from collections import Counter, defaultdict
import fractions

print(sqrt(4))
print(3.5)

c = Counter()
c["a"] = 1

c = Counter("julio")
print(c)

g = defaultdict(list)
print(g)
g["city"].append("Marseille")  # "City" key is created on the fly.
g["city"].append("Lyon")
print(g)

# Copying a list
a_list = [1, 2, 3]
b_list = a_list[:]  # b_list becomes a distinct copy of a_list
b_list.append(4)
print(a_list)
print(b_list)

# square matrix initialization
M1 = [[0] * 10 for _ in range(10)]
M2 = [[0 for j in range(10)] for i in range(10)]
print(M2)

M = 2
instance = list(map(int, os.read(0, M).split()))
print(instance)
