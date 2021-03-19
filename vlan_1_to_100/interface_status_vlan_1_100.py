# VLAN 1 > 100 script
# https://github.com/networktocode/ntc-templates
# Create local windows variable "NET_TEXTFSM"
# C:\Users\User\Documents\Python\ntc-templates-master\ntc-templates-master\templates

from netmiko import ConnectHandler
import getpass
import logging

username_input = input("Username: ")
password_input = getpass.getpass(prompt="Password: ")

# netmiko logging for debugg
logging.basicConfig(filename="logfile.log", level=logging.DEBUG)
logger = logging.getLogger("netmiko")

with open('devices.txt') as f:
    devices = f.read().splitlines()

device_list = list()

Te = "Te"
Po = "Po"
Trunk = "Trunk"

# create ConnectHandler for each device in the list
for ip_address in devices:
    cisco_device = {
            'device_type': 'cisco_ios_telnet',
            'ip': ip_address,
            'username': username_input,
            'password': password_input,
            'port': 23,
            'secret': password_input,
            'verbose': True,
    }
    device_list.append(cisco_device)

# loop for parsing each device and configuring interface description
for device in device_list:
        try:
            with ConnectHandler(**device) as net_connect:
                parser_output = net_connect.send_command("show interfaces status", use_textfsm=True)

                config_commands = []

                # change == check if needed
                for interface in parser_output:
                    if Te in interface["port"]:
                        continue
                    elif Po in interface["port"]:
                        continue
                    elif Trunk in interface["vlan"]:
                        continue
                    elif interface["vlan"] == "1":
                        config_commands.append("interface " + interface["port"])
                        config_commands.append("switchport access vlan 100")
                    else:
                        continue

                net_connect.enable()
                net_connect.send_config_set(config_commands)
                net_connect.save_config()

            continue
        except Exception as Error:
            print(Error)
            break

input("Press enter to close")
