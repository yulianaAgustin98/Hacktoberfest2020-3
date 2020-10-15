#!/usr/bin/env python
import math

def circumference(r):
    return r * 2 * math.pi

def area(r):
    return math.pi * (r ** 2)

print("Circumference of circle with radius 5: " + str(circumference(5)))
print("Area of circle with radius 5: " + str(area(5)))
