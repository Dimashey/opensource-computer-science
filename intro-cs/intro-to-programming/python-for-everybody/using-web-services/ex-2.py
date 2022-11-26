import urllib.request
import json

location = input("Enter localtion: ")

print(f"Retrieving {location}")

data = urllib.request.urlopen(location).read().decode()

comments = json.loads(data)['comments']

sum = 0

for comment in comments:
    count = int(comment['count'])
    sum += count

print(f"Retrieved {len(data)} characters")
print(f"Count {len(comments)}")
print(f"Sum {sum}")
