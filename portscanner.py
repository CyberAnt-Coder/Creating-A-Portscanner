#import necessary libraries
import socket
import re

#assign variables
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# using regular expression, we specify the input of the IP we are going to take later
ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")

#we use a true loop here so that if the user enters an invalid input, it will ask again
while True:
    ip = input("\n What is the IP address you would like to scan?")
    if ip_add_pattern.search(ip):
        print(f"{ip} is a valid ip address")
        break
    else:
        print(f"{ip} is not a valid ip address")

# now ask for port number and change it into int to use later
port = int(input("What is the port you would like to scan?"))


#define portscanning function
def portscan(ip, port):
  if s.connect_ex((ip, port)):
    print("This port is closed")
  else:
    print("This port is open")


#call function
portscan(ip, port)
