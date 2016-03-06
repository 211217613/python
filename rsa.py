#!/usr/bin/python

import os
print "python"

def gen_rsa_parameters():
	r = os.urandom(63)  //returns a string 
	print r
	print "pythonnn"

	e = int(r.encode('hex'), 16)