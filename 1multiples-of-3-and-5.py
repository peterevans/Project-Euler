#!/usr/bin/env python
# encoding: utf-8


import sys
import os


def multiples(number):
	i = 0
	total = 0
	while i < number:
		if i % 3 == 0 or i % 5 == 0:
			total = total + i
			i = i + 1
		else:
			i = i + 1
	return total
	
print multiples(1000)


