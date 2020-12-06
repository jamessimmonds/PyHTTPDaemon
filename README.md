# PyHttpDaemon
Server and handler for HTTP requests

```python
from daemon import Daemon
from response import htmlrespose

routes = {
    '/': lambda req : htmlresponse('<h1>Index</h1><p>Index page.</p>')
}

d = Daemon(routes=routes)
d.runserver()
```