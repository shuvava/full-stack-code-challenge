from sqlalchemy.dialects.postgresql import UUID
from transaction_service.models.base_model import BaseModel
from .credit_pack import CreditPack
from . import db, ma


class Account(BaseModel):
    __tablename__ = 'account'

    orgunit_id = db.Column(UUID(as_uuid=True), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    deleted = db.Column(db.Boolean(), default=False, nullable=False)
    credits = db.relationship('CreditPack', backref='account')


class AccountSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Account

    id = ma.auto_field()
    orgunit_id = ma.auto_field()
    created_at = ma.auto_field()
    modified_at = ma.auto_field()
    active = ma.auto_field()
    deleted = ma.auto_field()
