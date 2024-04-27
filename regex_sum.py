import re

# Get the file name from user input
file_name = input("Enter the file name: ")

try:
    with open(file_name, 'r') as file:
        # Read the file content
        content = file.read()

        # Use regular expression to find all numbers in the content
        numbers = re.findall('[0-9]+', content)

        # Convert the numbers from strings to integers and calculate the sum
        total_sum = sum(map(int, numbers))

        # Print the sum
        print("The sum of all numbers in the file is:", total_sum)

except FileNotFoundError:
    print("File not found. Please make sure the file exists and try again.")
except Exception as e:
    print("An error occurred:", e)
