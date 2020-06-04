import http.server
import socketserver
import sys
import socket

PORT =int(sys.argv[1])
server_name = socket.gethostname() 
print("the Server IP is :", socket.gethostbyname(server_name) )

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()