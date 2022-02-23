"""add column content

Revision ID: 621b0158c22b
Revises: b404185682c6
Create Date: 2022-02-23 11:04:30.838071

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '621b0158c22b'
down_revision = 'b404185682c6'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('content', sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
