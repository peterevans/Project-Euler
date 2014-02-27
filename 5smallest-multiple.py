#!/usr/bin/env python
# encoding: utf-8


import sys
import os

def smallmult(n):
	i = 1
	max = n
	while i <= n:
		if max % i == 0:
			i = i + 1
		else:
			max = max + 1
			i = 1
	return max
	
print smallmult(20)


