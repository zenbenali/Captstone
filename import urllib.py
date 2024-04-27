import urllib.request
from bs4 import BeautifulSoup

# Function to extract numbers from HTML using BeautifulSoup
def extract_numbers(url):
    # Fetch HTML content from the URL
    html = urllib.request.urlopen(url).read()

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find all <span> tags with class 'comments' (assuming numbers are stored in such tags)
    span_tags = soup.find_all('span', class_='comments')

    # Extract numbers from the <span> tags and return them
    numbers = [int(span.get_text()) for span in span_tags]

    return numbers

# Actual data URL
actual_url = "http://py4e-data.dr-chuck.net/comments_2000233.html"

# Extract numbers from actual data URL
numbers = extract_numbers(actual_url)

# Compute sum of the extracted numbers
real_sum = sum(numbers)

print("Real sum of numbers from actual data:", real_sum)
