import urllib.request
import xml.etree.ElementTree as ET

# Prompt for the URL
url = input('Enter URL: ')

# Read the XML data from the URL
xml_data = urllib.request.urlopen(url).read()

# Parse the XML data
tree = ET.fromstring(xml_data)

# Initialize the sum of comment counts
total = 0

# Extract all 'count' elements and sum their values
for comment in tree.findall('.//count'):
    count = int(comment.text)
    total += count

# Print the total sum of comment counts
print('Sum of comment counts:', total)