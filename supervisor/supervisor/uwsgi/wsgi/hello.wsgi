import time

def hello(environ, start_response):
    status = '200 OK'

    http_host = environ.get('HTTP_HOST', None)
    if http_host is not None:
        hostname = http_host.split(':')[0]
    else:
        hostname = "Website"

    html = []
    html.append("<html><head><title>%s</title></head>" % (hostname,))
    html.append("<body>")
    html.append("<h1>%s</h1>" % (hostname,))
    html.append("<p>Hello World at %s</p>" % (time.ctime(),))
    html.append("</body>")
    html.append("</html>")

    output = "\n".join(html)
    response_headers = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]

application = hello
