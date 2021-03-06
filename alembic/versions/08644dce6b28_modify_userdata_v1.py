"""modify userdata v1

Revision ID: 08644dce6b28
Revises: 2ce21e3be231
Create Date: 2022-03-28 23:30:08.729602

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08644dce6b28'
down_revision = '2ce21e3be231'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('userdata', sa.Column('image_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'userdata', 'userimage', ['image_id'], ['Id'], ondelete='CASCADE')
    op.drop_constraint('userimage_userid_fkey', 'userimage', type_='foreignkey')
    op.drop_column('userimage', 'userid')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('userimage', sa.Column('userid', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('userimage_userid_fkey', 'userimage', 'userdata', ['userid'], ['Id'], ondelete='CASCADE')
    op.drop_constraint(None, 'userdata', type_='foreignkey')
    op.drop_column('userdata', 'image_id')
    # ### end Alembic commands ###
