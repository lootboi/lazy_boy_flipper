from dotenv import load_dotenv
from colors import red, white, pgreen, pblue

import os
import requests

# Load .env file
load_dotenv()

# Get API key from .env file
key = os.getenv('JOEPEG_API_KEY')

# Create Authentification header
headers = {'x-joepegs-api-key': key}

def check_status_code():
    pblue('\nChecking Status Code...')
    test_response = requests.get('https://api.joepegs.dev/v2/sales/recent-taker-orders?pageSize=1', headers=headers)
    status_code = test_response.status_code
    if status_code == 200:
        pgreen('\nConnection to API successful - Status Code: ' + white + str(status_code))
    else:
        print(red + '\nError: ' + str(status_code) + white + ' - ' + test_response.reason)