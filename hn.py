#!/usr/bin/python3

#Make sure to run this using python3
import urllib.request
import logging 

top_story_ids = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
item_ids 	  = 'https://hacker-news.firebaseio.com/v0/item.json?print=pretty'
job_ids 	  = 'https://hacker-news.firebaseio.com/v0/jobstories.json?print=pretty'
job1 		  = 'https://hacker-news.firebaseio.com/v0/item/11500588.json?print=pretty'


def setup_logging():
	logging.basicConfig(filename='hn.log', level=logging.INFO)
	logger = logging.getLogger(__name__)
	logger.info('Starting logging')

def main():
	setup_logging()
	
	with urllib.request.urlopen(job1) as response:
		html = response.read()
	# Decode b' to ascii
	html = html.decode("ascii")
	length = len(html)
	print(length)
	e1 = top_story_ids[0]
	# for element in e1:
	# 	print(element)
	print(html)
	# if 'meta' in html:
	# 	print("sdf")


if __name__ == '__main__':
	main()