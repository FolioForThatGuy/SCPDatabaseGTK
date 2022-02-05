import http.server
import os, sys
import socketserver
PORT = 8081
web_dir = os.path.join(os.path.dirname(__file__), 'files')
os.chdir(web_dir)
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()
