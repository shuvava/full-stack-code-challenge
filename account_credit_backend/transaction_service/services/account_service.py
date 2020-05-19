from transaction_service.models.account import Account, AccountSerializer, db
from logging import error


class AccountService:
    def __init__(self, database):
        self.db = database

    def create_account(self, account_info):
        account = Account(orgunit_id=account_info['orgunit_id'])

        try:
            self.db.session.add(account)
            self.db.session.commit()
        except ValueError as e:
            error('Account creation failed: %s', e)

        return AccountSerializer().dump(account)

    def get_accounts(self, page, per_page):
        query = Account.query.paginate(page, per_page, False)
        total = query.total
        record_items = query.items

        return {
            'total': total,
            'entities': AccountSerializer(many=True).dump(record_items),
            'page': page,
            'per_page': per_page,
            'next_page': query.next_num
        }


service = AccountService(db)
