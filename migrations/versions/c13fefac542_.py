"""empty message

Revision ID: c13fefac542
Revises: 378b575701cd
Create Date: 2015-09-16 23:35:00.854999

"""

# revision identifiers, used by Alembic.
revision = 'c13fefac542'
down_revision = '378b575701cd'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('uploads', schema=None) as batch_op:
        batch_op.add_column(sa.Column('disciplina_id', sa.Integer(), nullable=True))

    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('uploads', schema=None) as batch_op:
        batch_op.drop_column('disciplina_id')

    ### end Alembic commands ###