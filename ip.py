import sys
import socket


hostname = raw_input("Insert Site: ")

try:
    information_site = socket.getaddrinfo(hostname, 'www', 0, socket.SOCK_STREAM, 0, socket.AI_ADDRCONFIG | socket.AI_V4MAPPED | socket.AI_CANONNAME,)
except socket.gaierror as e:
    print('Failure:', e.args[1])
    sys.exit(1)
print information_site
information = information_site[0]
sitename = information[4]
ip = sitename[0]


print('The IP address for ' + str(hostname) + ' is ', str(ip))

