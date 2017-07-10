import sweb
import model

def list(environ, start_response):
    rows = model.entry_table.select().execute()
    return sweb.render(start_response, 'list.html', locals())

def member_get(environ, start_response):
    id = environ['selector.vars']['id']
    rows = model.entry_table.select(model.entry_table.c.id==id).execute().fetchone()
    return sweb.render(start_response, 'entry.html', locals())

def create(entry, start_response):
    pass

def create_form(entry, start_response):
    pass

def member_edit_form(entry, start_response):
    pass

def member_update(entry, start_response):
    pass
