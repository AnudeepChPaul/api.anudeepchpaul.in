from rethinkdb import RethinkDB
import src.configurations as config

r = RethinkDB()

conn = None

HOST = config.DB_HOST
PORT = config.DB_PORT
DB = config.DB_ROOT_NAME

tables = dict({
    'app': ('app', 'name'),
    'skills': ('skills', 'skill_name')
})


def create_db():
    try:
        r.db_create(DB).run(conn)
        print('Database with name="{DB}" created'.format(DB=DB))
    except:
        print('Database with name="{DB}" exists'.format(DB=DB))


def create_tables():
    for table_name, primary in tables.values():
        try:
            query = r.db(DB).table_create(table_name, primary_key=primary)
            query.run(conn)

            print('Table with name="{table_name}" created'.format(
                table_name=table_name))
        except:
            print('Table with name="{table_name}" exists'.format(
                table_name=table_name))


def connect_db():
    global conn
    try:
        conn = r.connect(host=HOST, port=PORT)
        print('db connected!')
    except:
        print('Not able to connect to db!')


def initialize_db():
    create_db()
    create_tables()


def destroy_db():
    pass


def destroy_tables():
    pass



def init_db_connection():
    connect_db()
    initialize_db()


print('db/__init__ loaded')
