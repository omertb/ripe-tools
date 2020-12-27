import requests
from time import time


def get_bgplay(ip_or_asn):
    start_time = int(time()) - 3600  # since before one hour
    url = f"https://stat.ripe.net/data/bgplay/data.json?&unix_timestamps=TRUE&starttime={start_time}&resource={ip_or_asn}"
    response = requests.request("GET", url)
    return response
