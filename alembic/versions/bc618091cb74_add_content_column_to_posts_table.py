"""add content column to posts table

Revision ID: bc618091cb74
Revises: f4b180b22b6c
Create Date: 2022-06-07 09:57:42.254466

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc618091cb74'
down_revision = 'f4b180b22b6c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
