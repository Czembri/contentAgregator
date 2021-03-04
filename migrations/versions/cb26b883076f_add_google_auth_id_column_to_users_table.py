"""add google_auth_id column to users table

Revision ID: cb26b883076f
Revises: b1fb0bedb04c
Create Date: 2021-03-04 14:36:02.884655

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb26b883076f'
down_revision = 'b1fb0bedb04c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('google_auth_id', sa.Text(), nullable=True))
    op.create_unique_constraint(None, 'users', ['google_auth_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'google_auth_id')
    # ### end Alembic commands ###
