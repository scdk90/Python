from getpass import Getpass
from netmiko import Netmiko


while True:
    try:
        net_connect = Netmiko(host = input('Enter host ip: '),
                              username = 'admin',
                              password = getpass(),
                              device_type = 'cisco_ios'
                              )
        break
    except Exception:
        print('Incorrect host or password, please try again.')
        continue

        
def ssh_script():
    input_interfaces = input('enter interfaces, "1/1" or "1/1-5" seperated by a space: ').split()
    
    while True:
        try:
          macro = input('enter voip or ap macro: ')
          if macro == 'ap' or macro == 'access point':
              ap_vlan = int(input('enter access point vlan: '))
              macro_command = f'macro apply ap $vlan {ap_vlan}'
              desciption_input = input('enter port description: ')
              description_command = f'description {desciption_input}'

              for i in input_interfaces:
                  interface_command = 'interface range gi' + i
                  commands = [interface_command, macro_command, description_command]
                  net_connect.send_config_set(commands)
              break
          elif macro == 'voip' or macro == 'voice':
              access_vlan = int(input('enter access vlan: '))
              voice_vlan = int(input('enter voice vlan: '))
              macro_command = f'macro apply voip $vlan {access_vlan} $vvlan {voice_vlan}'
              desciption_input = input('enter port description: ')
              description_command = f'description {desciption_input}'

              for i in input_interfaces:
                  interface_command = 'interface range gi' + i
                  commands = [interface_command, macro_command, description_command]
                  net_connect.send_config_set(commands)
              break
          else:
              print('please make a valid selection.')
              continue
        except Exception:
            print('please make a valid selection.')

            
ssh_script()


while True:
    try:
        reload_script = input('Would you like to run this script again? (y/n): ')
        
        if reload_script == 'yes' or reload_script == 'y':
            ssh_script()
            continue
        elif reload_script == 'no' or reload_script == 'n':
            print('Time for a break!')
            break
        else:
            print('Please select y/n')
            continue
    except Exception:
        print('Please select y/n')

print('Disconnecting...')
net_connect.disconnect()

