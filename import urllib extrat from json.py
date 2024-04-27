import urllib.request
import json

url = input('Enter URL: ')
data = urllib.request.urlopen(url).read().decode()
json_data = json.loads(data)

comments = json_data['comments']
total_sum = sum(int(comment['count']) for comment in comments)

print('Sum of comment counts:', total_sum)
