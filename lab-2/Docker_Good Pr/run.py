from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import socket
import time


hostName = os.environ['COOL_IP']
serverPort = int(os.environ['COOL_PORT'])
log_path = os.environ['COOL_LOG']
config_path = '/usr/share/cool-app/'
content_file = '{0}cool-text.txt'.format(config_path)
# serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Cool web application</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>{0}</p>".format(self.read_file()), "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
        self.write_log('site accessed from {0}'.format(self.client_address))
        if self.path != '/' and self.path != '/favicon.ico':
            self.write_log('Request: {0}'.format(self.path))


    def read_file(self):
        with open(content_file, 'r') as my_file:
            return my_file.read()

    def write_log(self, message):
        if not os.path.exists('{0}/cool.log'.format(log_path)):
            with open('{0}/cool.log'.format(log_path), 'w') as log_file:
                log_file.write('{0}\n'.format(message))
        else:
            with open('{0}/cool.log'.format(log_path), 'a') as log_file:
                log_file.write('{0}\n'.format(message))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")