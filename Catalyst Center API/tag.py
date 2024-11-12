import requests
from requests.auth import HTTPBasicAuth
import urllib3
import json

urllib3.disable_warnings()

# Authentication information
BASE_URL = 'https://catalyst.center.nl'
AUTH_URL = '/dna/system/api/v1/auth/token'
USERNAME = 'username'
PASSWORD = 'password'

# Ask for the token and create the Headers
response = requests.post(BASE_URL + AUTH_URL
                        , auth=HTTPBasicAuth(USERNAME, PASSWORD)
                        , verify=False)
token = response.json()['Token']
headers = {'X-Auth-Token': token, 'Content-Type': 'application/json', "Accept": "application/json"}

# function to get all the tags
def get_tag():
    url = "https://catalyst.center.nl/dna/intent/api/v1/tag"

    payload = None

    response = requests.request('GET', url, headers=headers, data = payload, verify=False)

    return response.text

# function to get info from one tag name
def get_tag_info(tag_name):
    url = "https://catalyst.center.nl/dna/intent/api/v1/tag"

    query_string_params = {'name':tag_name}

    response = requests.request('GET', url, headers=headers, verify=False, params=query_string_params)

    return response.json()

# function to format output to json
def print_json(input):
    json_object = json.loads(input)

    json_formatted_str = json.dumps(json_object, indent=2)

    return print(json_formatted_str)

# function to create a tag, need to edit for input
def create_tag():
    url = "https://catalyst.center.nl/dna/intent/api/v1/tag"

    payload = '''{"systemTag": false,
                "description": "tag test",
                "name": "tag_test"
                }'''

    response = requests.request('POST', url, headers=headers, data = payload, verify=False)

    return print(response.text.encode('utf8'))

# function to get tag id from a tag name
def get_tag_id(tag_name):
    url = "https://catalyst.center.nl/dna/intent/api/v1/tag"

    query_string_params = {'name':tag_name}

    response = requests.request('GET', url, headers=headers, verify=False, params=query_string_params)

    output = response.json()

    tag_id = output["response"][0]["id"]

    return tag_id

# function to delete a tag by id
def delete_tag_id(tag_id):
    url = f"https://catalyst.center.nl/dna/intent/api/v1/tag/{tag_id}"
    
    payload = {}
    
    response = requests.request('DELETE', url, headers=headers, data = payload, verify=False)

    return response
