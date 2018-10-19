import csv
import json
import urllib2
from collections import namedtuple
from pprint import pprint

site = "https://min-api.cryptocompare.com/data/pricemulti?fsyms="
filename="my_positions.txt"
currency=['USD']
mycurrency=','.join(currency)

Position= namedtuple('Position',['symbol','quantity','price'])
positions=[]

def get_positions():
    with open(filename) as f:
        reader = csv.reader(f, delimiter=' ')
        for symbol,quantity in reader:
            url = site + symbol + "&tsyms=" + mycurrency
            data = json.load(urllib2.urlopen(url))
            price=data[symbol]['USD']
            position=Position(symbol,quantity,price)
            positions.append(position)
    return positions


if __name__ == '__main__':
    port = get_positions()
    pprint(port)
