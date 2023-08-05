import uuid

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func


class IntegerIDMixin:
    id = sa.Column(sa.Integer, primary_key=True)


class UUIDMixin:
    id = sa.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)


class SimpleAuditMixin:
    created_at = sa.Column(sa.DateTime(timezone=True), default=func.now())
    updated_at = sa.Column(sa.DateTime(timezone=True), onupdate=func.now())
