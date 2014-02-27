#!/usr/bin/env python
# encoding: utf-8


import sys
import os

def fib(n):
    if n < 2:
		return n
    else:
		return (fib(n - 1) + fib(n - 2))

def fibsum(endpoint):
	total = 0
	n = 0
	while fib(n) < endpoint:
		if fib(n) % 2 == 0:
			total = total + fib(n)
			n = n + 1
		else:
			n = n + 1
	return total
			
		
print fibsum(4000000)


