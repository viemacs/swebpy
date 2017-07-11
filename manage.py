#!/usr/bin/env python
"""
Swebpy: Simple Webserver in Python
:copyright: (c) 2017 by Viemacs
:license: Mozilla

Manage the applicationn
"""

import os, sys
import click
from werkzeug import run_simple

from werkzeug.wrappers import Request, Response

def create():
    from sqlalchemy import Table
    import model
    for (name, table) in vars(model).items():
        if isinstance(table, Table):
            table.create()

def run():
    pass

def x_run():
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

# def make_app():
#     from application import make_app
#     return make_app('/tmp/swebpy.db')

@click.group()
def cli():
    pass

@cli.command()
@click.option('-h', '--hostname', type=str, default='localhost', help='localhost')
@click.option('-p', '--port', type=int, default=4000, help='4000')
@click.option('--reloader', is_flag=True, default=False)
@click.option('--debugger', is_flag=True)
@click.option('--evalex', is_flag=True, default=False)
@click.option('--threaded', is_flag=True)
@click.option('--processes', type=int, default=1, help='1')
def runserver(hostname, port, reloader, debugger, evalex, threaded, processes):
    '''start a server'''

    # app = make_app()

    @Request.application
    def app(request):
        return Response('foo')
    run_simple(hostname, port, app,
                   use_reloader=reloader, use_debugger=debugger, use_evalex=evalex,
                   threaded=threaded, processes=processes)


if __name__ == '__main__':
    if 'create' in sys.argv:
        create()
    elif 'run' in sys.argv:
        run()
    else:
        cli()
