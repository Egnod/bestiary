"""empty message

Revision ID: 8837252106ef
Revises: a258530ce12d
Create Date: 2019-06-16 22:13:00.703299

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8837252106ef'
down_revision = 'a258530ce12d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('subjects', 'category_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('subjects', 'type_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('subjects', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('subjects', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('subjects', 'type_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('subjects', 'category_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###