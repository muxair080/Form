"""pure form

Revision ID: 5c7f4dacc766
Revises: 08644dce6b28
Create Date: 2022-03-28 23:42:56.817197

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c7f4dacc766'
down_revision = '08644dce6b28'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('userdata', 'image_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('userdata', sa.Column('image_id', sa.INTEGER(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
