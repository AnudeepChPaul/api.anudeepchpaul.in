from src.app import app
from src.db import init_db_connection
import src.configurations as config


application = app

if __name__ == '__main__':
    """ init_db_connection() """
    """ host=config.DEV_HOST,
        port=config.DEV_PORT, """
    application.run(debug=config.DEV_DEBUG)
