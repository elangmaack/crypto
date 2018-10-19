
import json
import urllib2
url_convertion = "http://apilayer.net/api/live?access_key=ad260b69f1dd21c45d58193365057731&currencies=MXN"
print url_convertion
data_currency=json.load(urllib2.urlopen(url_convertion))
print data_currency
print float(data_currency['quotes']['USDMXN'])

print "%.2f,%.2f" % (float(data_currency['quotes']['USDMXN']),  float(data_currency['quotes']['USDMXN']))
