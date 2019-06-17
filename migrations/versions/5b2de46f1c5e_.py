"""empty message

Revision ID: 5b2de46f1c5e
Revises: 7578f0bc5206
Create Date: 2019-06-17 12:25:31.753089

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b2de46f1c5e'
down_revision = '7578f0bc5206'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'users', ['login'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    # ### end Alembic commands ###
