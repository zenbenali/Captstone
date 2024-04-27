import urllib.request
from bs4 import BeautifulSoup

# Function to retrieve the name at the specified position from a URL
def retrieve_name(url, position):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Find all anchor tags
    tags = soup('a')
    
    # Retrieve the href value at the specified position
    link = tags[position - 1].get('href', None)

    return link

# Starting URL
start_url = "http://py4e-data.dr-chuck.net/known_by_Rylee.html"
# Position of the link to follow
position = 18
# Number of times to repeat the process
repetitions = 7

# Repeat the process
for i in range(repetitions):
    # Retrieve the next URL to follow
    next_url = retrieve_name(start_url, position)
    # Update the start URL for the next iteration
    start_url = next_url

# Extract the last name from the final URL
html = urllib.request.urlopen(next_url).read()
soup = BeautifulSoup(html, 'html.parser')
last_name = soup.find('h1').get_text()

print("Last name retrieved:", last_name)
