from flask_skeleton import create_app
from config import config
import os


if os.getenv('FLASK_ENV'):
    app_env = os.getenv('FLASK_ENV')
else:
    app_env = "default"

app = create_app(config[app_env])

if __name__ == "__main__":
    app.run()
