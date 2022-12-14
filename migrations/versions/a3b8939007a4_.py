"""empty message

Revision ID: a3b8939007a4
Revises: 8b348cb5fa6c
Create Date: 2022-08-15 23:42:13.982779

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a3b8939007a4'
down_revision = '8b348cb5fa6c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('character_homeworld', sa.String(length=250), nullable=False),
    sa.Column('character_name', sa.String(length=250), nullable=True),
    sa.Column('character_skill', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('planet_population', sa.Integer(), nullable=False),
    sa.Column('planet_diameter', sa.Integer(), nullable=False),
    sa.Column('planet_climate', sa.String(length=250), nullable=False),
    sa.Column('planet_name', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.add_column('user', sa.Column('username', sa.String(length=40), nullable=False))
    op.alter_column('user', 'is_active',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True)
    op.drop_index('email', table_name='user')
    op.drop_index('email_2', table_name='user')
    op.create_unique_constraint(None, 'user', ['id'])
    op.create_unique_constraint(None, 'user', ['username'])
    op.drop_column('user', 'email')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', mysql.VARCHAR(length=120), nullable=False))
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_constraint(None, 'user', type_='unique')
    op.create_index('email_2', 'user', ['email'], unique=False)
    op.create_index('email', 'user', ['email'], unique=False)
    op.alter_column('user', 'is_active',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False)
    op.drop_column('user', 'username')
    op.drop_table('planet')
    op.drop_table('character')
    # ### end Alembic commands ###
