import getpass
import telnetlib


host = input('Enter host ip: ')
password = getpass.getpass().encode(encoding='ascii')

tn = telnetlib.Telnet(host, timeout = 5)

tn.read_until(b'Password: ')
tn.write(password + b'\r\n')
tn.write(b'enable' + b'\r\n')
tn.write(password + b'\r\n')

tn.write(b'show int | i proto.*notconnect|proto.*administratively down|Last in.* [6-9]w|Last in.*[0-9][0-9]w|[0-9]y|disabled|Last input never, output never, output hang never' + b'\r\n')
tn.write(b' ' + b' ' + b' ')

print(tn.read_until(b'exit', timeout = 3).decode('ascii'))

input('press enter to exit: ')
