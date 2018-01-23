import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

num = str(input("Data for calculate: "))

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "Data is: ", num

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(num, (UDP_IP, UDP_PORT))
