import socket
import re

from response import htmlresponse, filenotfound, message
from request import HttpRequest

def runserver(
    port=8000,
    routes={
        '/': message("Index", "You have accessed the index."),
        '/about': message("About", "This site is undergoing construction.")
    },
    host='127.0.0.1'
    ):

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
            print(request.params)

            # Show the path accessed by the request
            path = request.path
            
            # Send an HTTP response on the socket
            if path in routes.keys():
                conn.sendall(routes[path])
            else:
                errormessage = f"You have accessed the following path: {path}"
                conn.sendall(filenotfound(errormessage))
            
            conn.close()
        
        sock.close()

if __name__ == "__main__":
    runserver()