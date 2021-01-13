#! /usr/bin/env python
# needs Pyats/Genie installed on linux!!!

from netmiko import ConnectHandler
import getpass

username_input = input("Username: ")
password_input = getpass.getpass(prompt="Password: ")

with open('devices.txt') as f:
    devices = f.read().splitlines()

device_list = list()

# create ConnectHandler for each device in the list
for ip_address in devices:
    cisco_device = {
            'device_type': 'cisco_ios',
            'ip': ip_address,
            'username': username_input,
            'password': password_input,
            'port': '22',
            'secret': password_input,
            'verbose': True,
    }
    device_list.append(cisco_device)

# loop for parsing each device and configuring interface description
for device in device_list:
    while True:
        try:
            with ConnectHandler(**device) as net_connect:
                parser_output = net_connect.send_command("show cdp neighbors", use_genie=True)
                parser_output = parser_output["cdp"]["index"]
                
                config_commands = []

                for neighbor in parser_output:
                    if parser_output[neighbor]["platform"] == "AIR-AP280":
                        config_commands.append("interface " + parser_output[neighbor]["local_interface"])
                        config_commands.append("description " + parser_output[neighbor]["device_id"])
                    else:
                        continue
                
                net_connect.send_config_set(config_commands)
                net_connect.send_command("wr")
            break
        except Exception as error:
            print(error)
            break

input("Press enter to close")
