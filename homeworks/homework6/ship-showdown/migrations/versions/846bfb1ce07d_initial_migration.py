"""Initial migration

Revision ID: 846bfb1ce07d
Revises: 
Create Date: 2020-11-07 12:26:17.639661

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '846bfb1ce07d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ships',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('mass', sa.Integer(), nullable=True),
    sa.Column('speed', sa.Integer(), nullable=True),
    sa.Column('jump', sa.Integer(), nullable=True),
    sa.Column('img_id', sa.Integer(), nullable=True),
    sa.Column('deleted', sa.Boolean(), server_default='false', nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ships')
    # ### end Alembic commands ###