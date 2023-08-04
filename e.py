# Request POST /api/getinfo
# 
# <title>415 Unsupported Media Type</title>
# <h1>Unsupported Media Type</h1>
# <p>Did not attempt to load JSON data because the request Content-Type was not &#39;application/json&#39;.</p> fix it


import requests, json

data = {
    'username': '@' + 'av.c',
    'authorization': 'aviance.corp$$$$$$$$23243485348&*!#%@^'
}
data = json.dumps(data)

a = requests.post('http://capi.avnce.tech/api/getinfo', data=data, headers={'Content-Type': 'application/json'})
print(a.text)
