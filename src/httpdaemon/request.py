import re

class HttpRequest:
    """
    Parser for HTTP requests
    """

    def __init__(self, request):
        """
        Accepts an HTTP request bytestring
        """

        # Convert from bytes to string
        self.request = request.decode("utf-8")

        self.requestline = re.match("GET .* HTTP/1.1", self.request).group(0)
        self.url = re.search("\s.*\s", self.requestline).group(0)[1:-1]

        self.params = {}

        if '?' in self.url:
            elems = self.url.split('?')
            self.path = elems[0]
            self.query = elems[1]

            querylines = self.query.split('&')

            for line in querylines:
                linekey, lineval = line.split('=')
                self.params[linekey] = lineval

        else:
            self.path = self.url