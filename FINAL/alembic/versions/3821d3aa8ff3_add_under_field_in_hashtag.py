"""add under field in hashtag

Revision ID: 3821d3aa8ff3
Revises: 558bd3f07675
Create Date: 2014-10-24 21:43:32.745609

"""

# revision identifiers, used by Alembic.
revision = '3821d3aa8ff3'
down_revision = '558bd3f07675'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column(u'hashtag', sa.Column('under_id', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'hashtag', 'under_id')
    ### end Alembic commands ###
