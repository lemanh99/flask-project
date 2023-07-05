"""create inital tables user

Revision ID: 672ab27fe0d8
Revises: 1ff5d2021596
Create Date: 2023-07-05 18:50:33.532559

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '672ab27fe0d8'
down_revision = '1ff5d2021596'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('email', sa.Text(), nullable=False),
    sa.Column('first_name', sa.Text(), nullable=True),
    sa.Column('last_name', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
