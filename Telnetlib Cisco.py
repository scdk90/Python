import getpass
import telnetlib

ip_list = open('iplist.txt', 'r')
host = ip_list.read().split()

print('Please enter the Telnet password')
password = getpass.getpass().encode(encoding='ascii')

for ip in host:
    #print(ip)
    tn = telnetlib.Telnet(ip, timeout = 5)

    tn.read_until(b'Password: ')
    tn.write(password + b'\r\n')
    tn.write(b'enable' + b'\r\n')
    tn.write(password + b'\r\n')

    tn.write(b'config t' + b'\r\n')
    #tn.write(b'access-list 1 permit host 8.8.8.8' + b'\r\n')
    #tn.write(b'access-list 1 permit host 8.8.4.4' + b'\r\n')

    tn.write(b'exit')
    tn.write(b'wr')
    tn.close()

    print('Host ' + str(ip) + ' is done')
    
ip_list.close()
print(input('All done! Press enter to exit'))