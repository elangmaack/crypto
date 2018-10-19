import json
import urllib2

coins=['LTC','ETH','BTC','XTZ','NEO','XLM','PPT','PLR','VERI','GAS','PRO','LA']
mycoins=','.join(coins)
currency=['USD']
mycurrency=','.join(currency)
url = "https://min-api.cryptocompare.com/data/pricemulti?fsyms=" + mycoins + "&tsyms=" + mycurrency
data = json.load(urllib2.urlopen(url))

##or symbol in data:
##    print '%s,%s' % (symbol,data[symbol]['USD'])

for coin in coins:
    print '%s' % (data[coin]['USD'])
