import requests
import json

trans_mean = ['walking', 'transit/integrated', 'bicycling', 'driving']

payload = {
    'origin': '121.587674,31.201777',
    'destination': '121.479699,31.230991',
    'key': 'c089d6c81839755297c6af10d390472e',
    'city': '021'
    }


amap_api_url = 'http://restapi.amap.com/v3/direction/{}'.format(trans_mean[1])

r = requests.get(amap_api_url, params=payload)
j = r.content
c = json.loads(j)

mnt = 'mnt'