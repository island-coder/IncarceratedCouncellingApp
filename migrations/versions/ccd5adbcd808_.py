"""empty message

Revision ID: ccd5adbcd808
Revises: 7e5dbcadc154
Create Date: 2023-04-13 19:25:31.813487

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ccd5adbcd808'
down_revision = '7e5dbcadc154'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('inmate', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_of_birth', sa.DateTime(), nullable=True))

    with op.batch_alter_table('professional', schema=None) as batch_op:
        batch_op.add_column(sa.Column('bio', sa.String(length=150), nullable=True))
        batch_op.add_column(sa.Column('speciality', sa.String(length=64), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('professional', schema=None) as batch_op:
        batch_op.drop_column('speciality')
        batch_op.drop_column('bio')

    with op.batch_alter_table('inmate', schema=None) as batch_op:
        batch_op.drop_column('date_of_birth')

    # ### end Alembic commands ###
