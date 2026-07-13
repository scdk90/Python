import requests
from requests.auth import HTTPBasicAuth

# Cisco ISE details
ip_address = "1.2.3.4"
ISE_HOST = f'https://{ip_address}'
USERNAME = input("Username: ")
PASSWORD = input("Password: ")


# API URL's
BASE_URL = f'{ISE_HOST}/ers/config'
ENDPOINT_GROUPS_URL = f'{BASE_URL}/endpointgroup?size=100'
ENDPOINTS_URL = f'{BASE_URL}/endpoint'

# Disable SSL warnings (for demo/test environments only!)
requests.packages.urllib3.disable_warnings()

# Functions
def get_endpoint_identity_groups():
    headers = {'Accept': 'application/json'}
    try:
        response = requests.get(
            ENDPOINT_GROUPS_URL,
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
            headers=headers,
            verify=False,
        )
        if response.status_code == 200:
            groups = response.json()['SearchResult']['resources']
            return groups
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return []
    except requests.RequestException as e:
        return f"Request failed: {e}"


def get_macs_in_identity_group(group_id):
    headers = {'Accept': 'application/json'}
    # filter out group "Unknown"
    if group_id == "Unknown group id":
        return []
    #apply group id filter and size
    url = f"{ENDPOINTS_URL}?filter=groupId.EQ.{group_id}&size=100"
    mac_list = []
    try:   
        # true until no nextpage found
        while url:
            response = requests.get(
                url,
                auth=HTTPBasicAuth(USERNAME, PASSWORD),
                headers=headers,
                verify=False,
            )            
            if response.status_code == 200:                
                result = response.json()                
                for endpoint in result['SearchResult']['resources']:
                    mac_list.append(endpoint['name'])
                # check for nextpage
                try:
                    url = result['SearchResult']['nextPage']['href']
                except:
                    url = False
            else:
                print(f"Error: {response.status_code} - {response.text}")
                return []
        return mac_list    
    except requests.RequestException as e:
        print(f"Request failed: {e}")


if __name__ == '__main__':    
    visual = "#"
    endpointgroups_data = get_endpoint_identity_groups()

    with open("endpoints.txt", "a") as file:        
        for group in endpointgroups_data:
            file.write(group["name"])
            file.write('\n')            
            mac_data = get_macs_in_identity_group(group["id"])
            
            for mac_address in mac_data:
                file.write(mac_address)
                file.write('\n')
                
            file.write('\n')
            print(visual)
            visual += "#"

    print("End of script")

# API filter options
"""
--Cisco ISE REST API filters--
EQ: Equals
NEQ: Not Equals
GT: Greater Than
LT: Less Then
STARTW: Starts With
NSTARTSW: Not Starts With
ENDSW: Ends With
NENDSW: Not Ends With
CONTAINS: Contains
NCONTAINS: Not Contains
"""
