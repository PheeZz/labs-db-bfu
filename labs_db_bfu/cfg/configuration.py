from dotenv import load_dotenv
from os import getenv


class Configuration:
    def __init__(self):
        load_dotenv(override=True)

        self._db_connection_parameters = {
            'host': getenv('DB_HOST'),
            'port': getenv('DB_PORT'),
            'user': getenv('DB_USER'),
            'password': getenv('DB_USER_PASSWORD'),
            'database': getenv('DB_NAME'),
        }

    @property
    def db_connection_parameters(self):
        return self._db_connection_parameters
