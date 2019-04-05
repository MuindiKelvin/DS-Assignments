import socket
 
HOST = "localhost"
PORT = 8080
 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


sock.connect((HOST, PORT))


message = "Hello\n"
new_msg = message.encode()
sock.sendall(new_msg)
#sock2.sendall(new_msg)
#sock3.sendall(new_msg)

data = sock.recv(1024)

#data2 = sock.recv(1024)

print ("1")

if ( data == "olleH\n" ):
    sock.sendall("Bye\n")
    data = sock.recv(1024)
    print ("2"), data
 
    if (data == "eyB}\n"):
        sock.close()
        print ("Socket closed")


PORT1 = 8082
 
sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


sock1.connect((HOST, PORT1))


sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock1.connect((HOST, PORT1))

message = "Hello\n"
new_msg = message.encode()
sock1.sendall(new_msg)

data1 = sock1.recv(1024)

print ("2")
       
if ( data1 == "olleH\n" ):
    sock1.sendall("Bye\n")
    data1 = sock1.recv(1024)
    print ("2")
 
    if (data1 == "eyB}\n"):
        sock1.close()
        print ("Socket closed")


PORT2 = 8083
 
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


sock2.connect((HOST, PORT2))


sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2.connect((HOST, PORT2))

message = "Hello\n"
new_msg = message.encode()
sock2.sendall(new_msg)

data2 = sock2.recv(1024)

print ("3")
       
if ( data2 == "olleH\n" ):
    sock2.sendall("Bye\n")
    data2 = sock2.recv(1024)
    print ("3")
 
    if (data2 == "eyB}\n"):
        sock2.close()
        print ("Socket closed")
