from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from .models import UserData, Service, ServiceConfig
from . import appbuilder, db
from flask_appbuilder.actions import action


class UserDataView(ModelView):
    datamodel = SQLAInterface(UserData)

    list_columns = ["user_id", "user_icon", "user_country", "user_tz"]


@action(name="config", text="Config", icon='fa-folder-open-o', multiple=False, single=True)
class ServiceView(ModelView):
    datamodel = SQLAInterface(Service)
    list_columns = ["name", "active", 'url_ok']


class ServiceConfigView(ModelView):
    datamodel = SQLAInterface(ServiceConfig)

    list_columns = ["name", "data", "active"]
    related_views = [ServiceView]


"""
    Application wide 404 error handler
"""


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


db.create_all()
"""
appbuilder.add_view(
    ServiceView, "Services", icon="fa-folder-open-o", category="System"
)
appbuilder.add_view(
    ServiceConfigView,
    "Service Config",
    icon="fa-folder-open-o",
    category="System"
)
"""
