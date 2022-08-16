from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# ORM configuration
db = SQLAlchemy()
# This is to be changed when using PGAdmin PostgreSQL
#DB_NAME = "database.db"

# Default Python Package creation.
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "webAppsCSCI"
    # change below to use a local sql lite ORM file
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{{DB_NAME}}'
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:lopezs20@localhost/blogposts"
    db.init_app(app)

    # Get view and authorization models to make endpoints accessible
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Post, Comment, Like
    create_database(app)
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    # Only show login when first visiting site (non-cacheable)
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

# define an ORM file based on SQLAclchemy lite 
def create_database(app):
    #if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)
        print("Created database!")
