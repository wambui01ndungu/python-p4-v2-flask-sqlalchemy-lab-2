"""remane review

Revision ID: 10da94d8eb8d
Revises: 182a082d561e
Create Date: 2024-11-19 21:09:15.703650

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10da94d8eb8d'
down_revision = '182a082d561e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    op.rename_table('review', 'reviews')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    op.rename_table('reviews', 'review')
    # ### end Alembic commands ###
