from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.types import DateTime
from uuid import uuid4
from transaction_service.models import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
        unique=True,
        nullable=False
    )
    created_at = db.Column(DateTime, server_default=db.func.now(), nullable=False)
    modified_at = db.Column(DateTime, server_default=db.func.now(), onupdate=db.func.now(), nullable=False)
