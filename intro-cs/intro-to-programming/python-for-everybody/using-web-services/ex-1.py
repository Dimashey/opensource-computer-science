import urllib.request
import xml.etree.ElementTree as ET

location = input("Enter localtion: ")

print(f"Retrieving {location}")

connection = urllib.request.urlopen(location)

data = connection.read().decode()

xml = ET.fromstring(data)

comments = xml.findall('comments/comment')

sum = 0

for comment in comments:
    count = int(comment.find('count').text) 
    sum += count

print(f"Retrieved {len(data)} characters")
print(f"Count {len(comments)}")
print(f"Sum {sum}")