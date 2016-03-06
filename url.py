#!/usr/bin/env python

import urllib2 	#Let me get urls. URLLIB2 newer and better?
import sys		#Let me get argv[]

from BeautifulSoup import BeautifulSoup
import re


url = sys.argv[1]


response = urllib2.urlopen(url)
print 'RESPONSE:', response
print 'URL     :', response.geturl()

headers = response.info()
# print 'DATE    :', headers['date']
# print 'HEADERS :'
# print '---------'
# print headers

data = response.read()
# print 'LENGTH  :', len(data)
# print 'DATA    :'
# print '---------'
# print data
soup = BeautifulSoup(url)

def main():
	print("in main")

	# for link in soup.findAll('a'):
		# print(link.get('href'))
		
	for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
		print(link.get('href'))




if __name__ == '__main__':
    main()
