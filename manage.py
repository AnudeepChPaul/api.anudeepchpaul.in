from src.app import app
from src.db import init_db_connection
import src.configurations as config


def start():
    init_db_connection()
    app.run(
        host=config.DEV_HOST,
        port=config.DEV_PORT,
        debug=config.DEV_DEBUG
    )


if __name__ == '__main__':
    start()
