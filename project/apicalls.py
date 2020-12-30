import requests
import json
from time import time


def get_bgplay(ip_or_asn):
    start_time = str(int(time()) - 43200)  # since before twelve hours
    end_time = str(int(time()))
    url = f"https://stat.ripe.net/data/bgplay/data.json?resource={ip_or_asn}&starttime={start_time}&endtime={end_time}&resolution=1h"
    print(url)
    response = requests.request("GET", url)
    return json.loads(response.text)
