from flask_skeleton.core import blueprint


@blueprint.route("/")
def route_default():
    return "/"
