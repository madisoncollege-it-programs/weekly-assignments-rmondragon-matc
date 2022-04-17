#!/usr/bin/env python3

import socket



RHOST = '172.16.189.132'
RPORT = 5000
SND_DATA = 'MY Text to send'

C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
C_SOCK.connect((RHOST, RPORT))

C_SOCK.send(bytearray(SND_DATA,'utf8'))

RCV_DATA = C_SOCK.recv(1024)
print(RCV_DATA)

C_SOCK.close()


