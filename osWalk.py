#!/usr/bin/python3
"""
Traverse both local and extrnal folder
Store in lists/dicts/sets
Find duplicates
Delete duplicates from either local or external
os.walk yields a 3-tuple
dirpath: str
dirnames: list
fnames: list
"""

import os
import logging
import re

logfile  = "logging.log"
logging.basicConfig(level=logging.INFO, filename=logfile,filemode='w', format='%(message)s')

videos_external = '/media/vitoriano-vaz/External/Videos/'
videos_local	= '/media/vitoriano-vaz/Thumper/RV/Videos/'
local 		= list()
external 	= list()
fn 		 	= ""
files_txt	= True

# Text file, wanna make it more readable
# insert \n after every ','
def parse_log():
	with open(logfile,'r+') as log:
		pass
def rm_periods():
	for idx in range(len(dirname)):
		newname = dirname[idx].replace('.',' ')
		os.rename(os.path.join(dirpath,dirname[idx]), os.path.join(dirpath, newname) )
		dirname[idx] = newname

# dirname is a list. appending a list to a list
def main():
	logging.info("In main")
	cntr = 0
	# logging.info("local txt files")
	for (dirpath, dirname, filenames) in os.walk(videos_external):
		logging.info(filenames)
		for name in filenames:
			if name.endswith('.txt') and files_txt:
				print("deleting {0}".format(name) )

				cntr = cntr +1

				try:
					os.remove(name)
				except OSError:
					logging.error(OSError)
	print("num of txt files {}".format(cntr))

if __name__ == '__main__':
	main()