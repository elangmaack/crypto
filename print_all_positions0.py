import csv
import json
import urllib2
import time
import sys
from collections import namedtuple
from pprint import pprint


'''class MyWriter:

    def __init__(self, stdout, filename):
        self.stdout = stdout
        self.logfile = file(filename, 'a')

    def write(self, text):
        self.stdout.write(text)
        self.logfile.write(text)

    def close(self):
        self.stdout.close()
        self.logfile.close()


writer = MyWriter(sys.stdout, 'log.txt')
sys.stdout = writer
'''

site = "https://min-api.cryptocompare.com/data/pricemulti?fsyms="
url_convertion = "https://api.fixer.io/latest?symbols=MXN&base=USD"
filename="my_positions.txt"
currency=['USD']
mycurrency=','.join(currency)
investment=8301.49

Position= namedtuple('Position',['symbol','quantity','price','value'])
portfolio=[]
data_currency=json.load(urllib2.urlopen(url_convertion))
pesos=float(data_currency['rates']['MXN'])

with open(filename) as f:
    reader = csv.reader(f, delimiter=' ')
    for symbol,quantity in reader:
        url = site + symbol + "&tsyms=" + mycurrency
        data = json.load(urllib2.urlopen(url))
        price=data[symbol]['USD']
        value=float(quantity)*float(price)
        position=Position(symbol,float(quantity),float(price),float(value))
        portfolio.append(position)
pprint(portfolio)





total=sum([position.quantity * position.price for position in portfolio])
xtz_value=sum([position.quantity * position.price for position in portfolio if position.symbol == 'XTZ'])
erc20_value=sum([position.quantity * position.price for position in portfolio if position.symbol == 'ETH' or position.symbol == 'PPT' or position.symbol == 'PLR' or position.symbol == 'PRO' or position.symbol == 'VERI'])
ltc_value=sum([position.quantity * position.price for position in portfolio if position.symbol == 'LTC'])
xlm_value=sum([position.quantity * position.price for position in portfolio if position.symbol == 'XLM'])
neo_value=sum([position.quantity * position.price for position in portfolio if position.symbol == 'NEO' or position.symbol == 'GAS'])
print '\n'
print "Pesos Value:\t\t%.2f" % pesos
print ''
print "Non Ledger:"
print "Tezos:%.2f" % xtz_value
print ''
print "Ledger:"
print "ERC20:%.2f\tLTC:%.2f\tXLM:%.2f\tNEO:%.2f\t" % (erc20_value,ltc_value,xlm_value,neo_value)
print ''
print ''
print "Total value:\t\t USD:%.2f\t MXN:%.2f" % (total, (total*pesos))
print "Gain:\t\t\t USD:%.2f\t MXN:%.2f" % ((total-investment),(total-investment)*pesos)
print ''
print "Total value - Tezos:\t USD:%.2f\t MXN:%.2f" % (total-xtz_value, ((total-xtz_value)*pesos))
print "Gain - Tezos:\t\t USD:%.2f\t MXN:%.2f" % ((total-investment-xtz_value),(total-investment-xtz_value)*pesos)
print ''
print "Invested:\t\t USD:%.2f\t MXN:%.2f" % (investment, (investment*pesos))
print ''
print time.strftime("%c")
print ''
