"""empty message

Revision ID: 5faf12fad787
Revises: d1cb6eeef066
Create Date: 2023-04-16 09:31:19.219242

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5faf12fad787'
down_revision = 'd1cb6eeef066'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('appointment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('professional', sa.Integer(), nullable=True),
    sa.Column('patient', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['patient'], ['inmate.id'], name=op.f('fk_appointment_patient_inmate')),
    sa.ForeignKeyConstraint(['professional'], ['professional.id'], name=op.f('fk_appointment_professional_professional')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_appointment'))
    )
    with op.batch_alter_table('review', schema=None) as batch_op:
        batch_op.drop_constraint('fk_review_id_user', type_='foreignkey')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('review', schema=None) as batch_op:
        batch_op.create_foreign_key('fk_review_id_user', 'user', ['id'], ['id'])

    op.drop_table('appointment')
    # ### end Alembic commands ###
