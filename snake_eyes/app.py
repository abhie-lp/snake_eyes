"""Main application file"""

from celery import Celery
from flask import Flask

from .extensions import debug_toolbar
from .blueprints import page, contact

CELERY_TASK_LIST = []


def create_celery_app(app: Flask = None):
    """Create new Celery object with Celery and app config"""
    app = app or create_app()
    celery = Celery(app.import_name, broker=app.config["CELERY_BROKER_URL"],
                    include=CELERY_TASK_LIST)
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        """Class to setup context for each task"""
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return super(ContextTask, self).__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery


def create_app(settings_override: dict = None) -> Flask:
    """Create Flask application using the app factory pattern"""
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object("config.settings")
    app.config.from_pyfile("settings.py", silent=True)

    if settings_override:
        app.config.update(settings_override)

    app.register_blueprint(page.page)
    app.register_blueprint(contact.contact)

    extensions(app)

    return app


def extensions(app: Flask) -> None:
    """Integrate all the extensions in the app"""
    debug_toolbar.init_app(app)


celery_app = create_celery_app()
