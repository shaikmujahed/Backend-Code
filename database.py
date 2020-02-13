# importing pool from psycopg2 
from psycopg2 import pool

#database class and selective initialisation
# creating database class
class Database:
    connection_pool = None
    @classmethod
    def initialise(cls,**kwargs):
         cls.connection_pool = pool.SimpleConnectionPool(1,10,**kwargs)
# Requesttting for a connection 
    @classmethod
    def get_connection(cls):
        return cls.connection_pool.getconn()
# returning connection back 
    @classmethod
    def return_connection(cls,connection):
        return Database.connection_pool.putconn(connection)
# closing all connections
    @classmethod
    def close_all_connections(cls):
        Database.connection_pool.closeall()

# creating CursorFromConnectionFromPool class
class CursorFromConnectionFromPool:

# creating connections and cursor seting intially None
    def __init__(self):
        self.connection = None
        self.cursor = None
# creating enter method 
    def __enter__(self):
        self.connection = Database.get_connection()
        self.cursor = self.connection.cursor()
        return self.cursor
# creating exit method
    def __exit__(self, exception_type, exception_val, exception_traceback):
        if exception_val is not None:
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        return Database.return_connection(self.connection)
    


