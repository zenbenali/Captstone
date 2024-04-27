import urllib.request, urllib.parse, urllib.error
import json

# API endpoint
base_url = 'http://py4e-data.dr-chuck.net/opengeo?'

# Function to fetch plus_code for a given location
def fetch_plus_code(location):
    # Encode the location parameter
    params = {"q": location}
    url = base_url + urllib.parse.urlencode(params)

    print(f"Retrieving {url}")
    
    # Fetch data from the API
    try:
        data = urllib.request.urlopen(url).read().decode()
        print(f"Retrieved {len(data)} characters")
        
        # Parse JSON data
        json_data = json.loads(data)
        
        # Extract plus_code
        plus_code = json_data["features"][0]["properties"]["plus_code"]
        print("Plus code:", plus_code)
        
    except Exception as e:
        print("Error fetching data:", e)

# Main function
def main():
    location = input("Enter location: ")
    fetch_plus_code(location)

if __name__ == "__main__":
    main()
