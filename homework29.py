"""Основи мережевого програмування"""


"""Task 1
During the lesson, we have created a server and client, 
which use TCP/IP protocol for communication via sockets.
In this task, you have to create a server and client, 
which will use user datagram protocol (UDP) for communication."""

import socket


"SERVER"
HOST = "localhost"
PORT = 8848

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
sock.bind((HOST, PORT))
print("Server is listening")

while True:
    msg, adr = sock.recvfrom(1024)
    print(f"Client msg:{msg}, \nClient IP: {adr}")


"CLIENT"

HOST = "localhost"
PORT = 8848

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hi there")
s.close()





"""Task 2
Extend the echo server, which returns to client the data,
encrypted using the Caesar cipher algorithm by a 
specific key obtained from the client. """

###################################################
"""SERVER"""

import socket

HOST = "localhost"
PORT = 8868

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
sock.bind((HOST, PORT))
print("Server is listening")


while True:
    msg, adr = sock.recvfrom(1024)
    print(f"Client msg:{msg}, \nClient IP: {adr}")

    from string import ascii_letters
    letters = ascii_letters

    def msg_crypt(massage):
        for i in massage:
            if i in letters:
                try:
                    new_idx = letters.index(i) + 1
                    massage = massage.replace(i, letters[new_idx])
                except:
                    if (letters.index(i) + 1) > (len(letters) - 1):
                        new_idx = 0
                        massage = massage.replace(i, letters[new_idx])
            else:
                continue
        return massage

    data = msg_crypt(msg.decode())
    sock.sendto(data.encode(), adr)


#######################################################
"""CLIENT"""

HOST = "localhost"
PORT = 8868

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.connect((HOST, PORT))
    sock.sendall("Hi there".encode("utf-8"))
    data = s.recv(1024)
    print(data)
sock.close()