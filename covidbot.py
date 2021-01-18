import requests
import json

url='https://covid19.who.int/table'
data=requests.get(url)
r=data.json()
f=json.dumps(r,indent=4)
print(f)