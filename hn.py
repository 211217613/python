#!/usr/bin/python3

#Make sure to run this using python3
import urllib.request
import logging #https://docs.python.org/3.4/howto/logging.html#logging-basic-tutorial

top_story_ids = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
item_ids 	  = 'https://hacker-news.firebaseio.com/v0/item.json?print=pretty'
job_ids 	  = 'https://hacker-news.firebaseio.com/v0/jobstories.json?print=pretty'
jobs = list()

string = 'https://hacker-news.firebaseio.com/v0/item/{0!s}.json?print=pretty' 

def setup_logging():
	logging.basicConfig(filename='hn.log', format='%(asctime)s %(message)s', datefmt='%I:%M:%S',level=logging.INFO, filemode='w')
	logger = logging.getLogger(__name__)
	logger.info('Starting logging')

def string_formatting(html):
	#html is a string, need to strip and only leave spaces between
	logging.info("Removing commas... ")
	html = html.replace(',','')
	logging.info("html .... %s \n" % html )

	logging.info("Splitting html into space delimited sections...")
	ids = html.split()
	logging.info("Now html is a list with ids ")
	logging.info(ids)

	string = 'https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty'.format(html[::])
	jobs.append(string)
	logging.info("jobs list contains %s" % jobs)

def main():
	setup_logging()
	
	with urllib.request.urlopen(job_ids) as response:
		html = response.read()
	# Decode b' to ascii
	html = html.decode("ascii")			# this converts html into a string NOT a list
	logging.info("html before rstrip %s \n" % html)
	html = html[2 : -3] 				# This gives a string with the beginning and end stripped
	#
	logging.info("logging" )
	print("len %d " % len(html))
	string_formatting(html)


if __name__ == '__main__':
	main()