#!/usr/bin/python
import gmpy2
import os

def gen_rsa_parameters():
	r = os.urandom(63)  #returns a string 
	print (r)
	print ("pythonnn")

	e = int(r.encode('hex'), 16)

def main():
	gen_rsa_parameters()

if __name__ == '__main__':
	main()