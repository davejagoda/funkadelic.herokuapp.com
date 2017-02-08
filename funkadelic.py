#!/usr/bin/env python3

PAGE = """
<html>
  <head>
    <title>funkadelic</title>
  </head>
  <body>
    <h1>funkadelic</h1>
    <p>
      path:{}
    </p>
  </body>
</html>
"""

def app(environ, start_response):
    path = environ.get('PATH_INFO', '').lstrip('/')
    status = '200 OK'
    content = PAGE.format(path)
    response_headers = [('Content-Type', 'text/html'), ('Content-Length', str(len(content)))]
    start_response(status, response_headers)
    yield content.encode('utf8')

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 5000, app)
    srv.serve_forever()
