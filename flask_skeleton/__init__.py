from flask import Flask


__version__ = "0.0.0"


def load_blueprints(app):
    if app.config["REGISTER_CORE"]:
        from flask_skeleton.core import routes

        app.register_blueprint(routes.blueprint)


def create_app(config):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config)

    load_blueprints(app)

    return app
