from jinja2 import Environment, PackageLoader, select_autoescape
import os
from io import StringIO

extensions = {
    'html': 'text/html',
    'atom': 'application/atom+xml'
    }

env = Environment(
    loader = PackageLoader('sweb', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
    )

template = env.get_template('list.html')

print(template.render(the='variables', go='here'))

def render(start_response, template_file, vars):
    ext = template_file.rsplit('.')
    contenttype = 'text/html'
    if len(ext) > 1 and (ext[1] in extensions):
        contenttype = extensions[ext[1]]

    template = kid.Template(file=os.path.join('templates', template_file), **vars)
    body = template.serialize(encoding='utf-8')

    start_response('200 OK', [('Content-Type', contenttype)])
    return [body]

    # stdout = StringIO()
    # start_response('200 OK', [('Content-Type', 'text/plain; charset=utf-8')])
    # return [stdout.getvalue().encode('utf-8')]
