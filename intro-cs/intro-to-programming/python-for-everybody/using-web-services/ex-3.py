import urllib.request, urllib.parse
import json

basic_url = 'http://py4e-data.dr-chuck.net/json?'


address = input("Enter location ")

params = dict()

params['address'] = address
params['key'] = 42

url = basic_url + urllib.parse.urlencode(params)

print(f"Retrieving {url}")

connection = urllib.request.urlopen(url)

data = connection.read().decode()

print(f"Retrieved {len(data)} characters")

location_data = json.loads(data)

place_id = location_data["results"][0]['place_id']
print(f"Place id {place_id}")
