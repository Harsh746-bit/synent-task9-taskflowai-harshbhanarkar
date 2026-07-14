from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

# Extensions
db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    app.config.from_object("config.Config")

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    login_manager.login_view = "auth.login"
    login_manager.login_message_category = "info"

    # Import models
    from app.models import User, Task

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    # Import blueprints
    from app.auth.routes import auth
    from app.tasks.routes import tasks
    from app.ai import ai

    # Register blueprints
    app.register_blueprint(auth)
    app.register_blueprint(tasks)
    app.register_blueprint(ai)

    # Create database tables
    with app.app_context():
        db.create_all()

    return app