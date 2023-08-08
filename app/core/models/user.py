import uuid

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

from app.core.models.base import Base


class User(Base):
    __tablename__ = "users"

    id = sa.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = sa.Column(sa.Text, nullable=False)
    first_name = sa.Column(sa.Text, nullable=True)
    last_name = sa.Column(sa.Text, nullable=True)
