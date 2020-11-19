"""empty message

Revision ID: 537abacae381
Revises: ac35dd8b89c5
Create Date: 2020-11-18 22:52:24.082253

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '537abacae381'
down_revision = 'ac35dd8b89c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('instance', sa.Column('ip', sa.String(), nullable=True))
    op.drop_column('instance', 'ipaddr')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('instance', sa.Column('ipaddr', sa.TEXT(), autoincrement=False, nullable=True))
    op.drop_column('instance', 'ip')
    # ### end Alembic commands ###
