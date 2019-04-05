#KYALO KELVIN MUINDI
#P15/37561/2016
#Gossip_Based Assignment
#Sendercode

import socket
import struct
import sys

message = 'Hello Gossip_Nodes'
multicast_group = ('224.4.9.1', 10000)

# Create the datagram socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set a timeout so the socket does not block indefinitely when trying
# to receive data.
sock.settimeout(0.1)
# Set the time-to-live for messages to 1 so they do not go past the
# local network Nodes.
ttl = struct.pack('b', 5)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
try:

    # Send data to the multicast group
    newmessage=message.encode('utf-8')
    print(sys.stderr, 'sending "%s"' % message)
    sent = sock.sendto(newmessage, multicast_group)

    # Look for responses from all recipients
    while True:
        print(sys.stderr, 'waiting to receive')
        try:
            data, server = sock.recvfrom(48)
        except socket.timeout:
            print (sys.stderr, 'timed out, no more responses')
            break
        else:
            print(sys.stderr, 'received "%s" from %s' % (data, server))
            #Send data to the multicast group
            newmessage=message.encode('utf-8')
            print(sys.stderr, 'sending "%s"' % message)
            sent = sock.sendto(newmessage, multicast_group)
            

finally:
    print(sys.stderr, 'closing socket')
    sock.close()
