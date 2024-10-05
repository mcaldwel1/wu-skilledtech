import requests 
import json
import re

all_users = []

def per_page(page):
    response = requests.get(url="https://www.wu-skilledtech.com/admin/api/v2/users", 
    headers={"Authorization": "Bearer AunFTUso15kMMpqHTyfm8CdZ6HRRjvrhkwtoUCWz", 
            "Lw-Client": "647a25ef09b3e9a6f00aa290",
            "Accept": "application/json"},
    params={"items_per_page": "200",
            "page": page})

    prsd = response.json()

    for a in prsd['data']:
        for b in a:
            if(b == 'username'):
                """print(a[b])"""
                all_users.append(a[b])

    return (len(prsd['data']))

index = 1

while(per_page(index) > 199):
    index+=1

print(len(all_users))
