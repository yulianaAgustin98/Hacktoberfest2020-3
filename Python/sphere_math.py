#!/usr/bin/env python3
import math

def volume(r):
    v = (4 / 3) * math.pi * (r ** 3)
    return v

def area(r):
    a = 4 * math.pi * r ** 2
    return a

print("Volume of sphere with radius 5: " + str(volume(5)))
print("Area of sphere with radius 5: " + str(area(5)))
