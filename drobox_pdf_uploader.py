#!/usr/bin/python3
import os
import sys
import argparse

import dropbox
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError
"""
 Scan home directory for all pdf once a week and upload them to a dropbox folder
 Reqs: Identify duplicates and don't push them

Traverse home directory and search for all PDFs 

"""
TOKEN = 'JkBtVwVdzbAAAAAAAAABdvHIzPTFZ8NUF7bhVKl5zi-8RhM05cRk-DpdXkbg0mDO'
# app_key = 'wca075sjdfy99wu'
# app_secret = ''
# access_token = 'JkBtVwVdzbAAAAAAAAABdvHIzPTFZ8NUF7bhVKl5zi-8RhM05cRk-DpdXkbg0mDO'

LOCALFILE = './dropbox_pdf_uploader.py'
BACKUPPATH = '/my-file-backup.txt'

def backup():
	with open(LOCALFILE, 'rb') as f: # rb read in binary mode?
		print("Uploading {} to dropbox as {} ...".format(LOCALFILE, BACKUPPATH) )
		try:
			dbx.files_upload(f, BACKUPPATH, mode=WriteMode('overwrite') )
		except ApiError as err:
			#CHecks for the specific error user doesn't ahve enough space
			if (err.error.is_path() and  err.error.get_path().error.is_insufficient_space() ):
				sys.exit("Err: not enough space")
			elif err.user_message_text:
				print(err.user_message_text)
				sys.exit()
			else:
				print(err)
				sys.exit()

def change_local_file(new_content):
	pass

	
parser = argparse.ArgumentParser(description='Sync ~/Downloads to Dropbox')
parser.add_argument('files', nargs='?', default='PDF', help='PDF files')

def get_pdfs():
	for root, dir, files in os.walk('/home/user'):
		print(root)

def main():
	args = parser.parse_args()

	get_pdfs()

	if ( len (access_token) == 0 ):
		sys.exit("Error: Looks like you didint add your access token")

# @contextlib.contextmanager
# def stopwatch(message):
	"""Context manager to print how long a block of code took."""
	t0 = time.time()
	try:
		yield
	finally:
		t1 = time.time()
		print('Total elapsed time for {}: {}'.format(message, t1 - t0) )


if __name__ == '__main__':
	main()