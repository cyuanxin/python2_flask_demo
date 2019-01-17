from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
# from flask import Flask
# app = Flask(__name__)

class RequestHandler(BaseHTTPRequestHandler):
  def do_GET(s):
    s.send_response(200)
    s.end_headers()
    s.wfile.write('HelloWorld!')



if __name__ == '__main__':
    server = HTTPServer(('', 8080), RequestHandler)
    server.serve_forever()