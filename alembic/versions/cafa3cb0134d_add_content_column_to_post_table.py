"""add content column to post table

Revision ID: cafa3cb0134d
Revises: cb6cbe9ce54a
Create Date: 2025-12-22 02:02:45.575257

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cafa3cb0134d'
down_revision: Union[str, Sequence[str], None] = 'cb6cbe9ce54a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
