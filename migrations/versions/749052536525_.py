"""empty message

Revision ID: 749052536525
Revises: 8d4a3a7b941d
Create Date: 2025-02-26 14:22:32.061170

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '749052536525'
down_revision = '8d4a3a7b941d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('delivery_agent',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('phone', sa.Integer(), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('delivery_area', sa.String(length=100), nullable=False),
    sa.Column('available_slots', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_delivery_agent')),
    sa.UniqueConstraint('email', name=op.f('uq_delivery_agent_email')),
    sa.UniqueConstraint('phone', name=op.f('uq_delivery_agent_phone'))
    )
    op.drop_table('delevery_agent')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('delevery_agent',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=100), nullable=True),
    sa.Column('email', sa.VARCHAR(length=100), nullable=True),
    sa.Column('phone', sa.INTEGER(), nullable=False),
    sa.Column('password', sa.VARCHAR(length=100), nullable=False),
    sa.Column('delevery_area', sa.VARCHAR(length=100), nullable=False),
    sa.Column('available_slots', sa.BOOLEAN(), nullable=False),
    sa.PrimaryKeyConstraint('id', name='pk_delevery_agent'),
    sa.UniqueConstraint('email', name='uq_delevery_agent_email'),
    sa.UniqueConstraint('phone', name='uq_delevery_agent_phone')
    )
    op.drop_table('delivery_agent')
    # ### end Alembic commands ###
