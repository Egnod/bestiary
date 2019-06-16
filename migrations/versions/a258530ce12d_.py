"""empty message

Revision ID: a258530ce12d
Revises: 218dedde3478
Create Date: 2019-06-16 22:10:53.306600

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a258530ce12d'
down_revision = '218dedde3478'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('login', sa.String(length=255), nullable=False),
    sa.Column('password_hash', sa.String(length=255), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('subjects', sa.Column('user_id', sa.Integer(), nullable=True))
    op.alter_column('subjects', 'category_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('subjects', 'type_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.create_foreign_key(None, 'subjects', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'subjects', type_='foreignkey')
    op.alter_column('subjects', 'type_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('subjects', 'category_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('subjects', 'user_id')
    op.drop_table('users')
    # ### end Alembic commands ###