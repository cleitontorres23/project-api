import requests
import json


def query(url):
    
    r = requests.get(url)
    if (r.status_code == 200):
        return(r.text)
    else:
        print("we have a problem, back off")

a = query("https://api.thecatapi.com/v1/images/search")
values = json.loads(a)

for i in values:
    print(i.get('url'))