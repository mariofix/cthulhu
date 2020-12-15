from cthulhu import rise
import os

if os.getenv('FLASK_ENV'):
    app_env = os.getenv('FLASK_ENV')
else:
    app_env = "default"

rlyeh = rise(f"instance.{app_env}")
