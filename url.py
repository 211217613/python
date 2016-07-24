#!/usr/bin/python3
"""
Workflow for getting url's
"""
import urllib.request 	#Let me get urls. URLLIB2 newer and better?
import sys		#Let me get argv[]
import re

def main():
	print("in main")
	print(len(sys.argv))
	# for link in soup.findAll('a'):
		# print(link.get('href'))
		
	# for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
	# 	print(link.get('href'))
	if len( sys.argv ) == 1:
		url = 'http://www.google.com'
	else:
		url = sys.argv[1]


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
