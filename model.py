from sqlalchemy import Table, Column, String
import dbconfig

# model description

entry_table = Table('entry', dbconfig.metadata,
                        Column('id', String(32), primary_key=True),
                        Column('title', String(32)),
                        Column('content', String(30000)),
                        Column('updated', String(20), index=True)
                        )
