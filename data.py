import requests
import json
from datetime import date, datetime
from urllib.parse import urlparse

def fonction(base_url,params):
    if params!= None:
        result = requests.get(base_url+"/"+params)
    else:
        result = requests.get(base_url)
    endpoint = urlparse(base_url).path
    endpoint = endpoint.replace("/","_")
    today = date.today()
    now = datetime.now()
    date_time = now.strftime("%m_%d_%Y")
    payload = {
        'donne' :result.json(),
        'jour': date_time,
        'nom':endpoint
    }
    with open(endpoint+"_"+date_time + ".json", "w") as outfile:
        json.dump(payload, outfile)

fonction("https://api.nasa.gov/planetary/apod?api_key=ZNc52Vo8F4nyxgZtvkJHQqiwyBH6JZvDCGaA3jgU", "")