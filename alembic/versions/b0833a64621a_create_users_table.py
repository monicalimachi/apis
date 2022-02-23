"""create users table

Revision ID: b0833a64621a
Revises: 621b0158c22b
Create Date: 2022-02-23 11:09:51.032380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0833a64621a'
down_revision = '621b0158c22b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users', 
    sa.Column('id', sa.Integer(), nullable=False,primary_key=True), 
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'), sa.UniqueConstraint('email'))


def downgrade():
    op.drop_table('users')
    pass
