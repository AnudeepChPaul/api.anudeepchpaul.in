from src.configurations import config
from src.app import app

application = app

if __name__ == '__main__':
    application.run(debug=config.bool('DEBUG_MODE'), threaded=True)
