import requests
import json

# Send a GET request to the API
response = requests.get('https://www.example.com/api/data')

# Parse the response data as JSON
data = json.loads(response.text)

# Open a file and write the data to it
with open('data.json', 'w') as file:
  json.dump(data, file)
