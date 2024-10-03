import requests 
import json
import re

response = requests.get(url="https://www.wu-skilledtech.com/admin/api/v2/users", 
    headers={"Authorization": "Bearer AunFTUso15kMMpqHTyfm8CdZ6HRRjvrhkwtoUCWz", 
            "Lw-Client": "647a25ef09b3e9a6f00aa290",
            "Accept": "application/json"})

prsd = response.json()

for a in prsd['data']:
    for b in a:
        if(b == 'username'):
            print(a[b])
