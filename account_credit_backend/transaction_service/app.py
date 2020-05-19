from flask import Flask, jsonify
from flask_migrate import Migrate

from transaction_service import config
from transaction_service.models import db, ma
from .route import register_blueprints
from .exceptions import TransactionServiceException

migrate = Migrate()


def register_error_handlers(app):
    """Register error handlers for app"""

    @app.errorhandler(TransactionServiceException)
    def handle_exception(e):
        return jsonify({'message': str(e)}), 400

    @app.errorhandler(ValueError)
    def handle_validation_error(e):
        return str(e), 400


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)
    app.db = db
    app.migrate = migrate

    ma.init_app(app)
    app.ma = ma

    register_error_handlers(app)
    register_blueprints(app)

    return app


transaction_service = create_app()
