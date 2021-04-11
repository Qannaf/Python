#coding:utf-8

import http.server
import socketserver

mon_port = 80
mon_address = ("",mon_port)

mon_handler = http.server.SimpleHTTPRequestHandler
mon_httpd = socketserver.TCPServer(mon_address, mon_handler)

print("Serveur démarré sur le port{}".format(mon_port))

mon_httpd.serve_forever()
