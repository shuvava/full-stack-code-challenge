"""Routes registering blueprints"""
from transaction_service.api.v1 import health_check_blueprint, account_blueprint


def register_blueprints(app):
    register_v1_blueprints(app)


def register_v1_blueprints(app):
    v1_prefix = '/api/v1'

    app.register_blueprint(health_check_blueprint, url_prefix=v1_prefix)
    app.register_blueprint(account_blueprint, url_prefix=v1_prefix)
