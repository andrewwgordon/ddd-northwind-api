from northwind.adapter.configuration import application
from northwind.adapter.repository.sqlite_datastore_context import SQLiteDatastoreContext

app_config = application.get_app_config()

def test_sqlite_datastore_context():
    try:
        datastore_context = SQLiteDatastoreContext(app_config)
        conn = datastore_context.get_connection()
        cursor = conn.execute('select 1')
        for row in cursor:
            assert row[0] == 1
    except Exception as ex:
        assert 1 == 0