import os, sys

def create():
    from sqlalchemy import Table
    import model
    for (name, table) in vars(model).items():
        if isinstance(table, Table):
            table.create()

def run():
    import urls
    if os.environ.get('REQUEST_METHOD', ''):
        from wsgiref.handlers import BaseCGIHandler
        BaseCGIHandler(sys.stdin, sys.stdout, sys.stderr, os.environ).run(urls.urls)
    else:
        from wsgiref.simple_server import WSGIServer, WSGIRequestHandler
        httpd = WSGIServer(('', 8080), WSGIRequestHandler)
        httpd.set_app(urls.urls)
        print('Serving HTTP on %s port %s ...' % http.socket.getsockname())
        httpd.serve_forever()

if __name__ == '__main__':
    if 'create' in sys.argv:
        create()
    if 'run' in sys.argv:
        run()
