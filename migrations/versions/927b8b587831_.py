"""empty message

Revision ID: 927b8b587831
Revises: 
Create Date: 2023-04-12 17:36:55.961651

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '927b8b587831'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('institute',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_institute'))
    )
    with op.batch_alter_table('institute', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_institute_title'), ['title'], unique=True)

    op.create_table('professional',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('first_name', sa.String(length=64), nullable=False),
    sa.Column('last_name', sa.String(length=64), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_professional')),
    sa.UniqueConstraint('username', name=op.f('uq_professional_username'))
    )
    op.create_table('inmate',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('first_name', sa.String(length=64), nullable=False),
    sa.Column('last_name', sa.String(length=64), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('in_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['in_id'], ['institute.id'], name=op.f('fk_inmate_in_id_institute')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_inmate')),
    sa.UniqueConstraint('username', name=op.f('uq_inmate_username'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('inmate')
    op.drop_table('professional')
    with op.batch_alter_table('institute', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_institute_title'))

    op.drop_table('institute')
    # ### end Alembic commands ###