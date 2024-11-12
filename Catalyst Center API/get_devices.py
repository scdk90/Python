import requests
from requests.auth import HTTPBasicAuth
import urllib3
import getpass

urllib3.disable_warnings()

# Authentication information
BASE_URL = 'https://catalyst.center.nl'
AUTH_URL = '/dna/system/api/v1/auth/token'
USERNAME = 'username'
PASSWORD = getpass.getpass("Enter password for username: ")

# Ask for the token and create the Headers
response = requests.post(BASE_URL + AUTH_URL
                        , auth=HTTPBasicAuth(USERNAME, PASSWORD)
                        , verify=False)
token = response.json()['Token']
headers = {'X-Auth-Token': token, 'Content-Type': 'application/json'}

# Get list of devices with family 'Switches and Hubs' parameters
query_string_params = {'family': 'Switches and Hubs'}
DEVICES_URL = '/dna/intent/api/v1/network-device'
response = requests.get(BASE_URL + DEVICES_URL
                        , headers = headers
                        , params=query_string_params
                        , verify=False)

# Add every ip address to a list
list_cc = []
for item in response.json()['response']:
    list_cc.append(item['managementIpAddress'])

# Get list of devices with family 'Switches and Hubs' parameters, start from device number 500
query_string_params = {'family': 'Switches and Hubs','offset':'500'}
DEVICES_URL = '/dna/intent/api/v1/network-device'
response = requests.get(BASE_URL + DEVICES_URL
                        , headers = headers
                        , params=query_string_params
                        , verify=False)

for item in response.json()['response']:
    list_cc.append(item['managementIpAddress'])

# Get list of devices with family 'Switches and Hubs' parameters, start from device number 1000
query_string_params = {'family': 'Switches and Hubs','offset':'1000'}
DEVICES_URL = '/dna/intent/api/v1/network-device'
response = requests.get(BASE_URL + DEVICES_URL
                        , headers = headers
                        , params=query_string_params
                        , verify=False)

for item in response.json()['response']:
    list_cc.append(item['managementIpAddress'])

# create list from management ip address text file
list_devices = open('source_devices.txt').read().splitlines()

# compare both lists and add diff to compare list
compare_list = []

for val in list_devices:
    if val not in list_cc:
        compare_list.append(val)

# Print results
number = str(len(compare_list))
print("IP's in list: " + number)
print(compare_list)

input("Press enter to exit")
