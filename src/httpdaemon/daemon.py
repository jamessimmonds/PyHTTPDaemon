import socket
import re

from response import htmlresponse, filenotfound, message, cssresponse
from request import HttpRequest

class Daemon:

    def __init__(
        self,
        port=8000,
        routes={
            '/': lambda req : message("Daemon", "The HTTP daemon is running."),
        },
        host='127.0.0.1'
        ):

        self.port = port
        self.routes = routes
        self.host = host

    def runserver(self):

        port = self.port
        routes = self.routes
        host = self.host

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind((host, port))
            sock.listen()
            print(f"Listening on port {port}...")
            
            while True:
            
                conn, addr = sock.accept()
                
                # Receive request and parse to determine path
                request = HttpRequest(conn.recv(1024))

                print(request.requestline)

                # Show the path accessed by the request
                path = request.path
                
                # Send an HTTP response on the socket
                if path in routes.keys():
                    conn.sendall(routes[path](request))
                else:
                    errormessage = f"You have accessed the following path: {path}"
                    conn.sendall(filenotfound(errormessage))
                
                conn.close()
            
            sock.close()

if __name__ == "__main__":

    homepage = """
    <html><head><link type="text/css" rel="stylesheet" href="style.css"></head>
    <body><h1>Home</h1><p>The site is operational.</p></body><html>
    """

    cssstyle = """
    body {
        font-family: Arial;
    }
    """

    routes = {
        '/': lambda req : htmlresponse(homepage),
        '/style.css': lambda req : cssresponse(cssstyle),
        '/query': lambda req : message('Query', f'Your query was {req.params}')
    }

    d = Daemon(routes=routes)
    d.runserver()