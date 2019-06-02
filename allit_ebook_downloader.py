#!/usr/bin/env python

# ref: https://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python

from bs4 import BeautifulSoup
import lxml.etree
import requests
import sys

def download(url):
    get_resp = requests.get(url, stream=True)
    file_name = url.split('/')[-1]
    print(file_name)
    size = int(get_resp.headers['Content-Length'])
    size_kb = size / 1024
    print(f"size:\t{size}")
    print(f"size kb:\t{size_kb}")
    with open(file_name, 'wb') as f:
        for chunk in get_resp.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

if len(sys.argv) > 1:
    url = sys.argv[1]
    print(url)
else:
    raise

page = requests.get(url)

soup = BeautifulSoup(page.content, 'lxml')
l = []
for links in soup.find_all('a', attrs={'target': '_blank'}):
    l.append(links.get('href'))
print(l)

for links in l:
    download(links)


