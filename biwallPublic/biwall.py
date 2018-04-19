import time
from binance.client import Client

api_key = 'INSERT API KEY HERE'
api_secret = 'INSERT API SECRET HERE'


client = Client(api_key, api_secret)


while True:

#pulling BTC balance.Returns as dict
    balance = client.get_asset_balance(asset='BTC')

#pulling value of "free" from dict to get available balance
    avail = balance['free']

#converting available balance to floating point
    free = float(avail)

#Making numbers more readable for binance API.
    print round(free, 6)-0.000001

    selling = round(free, 6)-0.000001

#Sends in Selling order for BTC at market price if value is large enough to make a trade.
    if selling >= 0.00010000:
        order = client.order_market_sell(
            symbol='BTCUSDT',
            quantity=selling)



    time.sleep(1.3) # in seconds... Binance has a limitaton on requests per minute.
