import http.server
import socketserver


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'static/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


handler_object = MyHttpRequestHandler

PORT = 3060
my_server = socketserver.TCPServer(("", PORT), handler_object)

# Start the server
my_server.serve_forever()
