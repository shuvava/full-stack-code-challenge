from transaction_service import app as transaction_app


def import_models():
    from transaction_service.models.account import Account
    from transaction_service.models.credit_pack import CreditPack


import_models()
app = transaction_app.create_app()
