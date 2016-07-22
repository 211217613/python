#!/usr/bin/python3
import json
import urllib.request
import sys
from trello import TrelloClient
# import trello

TRELLO_EXPIRATION = 'never'
NAME 	= "name"
LISTS 	= "lists"
CLOSED 	= "closed" 
CARD 	= "cards"
# Developer API key
key = '2819ec494f41829d45bdea15e3cf20e0'

# secret key
secret_key = '0a46c305b380455a83176624e3e980fa8cfcba3b189a668558f3b03dc729a60e'

# OAuth
oauth_secret = '47043b5293f8093f7121e233a080595855967e7cc145c82bd75f4817d6c7990b'

# url = 'https://trello.com/b/BE89pW61/expenses.json'
# url = 'https://trello.com/b/BE89pW61/expenses.json'
try:
	url = 'https://trello.com/b/BE89pW61.json'
	respone = urllib.request.urlopen(url)
except:
	e = sys.exc_info()[0]
	print(e)

with open('./expenses.json', 'r') as json_file:
	trello_board = json.load(json_file)
print( "Board: {}".format(trello_board[NAME]) )

for trello_list in trello_board[LISTS]:
	if not trello_list [CLOSED]:
		print("Lists: " + trello_list [NAME])
		for trello_card in trello_board[CARD]:
			print("Cards: " + trello_card[NAME])



# response = urllib.request.urlopen(url)
# html = response.read()
# html = html.decode('')

# client  = TrelloClient( 
# 	key,
# 	secret_key
# 	token,
# 	secret_token  )

