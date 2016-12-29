#!/usr/bin/python3
"""
Workflow for getting url's
"""
import requests	#Let me get urls. URLLIB2 newer and better?
import sys		#Let me get argv[]
import re
from multiprocessing import Pool
import bs4
import random
import string

URL = 'https://sysforensics.org/'
def starting():
	# for _ in range(3):
	# 	starting = ''.join(random.SystemRandom().choice(string.ascii_lowercase))
	starting = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(3))
	url = ''.join(['http://', starting, '.com'])
	print(url)


#
def get_links(URL):
	try:
		resp = requests.get(URL)
		soup = bs4.BeautifulSoup(resp.text, 'lxml')
		links = [link.get('href') for link in soup.find_all('a')]
		# remove hashtags
		# links = [links.remove(link) for link in links if link.startswith('#')]
		for link in links:
			if link.startswith("#"):
				links.remove(link)
		print(links)
	except IndexError as e:
		print(e)
		print('Probably no Links')

	# print ('RESPONSE:', resp)
	# print ('body     :', body)

def main():
	if len( sys.argv ) == 1:
		url = 'http://www.google.com'
	else:
		url = sys.argv[1]

	# starting()
	get_links(URL)

	proc = Pool(processes=50)
	# for link in soup.findAll('a'):
		# print(link.get('href'))

	# for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
	# 	print(link.get('href'))


if __name__ == '__main__':
	main()
