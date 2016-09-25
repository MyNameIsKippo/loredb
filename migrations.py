from playhouse.migrate import *
import peewee

ts_field = CharField(default='')

loreDatabase = SqliteDatabase('lore.db')
migrator = SqliteMigrator(loreDatabase)

migrate(
    migrator.add_column('lore', 'ts', ts_field),
)