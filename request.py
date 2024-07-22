import requests 

"""CLIENT_ID = '647a25ef09b3e9a6f00aa290'

grant_type = 'client_credentials'
body_params = {'grant_type' : grant_type}

url = 'https://www.wu-skilledtech.com/admin/api/v2/assessments/65cd2be39bc1aed0e6001d2b/responses'
response = requests.post(url, data=body_params, auth = (CLIENT_ID)) 

token_raw = json.loads(response.text)
token = token_raw["AunFTUso15kMMpqHTyfm8CdZ6HRRjvrhkwtoUCWz"]

headers = {"Authorization": "Bearer {}".format(token)}
r = requests.get(url=url, headers=headers)
print(r.text)"""

r = requests.get(url="https://www.wu-skilledtech.com/admin/api/v2/assessments/65cd2be39bc1aed0e6001d2b/responses", 
    headers={"Authorization": "Bearer AunFTUso15kMMpqHTyfm8CdZ6HRRjvrhkwtoUCWz", 
             "Lw-Client": "647a25ef09b3e9a6f00aa290",
             "Accept": "application/json"})

print(r.text)