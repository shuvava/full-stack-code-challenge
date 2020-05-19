from flask import (blueprints, jsonify, request, make_response)
from transaction_service.services.account_service import service as account_service
from .request_validators import validate_account_post_request

account_blueprint = blueprints.Blueprint('account', __name__)


@account_blueprint.route('/accounts', methods=['POST'])
def create_account():
    request_json = request.get_json()
    try:
        validate_account_post_request(request_json)
    except ValueError as e:
        return make_response(
            jsonify({
                'message': 'Request Failed',
                'errors': [str(e)],
            }), 400)

    account = account_service.create_account(request_json)
    return make_response(jsonify(account), 201)


@account_blueprint.route('/accounts', methods=['GET'])
def get_accounts():
    page = request.args.get('page', 1, int)
    per_page = request.args.get('per_page', 20, int)
    accounts = account_service.get_accounts(page, per_page)
    return make_response(jsonify(accounts), 200)
