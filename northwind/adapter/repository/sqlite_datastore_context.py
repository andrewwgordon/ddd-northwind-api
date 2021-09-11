from northwind.adapter.repository.i_datastore_context import IDatastoreContext
import sqlite3
import logging

log = logging.getLogger(__name__)

class SQLiteDatastoreContext(IDatastoreContext):

    def __init__(self,app_config) -> None:
        self.__app_config = app_config
    
    def open(self) -> None:
        raise NotImplementedError("Not required for SQLite")
    
    def get_connection(self) -> sqlite3.Connection:
        try:
            conn = sqlite3.connect(self.__app_config['database']['uri'])
            return conn
        except Exception as ex:
            log.error(ex.args[0])
            raise ex
    
    def close_connection(self,conn: sqlite3.Connection) -> None:
        try:
            conn.commit()
            conn.close()
        except Exception as ex:
            log.error(ex.args[0])

        