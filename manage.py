import os, sys

def create():
    from sqlalchemy import Table
    import model
    for (name, table) in vars(model).items():
        if isinstance(table, Table):
            table.create()

def run():
    import router
    if os.environ.get('REQUEST_METHOD', ''):
        # from wsgiref.handlers import BaseCGIHandler
        # BaseCGIHandler(sys.stdin, sys.stdout, sys.stderr, os.environ).run(router.urls)
        pass
    else:
        from werkzeug.wrappers import Request, Response
        from werkzeug.serving import run_simple

        @Request.application
        def app(request):
            return Response('hello there')

        run_simple('', 4000, app)
        return

        httpd.set_app()
        print('Serving HTTP on %s port %s ...' % httpd.socket.getsockname())
        httpd.serve_forever()

if __name__ == '__main__':
    if 'create' in sys.argv:
        create()
    if 'run' in sys.argv:
        run()
