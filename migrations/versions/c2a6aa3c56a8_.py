"""empty message

Revision ID: c2a6aa3c56a8
Revises: ccd5adbcd808
Create Date: 2023-04-13 21:26:15.800690

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2a6aa3c56a8'
down_revision = 'ccd5adbcd808'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('inmate', schema=None) as batch_op:
        batch_op.add_column(sa.Column('medical_history', sa.String(length=500), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('inmate', schema=None) as batch_op:
        batch_op.drop_column('medical_history')

    # ### end Alembic commands ###
