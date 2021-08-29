from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
import threading, os , sqlite3 , datetime
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
server_ip = s.getsockname()[0]
s.close()
server_port = 8080
db_filename = 'server_log.db'
schema_filename = 'server_log_schema.sql'

db_is_new = not os.path.exists(db_filename)

with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print('Creating schema')
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)

    else:
        print('Database exists, assume schema does, too.')


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type',
                         'text/plain; charset=utf-8')
        self.end_headers()
        message = threading.currentThread().getName()
        self.wfile.write(message.encode('utf-8'))
        self.wfile.write(b'\n')
        with sqlite3.connect(db_filename) as conn:
            conn.execute("INSERT INTO log_data VALUES (?,?,?,?,?)",(int(datetime.datetime.strptime(self.date_time_string(),'%a, %d %b %Y %H:%M:%S %Z').timestamp()),self.client_address[0],self.client_address[1],server_ip,server_port))
class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""


if __name__ == '__main__':
    server = ThreadedHTTPServer((server_ip, server_port), Handler)
    print('Starting server, use <Ctrl-C> to stop', server_ip)
    server.serve_forever()
