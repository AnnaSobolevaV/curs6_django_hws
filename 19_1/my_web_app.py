from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import os

hostName = "localhost"
serverPort = 8080
DATA_PATH = os.getcwd()
file_index = os.path.join(DATA_PATH, 'index.html')


class MyServer(BaseHTTPRequestHandler):
    file = file_index

    def __get_index(self):
        if os.access(self.file, os.R_OK):
            with open(self.file, 'r', encoding='utf-8') as f:
                data = f.read()
            return data

    def do_GET(self):
        page_content = self.__get_index()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
