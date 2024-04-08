"""empty message

Revision ID: 76ae94046a60
Revises: 6c436661de2a
Create Date: 2024-04-08 17:02:13.583970

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76ae94046a60'
down_revision = '6c436661de2a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('produc', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nome_rct', sa.String(length=75), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('produc', schema=None) as batch_op:
        batch_op.drop_column('nome_rct')

    # ### end Alembic commands ###
