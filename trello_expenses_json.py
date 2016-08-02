#!/usr/bin/python

import json
from pprint import pprint
import sys
from trollop import TrelloConnection
import logging 

api_key = '2819ec494f41829d45bdea15e3cf20e0' # TRELLO_API_KEY
token = '0a46c305b380455a83176624e3e980fa8cfcba3b189a668558f3b03dc729a60e'
url = 'https://trello.com/b/BE89pW61.json'
# idBoard': '577b17583e5d17ee55b20e44',
# idList': '577b17583e5d17ee55b20e45',
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',level=logging.INFO, filename='trello_expenses.log', mode='w+')

conn = TrelloConnection(api_key, token)
board = conn.get_board('BE89pW61')
food_list = conn.get_list('577b17583e5d17ee55b20e45')
food_list_cards = food_list.cards
print conn.me.username

food = conn.me.boards[3]
counter = 0
for each in conn.me.boards[3].lists:
    counter += 1
    logging.info("id: {}".format(each._id))
    print u"id: {0}, url: {1}".format(each.name, each.url)  
print counter

# for each_card in conn.me.boards[2].cards:
#     print u"{0},{1},{2}".format(each_card._id, each_card.url,each_card.desc)  

def main():
    name = list()
    l1 = list()
    total = 0.0
    with open('trello_expenses.json', 'r') as f:
        file = f.read()
        json_file = json.loads(file)
        # pprint(file)
        # print(json_file['lists'][0])
    for card in json_file['cards']:
        if card['idList'] == '577b17583e5d17ee55b20e45':
            name.append( card['name'] )
            # pprint(card['name'])

    for entry in name:
        l1.append( float(entry.split('-')[1]) )

    total =  sum( l1)
    # print( "Total from JSON {0}".format(total) )


if __name__=='__main__':
    main()