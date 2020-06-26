from src.app import app
import src.configurations as config


application = app

if __name__ == '__main__':
    application.run(debug=config.DEV_DEBUG)
