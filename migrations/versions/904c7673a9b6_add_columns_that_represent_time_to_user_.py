"""add columns that represent time to user_articles table

Revision ID: 904c7673a9b6
Revises: b92850d3951b
Create Date: 2021-01-12 21:52:10.798747

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '904c7673a9b6'
down_revision = 'b92850d3951b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_article', sa.Column('creation_time', sa.DateTime(), nullable=True))
    op.add_column('user_article', sa.Column('last_modified', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_article', 'last_modified')
    op.drop_column('user_article', 'creation_time')
    op.drop_column('users', 'last_seen')
    # ### end Alembic commands ###
