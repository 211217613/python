#!/usr/bin/python3
"""
Workflow for getting url's
"""
import bs4 as bs
import urllib.request 	# Let me get urls. URLLIB2 newer and better?
import sys		# Let me get argv[]
import re
import requests 

URL = 'http://www.cs.fsu.edu/~redwood/OffensiveComputerSecurity/'
URL_LECTURE = 'http://www.cs.fsu.edu/~redwood/OffensiveComputerSecurity/lectures.html'

def main():
	# print(len(sys.argv))
	# for link in soup.findAll('a'):
		# print(link.get('href'))
		
	# for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
	# 	print(link.get('href'))
	if len( sys.argv ) == 1:
		url = 'http://www.google.com'
	else:
		url = sys.argv[1]

    # Get the page
	response = urllib.request.urlopen(URL_LECTURE)
	print ('RESPONSE:', response)
	print ('URL     :', response.geturl())

	# Get the bs4 object
	soup = bs.BeautifulSoup(response, 'lxml')
	print('Title: {}'.format(soup.title.string))

	# beginning navigation
	print('nav: {}'.format(soup.title.parent.name))

	# Get a paragraph <p> tags
	print('<p>: {}'.format(soup.p.name))

	# Get all <p> tags
	# for paragraph in soup.find_all('p'):
	# 	print('<p>: {}'.format(paragraph.string))

	# Get all links
	# for url in soup.find_all('a'):
	# 	print('url: {}'.format(url.get('href')))
	# 	# if 'tube' in url.get('href'):
		# 	print('url: {}'.format(url.get('href')))


	for iFrame in soup.find_all('iframe'):
		# print('iFrame: {}'.format( iFrame))
		# print('iFrame src: {}'.format( iFrame.attrs['src'][2:]))
		temp_respone = iFrame.attrs['src']
		temp_respone = 'https:' + temp_respone
		print(temp_respone)
		i_respone = urllib.request.urlopen(temp_respone)
		# print('i_respone: {}'.format(i_respone))

		# iframe_soup = bs.BeautifulSoup(i_respone)
		# print(iframe_soup)
	

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
	main()