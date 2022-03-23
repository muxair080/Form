"""create user table

Revision ID: 30700a90c7af
Revises: a13802ab87cc
Create Date: 2022-03-20 22:26:19.964113

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30700a90c7af'
down_revision = 'a13802ab87cc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('Id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
