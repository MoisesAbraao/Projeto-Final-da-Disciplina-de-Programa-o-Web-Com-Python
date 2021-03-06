"""empty message

Revision ID: 22aa81d71d68
Revises: 1889020c840c
Create Date: 2015-09-01 00:27:08.458388

"""

# revision identifiers, used by Alembic.
revision = '22aa81d71d68'
down_revision = '1889020c840c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('uploads',
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('descricao', sa.String(length=50), nullable=True),
    sa.Column('arquivo', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('_id')
    )
    op.create_table('usuario_disciplina',
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.Column('disciplina_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['disciplina_id'], ['disciplina._id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario._id'], ),
    sa.PrimaryKeyConstraint('_id')
    )
    with op.batch_alter_table(u'disciplina', schema=None) as batch_op:
        batch_op.add_column(sa.Column('turma_id', sa.Integer(), nullable=True))

    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table(u'disciplina', schema=None) as batch_op:
        batch_op.drop_column('turma_id')

    op.drop_table('usuario_disciplina')
    op.drop_table('uploads')
    ### end Alembic commands ###
