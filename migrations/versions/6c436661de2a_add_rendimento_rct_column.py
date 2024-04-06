"""Add rendimento_rct column

Revision ID: 6c436661de2a
Revises: 
Create Date: 2024-04-04 22:21:16.749888

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c436661de2a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_giromedio')
    with op.batch_alter_table('giromedio', schema=None) as batch_op:
        batch_op.create_foreign_key(batch_op.f('fk_giromedio_user_id_usuarios'), 'usuarios', ['user_id'], ['id'])

    with op.batch_alter_table('receitamateriasprimas', schema=None) as batch_op:
        batch_op.alter_column('quantidade',
               existing_type=sa.NUMERIC(precision=10, scale=2),
               type_=sa.Numeric(precision=10, scale=3),
               existing_nullable=True)
        batch_op.alter_column('unidade',
               existing_type=sa.VARCHAR(length=12),
               type_=sa.Enum('KG', 'UN'),
               existing_nullable=True)

    with op.batch_alter_table('receitas', schema=None) as batch_op:
        batch_op.add_column(sa.Column('rendimento_rct', sa.Integer(), nullable=True))

    with op.batch_alter_table('usuarios', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_usuarios_username'), ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuarios', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_usuarios_username'), type_='unique')

    with op.batch_alter_table('receitas', schema=None) as batch_op:
        batch_op.drop_column('rendimento_rct')

    with op.batch_alter_table('receitamateriasprimas', schema=None) as batch_op:
        batch_op.alter_column('unidade',
               existing_type=sa.Enum('KG', 'UN'),
               type_=sa.VARCHAR(length=12),
               existing_nullable=True)
        batch_op.alter_column('quantidade',
               existing_type=sa.Numeric(precision=10, scale=3),
               type_=sa.NUMERIC(precision=10, scale=2),
               existing_nullable=True)

    with op.batch_alter_table('giromedio', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_giromedio_user_id_usuarios'), type_='foreignkey')

    op.create_table('_alembic_tmp_giromedio',
    sa.Column('id_gm', sa.INTEGER(), nullable=False),
    sa.Column('giro_medio', sa.INTEGER(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['usuarios.id'], name='fk_giromedio_user_id_usuarios'),
    sa.PrimaryKeyConstraint('id_gm')
    )
    # ### end Alembic commands ###
