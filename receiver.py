#KYALO KELVIN MUINDI
#P15/37561/2016
#Gossip_Based Assignment
#Receiver/Nodes code
import socket
import struct
import sys

multicast_group = '224.4.9.1'
server_address = ('', 10000)

num = 1

while num<5:
    # Create the socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind to the server address
    sock.bind(server_address)
    # Tell the operating system to add the socket to the multicast group
    # on all interfaces.
    group = socket.inet_aton(multicast_group)
    mreq = struct.pack('4sL', group, socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    # Receive/respond loop
    while True:

        print(sys.stderr, '\nwaiting to receive message')
        data, address = sock.recvfrom(1024)
        
        print(sys.stderr, 'received %s bytes from %s' % (len(data), address))
        print(sys.stderr, data)

        print(sys.stderr, 'sending acknowledgement to', address)
        myack='Acknowledgement message'
        mynewack=myack.encode('utf-8')
        sock.sendto(mynewack, address)
        num = num + 1
