# coding=utf-8

import math

def pi(n):
	s = 0.0 
	for i in range(n+1):
		s+= 1.0/(2*i+1)/(2*i+1)
	return math.sqrt(8*s)


def flb(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return flb(n-1)+flb(n-2)
