#!/usr/bin/python3
"""
Workflow for getting url's
"""
import urllib.request 	#Let me get urls. URLLIB2 newer and better?
import sys		#Let me get argv[]
import re

url  = 'https://hacker-news.firebaseio.com/'


def main():
	print("in main")

	response = urllib.request.urlopen(url)
	print ('RESPONSE:', response)
	print ('URL     :', response.geturl())

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
	# soup = BeautifulSoup(url)



if __name__ == '__main__':
	print('tessssstttt')
	main()
