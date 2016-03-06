#!/usr/bin/env python


import gmpy

def exper(n):
	total = 0
	for i in range(n):
		p = gmpy.rand("next", 2**512)
	print p

def main():
	exper(100)


if __name__ == '__main__':
	main()