#!/usr/bin/env python
# encoding: utf-8


import sys
import os

def squarediff(max):
	i = 0
	sumsquare = 0
	while i <= max:
		sumsquare = sumsquare + i**2
		i = i + 1
	i = 0
	squaresum = 0
	while i <= max:
		squaresum = squaresum + i
		i = i + 1
	return squaresum**2 - sumsquare
	
print squarediff(100)


