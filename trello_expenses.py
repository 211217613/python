#!/usr/bin/python3
import json
# import urllib.request
import sys
from trello import TrelloClient


TRELLO_EXPIRATION = 'never'
NAME 	= "name"
LISTS 	= "lists"
CLOSED 	= "closed" 
CARD 	= "cards"
# Developer API key
api_key = '2819ec494f41829d45bdea15e3cf20e0' # TRELLO_API_KEY
api_secret = '80cc221711c53bc6c3fab2776079e4c7' 

#OUATH
token = '0a46c305b380455a83176624e3e980fa8cfcba3b189a668558f3b03dc729a60e' # TRELLO_TOKEN: OAUTH TOKEN
oauth_secret = '47043b5293f8093f7121e233a080595855967e7cc145c82bd75f4817d6c7990b'

client = TrelloClient(api_key=api_key, api_secret=api_secret, token=token , token_secret=oauth_secret )
# Test board: https://trello.com/b/So69sspg/test-expenses

# Getting boards
board = client.list_boards()
board_info = client.info_for_all_boards(all)
board_expenses = client.get_board('So69sspg')
# board_expenses.get_list('Comidas')

for boards in board:
	print boards
