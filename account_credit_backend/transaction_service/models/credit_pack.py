from sqlalchemy.dialects.postgresql import UUID
from transaction_service.models.base_model import BaseModel
from sqlalchemy.schema import ForeignKey
from sqlalchemy.types import Date, Boolean, BigInteger

from . import db, ma

CREDIT_TYPES = ('promotional', 'regular')
CREDIT_ENUM = db.Enum(*CREDIT_TYPES, name='credit_types', create_type=True)


class CreditPack(BaseModel):
    __tablename__ = 'credit'

    account_id = db.Column(
        UUID(as_uuid=True),
        ForeignKey('account.id'),
        nullable=False
    )
    credit_type = db.Column(CREDIT_ENUM, nullable=False)
    expiry_date = db.Column(Date, name='expiry_date', nullable=False)
    expired = db.Column(Boolean, name='expired', default=False, nullable=False)
    depleted = db.Column(Boolean, name='depleted', default=False, nullable=False)
    amount = db.Column(BigInteger, name='amount', nullable=False)


class CreditPackSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CreditPack

    id = ma.auto_field()
    account_id = ma.auto_field()
    created_at = ma.auto_field()
    modified_at = ma.auto_field()
    credit_type = ma.auto_field()
