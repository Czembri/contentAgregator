"""add user_article table

Revision ID: 2ec3f6fc404e
Revises: 0083b68d8d6a
Create Date: 2021-01-06 00:04:54.900693

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ec3f6fc404e'
down_revision = '0083b68d8d6a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_article',
    sa.Column('article_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=500), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('article_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_article')
    # ### end Alembic commands ###
