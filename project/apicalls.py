import requests
import json
from time import time

TIME_RANGE = 86400  # in seconds

def get_bgplay(ip_or_asn, time_factor):
    start_time = str(int(time()) - TIME_RANGE * time_factor)
    end_time = str(int(time()) - TIME_RANGE * (time_factor - 1))
    url = f"https://stat.ripe.net/data/bgplay/data.json?resource={ip_or_asn}&starttime={start_time}&endtime={end_time}"
    response = requests.request("GET", url)
    return json.loads(response.text)
