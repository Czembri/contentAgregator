"""add article_attachments table"

Revision ID: e36ab3d51042
Revises: a3a4779d4d8a
Create Date: 2021-01-06 01:05:21.639729

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e36ab3d51042'
down_revision = 'a3a4779d4d8a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('article_attachments',
    sa.Column('attachment_id', sa.Integer(), nullable=False),
    sa.Column('article_id', sa.Integer(), nullable=True),
    sa.Column('file_name', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['article_id'], ['user_article.article_id'], ),
    sa.PrimaryKeyConstraint('attachment_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('article_attachments')
    # ### end Alembic commands ###
