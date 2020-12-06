
class HtmlResponse:
    """
    Returns a binary string representation an HTTP response that can be sent on a socket.
    """
    
    def __init__(self, responsebody):

        header = b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\n\n"
        body = responsebody.encode("utf-8")

        self.response = header + body