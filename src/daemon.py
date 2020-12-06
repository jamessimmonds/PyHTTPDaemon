import socket
import re

def html(sock, title, message):
    header = b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\n\n"
    body = f"<h1>{title}</h1><p>{message}</p>".encode("utf-8")
    
    htmlresponse = header + body
    
    sock.sendall(htmlresponse)

def runserver(port=8000, host='127.0.0.1'):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((host, port))
        sock.listen()
        print(f"Listening on port {port}...")
        
        while True:
        
            conn, addr = sock.accept()
            
            # Receive request and parse to determine path
            request = conn.recv(1024).decode("utf-8")
            requestline = re.match("GET .* HTTP/1.1", request).group(0)
            path = re.search("\s.*\s", requestline).group(0)[1:-1]

            # Show the path accessed by the request
            print(path)
            
            # Send an HTTP response on the socket
            html(conn, "Page title", f"The following path has been accessed: {path}")
            
            conn.close()
        
        sock.close()

if __name__ == "__main__":
    runserver()