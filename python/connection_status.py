from dotenv import load_dotenv
from colors import red, white, pgreen, pblue

import os
import requests

# Load .env file
load_dotenv()

# Get API key from .env file
key = os.getenv('API_KEY')

# Create Authentification header
headers = {'x-joepegs-api-key': key}

# Get the data from the API
test_response = requests.get('https://api.joepegs.dev/v2/', headers=headers).json()

def check_status_code(response):
    print()
    pblue('Checking Status Code...')
    if len(response) == 0:
        print()
        pgreen('Connection to API successful - Status Code: ' + white + '200')
    else:
        print(red + 'Error: ' + str(response.status_code) + white + ' - ' + response.reason)