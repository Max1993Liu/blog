"""create vocabulary table


Revision ID: 46a262d3b9d5
Revises: 
Create Date: 2020-01-31 15:56:51.401834

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46a262d3b9d5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vocabulary',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=20), nullable=True),
    sa.Column('word', sa.String(length=120), nullable=True),
    sa.Column('phonetic', sa.String(length=120), nullable=True),
    sa.Column('meaning', sa.String(length=240), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_vocabulary_category'), 'vocabulary', ['category'], unique=False)
    op.create_index(op.f('ix_vocabulary_word'), 'vocabulary', ['word'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_vocabulary_word'), table_name='vocabulary')
    op.drop_index(op.f('ix_vocabulary_category'), table_name='vocabulary')
    op.drop_table('vocabulary')
    # ### end Alembic commands ###
