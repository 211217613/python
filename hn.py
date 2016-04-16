#!/usr/bin/python3

#Make sure to run this using python3
import urllib.request
import logging 

base_url = 'https://hacker-news.firebaseio.com/'
with urllib.request.urlopen(base_url) as response:
	html = response.read()
# html = html.encode("ascii")
length = len(html)
print(length)
