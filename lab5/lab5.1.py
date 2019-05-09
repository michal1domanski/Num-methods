import requests

response = requests.get("https://bitbay.net/API/Public/BTCPLN/ticker.json")
data = response.json()
best_bid=data['bid']
best_ask=data['ask']
print('bid:',best_bid,'ask:',best_ask)

response2 = requests.get("https://www.bitmarket.pl/json/BTCPLN/ticker.json")
data2 = response2.json()
best_bid2 = data2['bid']
best_ask2 = data2['ask']
print('bid BTC:',best_bid2,'ask BTC:',best_ask2)

print('Selling:')

if best_bid > best_bid2:
    print('Bitbay is better for selling')
else:
    print('Bitmarket is better for selling')

print('Buying:')

if best_ask < best_ask2:
    print('Bitbay is better for selling')
else:
    print('Bitmarket is better for selling')

