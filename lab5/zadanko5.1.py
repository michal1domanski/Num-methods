import requests
from random import *
import time

# begin = time.time()

k=0
best_bid=22310
wszyscy=[]
kursBTC=22310
kursPLN=1/kursBTC

while k < 100:
    try:
        uzytkownicy=[]
        response = requests.get('https://randomuser.me/api/?inc=id,name,login')
        uzytkownik = response.json()

        username = uzytkownik['results'][0]['login']['username']
        first = uzytkownik['results'][0]['name']['first']
        last = uzytkownik['results'][0]['name']['last']
        value = uzytkownik['results'][0]['id']['value']

        uzytkownicy.append(first)
        uzytkownicy.append(last)
        uzytkownicy.append(username)
        uzytkownicy.append(value)
    
        randomBTC=round(best_bid*random()*0.001,3)
        uzytkownicy.append(randomBTC)

        randomPLN=round(uniform(5000,150000),2)
        uzytkownicy.append(randomPLN)
        wszyscy.append(uzytkownicy)
        k += 1
    except:
        pass

print(wszyscy)
begin = time.time()
k = 0
while k<100:
    random1=choice(wszyscy)
    random2=choice(wszyscy)
    while random1==random2:
        random1=choice(wszyscy)
    x=random1[4]*uniform(0.1,0.5)
    y=random2[5]
    if x*kursBTC<y:
        time.sleep(1/3)
        wymiana=x*kursBTC
        
        random2[5]=y-wymiana
        random2[4]=random2[4]+x
        random1[5]=random1[5]+wymiana
        random1[4]=random1[4]-x

        print(random1[2], 'exchanged', x, 'BTC for', wymiana, 'PLN with', random2[2])

        k+=1

    else:
        pass
    
print('-----------------------------------')

print(wszyscy)

end = time.time()
print(end - begin)


# Create and store 100 random users with ids, username, name (first + last name) using this API (2p)# fetch data from  API
