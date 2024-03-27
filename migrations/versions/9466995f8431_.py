"""empty message

Revision ID: 9466995f8431
Revises: 1f79b29e42dc
Create Date: 2024-03-26 22:39:56.614484

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9466995f8431'
down_revision = '1f79b29e42dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.String(length=100),
               existing_nullable=False)
        batch_op.alter_column('race',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.String(length=100),
               nullable=True)
        batch_op.alter_column('loyal_to',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.String(length=100),
               existing_nullable=False)
        batch_op.alter_column('height',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('weight',
               existing_type=sa.INTEGER(),
               nullable=False)

    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.add_column(sa.Column('diameter', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('rotation_period', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('orbital_period', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('terrain', sa.String(length=200), nullable=False))
        batch_op.drop_column('name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.VARCHAR(length=20), autoincrement=False, nullable=False))
        batch_op.drop_column('terrain')
        batch_op.drop_column('orbital_period')
        batch_op.drop_column('rotation_period')
        batch_op.drop_column('diameter')

    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.alter_column('weight',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('height',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('loyal_to',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=20),
               existing_nullable=False)
        batch_op.alter_column('race',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=20),
               nullable=False)
        batch_op.alter_column('name',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=20),
               existing_nullable=False)

    # ### end Alembic commands ###