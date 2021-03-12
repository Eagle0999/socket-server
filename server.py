#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CHANGED v3

import socket


def seach(message,el,count):
    i=0
    j=0

    while i<len(message):
        if message[i]==el:
           j+=1
        if j==count:
           break
        i+=1
    return i
	
print('Server started!!!')
sock = socket.socket()
sock.bind(('192.168.56.101', 9090))
sock.listen(1)
conn, addr = sock.accept()

print('connected:', addr)

while True:
	
    data = conn.recv(1024).decode('UTF-8')
    if not data:
        break
    print('Server recieved the message from Client: ',data,'\n')
    if data[ : seach(data,',',1)]=='Получить файл':
        file = open(data[seach(data,',',1)+1 : seach(data,',',2)], 'r')
        content = file.read()
        conn.send(content.encode('UTF-8'))
        file.close()
    if data[ : seach(data,',',1)]=='Отправить файл':
        file = open(data[seach(data,',',1)+1 : seach(data,',',2)], 'w')

        file.write(data[seach(data,',',2)+1 : ])

        file.close()
        conn.send('Данные успешно получены'.encode())
        print('Server sended the message to Client: ','Данные успешно получены')
	
conn.close()
