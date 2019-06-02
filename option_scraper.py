#!/opt/anaconda/python3

# ref http://www.blackarbs.com/blog/how-to-build-a-sequential-option-scraper-with-python-and-requests/7/8/2017

import requests


class BarchartScraper(object):
    def __init__(self, symbol):
        self.__request_headers = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate, sdch, br",
            "Accept-Language": "en-US,en;q=0.8",
            "Connection": "keep-alive",
            "Host": "core-api.barchart.com",
            "Origin": "https://www.barchart.com",
            "Referer": "https://www.barchart.com/etfs-funds/quotes/SPY/options",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",        
            }


def main():
    b = BarchartScraper('TSLA')


if __name__ == '__main__':
    main()