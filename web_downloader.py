#!/usr/bin/python3
"""
Workflow for getting url's
"""
import pdfkit
import requests	#Let me get urls. URLLIB2 newer and better?
import sys		#Let me get argv[]
import re
import bs4
import random
from pprint import pprint

URL = 'https://blog.filippo.io/'
def starting():
	# for _ in range(3):
	# 	starting = ''.join(random.SystemRandom().choice(string.ascii_lowercase))
	starting = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(3))
	url = ''.join(['http://', starting, '.com'])
	print(url)

def remove_non_blogposts(links):
	""" Blog posts are organized by date, this function extracts only links with dates"""
	blog_links = list()
	blog_links = [ x for x in links if re.search(r'/\d{4}', x)]
	blog_links = blog_links[0::2] # Entries are duplicated

	return blog_links

def get_links(URL):
	try:
		resp = requests.get(URL)
		soup = bs4.BeautifulSoup(resp.text, 'lxml')
		links = [link.get('href') for link in soup.find_all('a')]
		pprint(links)

	except IndexError as e:
		print(e)
		print('Probably no Links')
	with open('all_links.txt', 'w') as f:
		pprint(links, stream=f)

	return links

def reconstruct_full_link(links):
	blog_links = [URL + x for x in links]
	return blog_links

def convert_to_pdf(links):
	for entry in links:
		name = entry.split('/')[-2]
		# li = zip(entry,name)
		# print(type(name[-2]))
		# print(str(entry))
		pdfkit.from_url(str(entry), '{file_name}.pdf'.format(file_name=str(name)) )



def main():
	global URL
	# if len(sys.argv) == 2:
	# 	URL = sys.argv[1]
	# else:
	# 	print('Usage: script URL')
	# 	sys.exit(1)

	page_links = get_links(URL)
	page_links = remove_non_blogposts(page_links)
	page_links = reconstruct_full_link(page_links)
	with open('urls.txt', 'w') as f:
		pprint(page_links, stream=f)
	convert_to_pdf(page_links)

if __name__ == '__main__':
	main()
