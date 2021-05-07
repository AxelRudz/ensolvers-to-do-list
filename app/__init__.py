from os import path, environ
from flask import Flask, render_template, g
from flask_session import Session
from config import config
from app import db
from app.resources import user
from app.resources import folder
from app.resources import task
from app.helpers import auth as helper_auth


def create_app(environment="development"):
    
    app = Flask(__name__)

    # Load config
    env = environ.get("FLASK_ENV", environment)
    app.config.from_object(config[env])

    # Server Side session
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)

    # Configure db
    db.init_app(app)

    # Functions exported to Jinja2's context
    app.jinja_env.globals.update(is_authenticated=helper_auth.authenticated)
    
    # Home route
    @app.route('/')
    def index():
        return render_template("index.html")

    # User routes
    app.add_url_rule("/user-login", "user-login", user.login, methods=["POST"])
    app.add_url_rule("/user-logout", "user-logout", user.logout)
    app.add_url_rule("/main-menu", "user-main-menu", user.main_menu)

    # Folder routes
    app.add_url_rule("/folder-show", "folder-show",   folder.show)
    app.add_url_rule("/folder-create", "folder-create", folder.create, methods=["POST"])
    app.add_url_rule("/folder-delete", "folder-delete", folder.delete, methods=["POST"])

    # Task routes
    app.add_url_rule("/task-create", "task-create", task.create, methods=["POST"])
    app.add_url_rule("/task-delete", "task-delete", task.delete, methods=["POST"])
    app.add_url_rule("/task-update", "task-update", task.update, methods=["POST"])
    app.add_url_rule("/task-check", "task-check", task.check, methods=["POST"])

    
    # Retornar la instancia de app configurada
    return app
