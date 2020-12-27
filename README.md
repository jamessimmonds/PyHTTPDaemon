# PyHTTPDaemon
Server and handler for HTTP requests

## Basic usage

```python
from daemon import Daemon
from response import htmlrespose

routes = {
    '/': lambda req : htmlresponse('<h1>Index</h1><p>Index page.</p>')
}

d = Daemon(routes=routes)
d.runserver()
```

## Access GET query parameters

```python
from daemon import Daemon
from response import htmlrespose

# For a GET request e.g. /query?key1=val1&key2=val2
routes = {
    '/query': lambda req : htmlresponse(f'<h1>Index</h1><p>Your request was {req.params}</p>')
}

d = Daemon(routes=routes)
d.runserver()
```

## Serve static stylesheets

```python
from daemon import Daemon
from response import htmlrespose, cssresponse

htmlbody = """
<html>
    <head>
        <link href='style.css' type='text/css' ref='stylesheet' />
    </head>
    <body>
        <p>This page has been styled.</p>
    </body>
</html>""" 

cssbody = 'body { font-family: Arial; }'

routes = {
    '/': lambda req : htmlresponse(htmlbody),
    '/style.css': lambda req : cssresponse(cssbody)
}

d = Daemon(routes=routes)
d.runserver()
```

## Simple messages

```python
from daemon import Daemon
from response import message

routes = {
    '/': lambda req : message('Index', 'You have accessed the index page.'),
    '/about': lambda req : message('About', 'This site is under construction.'),
}

d = Daemon(routes=routes)
d.runserver()
```
