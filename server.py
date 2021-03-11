#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
print('Server started!!!')
sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

print('connected:', addr)

while True:
	
    data = conn.recv(1024).decode()
    if not data:
        break
    print('Server recieved the message from Client: ',data.upper(),'\n')
    print('Server is sending the message to Client: ',data.upper())
    conn.send(data.upper().encode())

conn.close()