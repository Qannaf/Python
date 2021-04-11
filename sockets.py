#coding:utf-8

import socket
mon_host, mon_port = ('',4454)
mon_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((mon_host,mon_port))
print("Le serveur à démarré...")

while True:
    socket.listen()
    mon_conn, mon_address = socket.accept()
    print('En écoute...')

mon_conn.close()
socket.close()