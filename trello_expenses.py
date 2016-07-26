#!/usr/bin/python3
import json
# import urllib.request
import sys
from trello import TrelloClient

# Developer API key
api_key = '2819ec494f41829d45bdea15e3cf20e0' # TRELLO_API_KEY
api_secret = '80cc221711c53bc6c3fab2776079e4c7' 

#OUATH
token = '0a46c305b380455a83176624e3e980fa8cfcba3b189a668558f3b03dc729a60e' # TRELLO_TOKEN: OAUTH TOKEN
oauth_secret = '47043b5293f8093f7121e233a080595855967e7cc145c82bd75f4817d6c7990b'

# Test board: https://trello.com/b/So69sspg/test-expenses

# Getting boards
# Returns a non-itereable board object


# Returns a non-iterable card object that has a .from_json function
# print (type(cards))

# board_expenses.get_list('Comidas')

def main():
    client = TrelloClient(api_key=api_key, api_secret=api_secret, token=token , token_secret=oauth_secret )
    board_expenses = client.get_board('So69sspg') # test board
    # board_expenses_list = board_expenses.all_lists()
    board_expenses.add_list("test list")
    cards =  board_expenses.get_cards()

    for card in cards:
        print(card)

    

if __name__ == '__main__':
    main()

