import requests
import random
import time
from random import *

# https://randomuser.me/api/?inc=id,name,login

begin = time.time()

response = requests.get("https://bitbay.net/API/Public/BTCPLN/ticker.json")
data = response.json()
best_bid=data['bid']
best_ask=data['ask']
print('bid:',best_bid,'ask:',best_ask)

def osoba():
    response = requests.get("https://randomuser.me/api/?inc=id,name,login")
    data = response.json()
    ide = data["results"][0]['id']['value']
    username = data["results"][0]['login']['username']
    first = data["results"][0]['name']['first']
    last = data["results"][0]['name']['last']
    btc = round(random(),3) * 10
    pln = round(random(),8) * 1000000
    return first, last, username, ide, btc, pln 

i = 100
osoby = []
while len(osoby) < i:
    try:
        osoby.append(osoba())
    except:
        pass

for k in range(len(osoby)):
    print(osoby[k])

zliczanie_wymian = 0

while zliczanie_wymian < i:

    rand = choice(osoby)
    rand2 = choice(osoby)

    while rand == rand2:
        rand2 = choice(osoby)

    a = uniform(0.2,0.7)
    if rand[4] * a * best_bid <= rand2[5]:
        time.sleep(1/3)
        zliczanie_wymian += 1
        btc_ex = rand[4] * a
        pln_ex = rand[4] * a * best_bid
        # rand2[4] = rand2[4] + btc_ex
        # rand[4] = rand[4] - btc_ex
        # rand2[5] = rand2[5] - pln_ex
        # rand[5] = rand[5] + pln_ex
        print(rand[2], 'exchanged', btc_ex, 'BTC for', pln_ex, 'PLN with', rand2[2])
    else:
        pass

end = time.time()
print('time:', end - begin)

# 2 Use https://randomuser.me API to download a random user data.
# Create and store 100 random users with ids, username, name (first + last name) using this API (2p)
# 3 Prepare a simulation of transactions between these users
# Take random user and pair him/her with another one. Assume a random amount but take real world price. Sum up the transaction printing:
# username1 exchanged X.XXX BTC with username2 for PLN YYYYY.YYY PLN. (2p)
# Simulate real time - do not proceed all transactions at once. Try to make around 100 transactions per minute (2p)
# Simulate user's assets. Creating a user assign random amount of a given currency. Take it into account while performing a transaction.
# Remember to amend user's assets after the transaction. (2p)