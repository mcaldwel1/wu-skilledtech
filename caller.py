from msal import PublicClientApplication

app = PublicClientApplication(
    "623383a3-9ddb-4ba2-85e4-d511d8d88fbc",
    authority="https://login.microsoftonline.com/common")

accounts = app.get_accounts()
if(accounts):
    print(accounts)
else: 
    print("no accounts")