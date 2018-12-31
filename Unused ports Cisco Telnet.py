import getpass
import telnetlib


host = input('Enter host ip: ')
password = getpass.getpass()

tn = telnetlib.Telnet(host)

tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b"\r\n")
tn.write(b"enable\r\n")
tn.write(password.encode('ascii') + b"\r\n")

tn.write(b"show int | i proto.*notconnect|proto.*administratively down|Last in.* [6-9]w|Last in.*[0-9][0-9]w|[0-9]y|disabled|Last input never, output never, output hang never" + b"\r\n")

tn.write(b"exit\r\n")

print(tn.read_all().decode('ascii'))

input('press enter to exit: ')

