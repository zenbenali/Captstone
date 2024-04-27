import urllib.parse
import urllib.request
import json

def get_plus_code(location):
    base_url = "http://py4e-data.dr-chuck.net/opengeo?"
    params = {"q": location}
    url = base_url + urllib.parse.urlencode(params)
    
    try:
        response = urllib.request.urlopen(url)
        data = response.read().decode()
        json_data = json.loads(data)
        
        # Check if the JSON response contains plus codes
        if 'plus_codes' in json_data:
            plus_codes = json_data['plus_codes']
            if plus_codes:
                first_plus_code = plus_codes[0]
                return first_plus_code
            else:
                return "No plus codes found for this location."
        else:
            return "No plus codes found in the response."

    except Exception as e:
        return f"Error occurred: {str(e)}"

def main():
    location = input("Enter a location: ")
    plus_code = get_plus_code(location)
    print("First plus code for the location:", plus_code)

if __name__ == "__main__":
    main()