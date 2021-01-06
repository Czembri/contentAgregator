"""drop fk user_id from user_article table

Revision ID: 9d62130f1dcc
Revises: ec1e7032d043
Create Date: 2021-01-06 00:22:35.125698

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9d62130f1dcc'
down_revision = '2ec3f6fc404e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('user_article_ibfk_1', 'user_article', type_='foreignkey')
    op.drop_column('user_article', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_article', sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('user_article_ibfk_1', 'user_article', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###
