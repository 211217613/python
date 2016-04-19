#!/usr/bin/python3

import os
import argparse
import logging


"""
This script will save specefic rc files likes bashrc
"""

#have alist of rc files
try:
	fd = open("rc.files")
except FileIOerror, e:
	print("cant open file")
	logging.error("cant open file")



for line in fd:
	print(line.rstrip())