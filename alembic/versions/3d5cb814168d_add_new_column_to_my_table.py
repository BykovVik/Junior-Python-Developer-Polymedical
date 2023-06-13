"""add new column to my table

Revision ID: 3d5cb814168d
Revises: c99d9c001a7b
Create Date: 2023-06-12 20:26:59.433849

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d5cb814168d'
down_revision = 'c99d9c001a7b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table('Students') as batch_op:
        batch_op.alter_column('group_id', nullable=True)


def downgrade() -> None:
    pass
