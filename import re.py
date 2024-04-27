import re
import urllib.request

def extract_numbers_and_sum(file_url):
    try:
        # Download the file content
        with urllib.request.urlopen(file_url) as response:
            data = response.read().decode()
        
        # Find all numbers in the text using regular expression
        numbers = re.findall(r'[0-9]+', data)
        
        # Convert numbers from strings to integers and calculate the sum
        total_sum = sum(int(num) for num in numbers)
        
        return total_sum
    
    except Exception as e:
        print("Error occurred:", str(e))
        return None

def main():
    # Provide the URL of the file containing data
    file_url = "http://py4e-data.dr-chuck.net/regex_sum_2000231.txt"
    
    # Extract numbers and calculate sum
    total_sum = extract_numbers_and_sum(file_url)
    
    if total_sum is not None:
        print("Sum of the numbers in the file:", total_sum)

if __name__ == "__main__":
    main()
