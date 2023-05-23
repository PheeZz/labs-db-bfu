from .configuration import Configuration
import psycopg2 as pg


class DbConnector(Configuration):
    def __init__(self):
        super().__init__()

        self._db_connection_parameters = self.db_connection_parameters
        self._connection = pg.connect(**self._db_connection_parameters)
        self._cursor = self._connection.cursor()
        self._connection.autocommit = True

    @property
    def db_connection_parameters(self):
        return self._db_connection_parameters

    @property
    def connection(self):
        return self._connection

    @property
    def cursor(self):
        return self._cursor
