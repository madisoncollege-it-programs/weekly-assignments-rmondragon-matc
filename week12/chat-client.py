#!/usr/bin/env python3

import socket

RHOST   = socket.gethostbyname('ident.me')
RPORT   = 80
SND_DATA= b"GET / HTTP/1.0\r\n\r\n"
RCV_DATA= ""

C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



C_SOCK.connect((RHOST, RPORT))



C_SOCK.send(SND_DATA)



RCV_DATA = C_SOCK.recv(1024)

print(RCV_DATA.decode())


C_SOCK.close()


