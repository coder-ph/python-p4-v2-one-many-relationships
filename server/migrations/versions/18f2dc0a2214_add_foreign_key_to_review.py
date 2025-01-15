"""add foreign key to review

Revision ID: 18f2dc0a2214
Revises: c41c00d341b2
Create Date: 2025-01-15 12:12:16.359793

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18f2dc0a2214'
down_revision = 'c41c00d341b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reviews', sa.Column('employee_id', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk_reviews_employee_id_employees'), 'reviews', 'employees', ['employee_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_reviews_employee_id_employees'), 'reviews', type_='foreignkey')
    op.drop_column('reviews', 'employee_id')
    # ### end Alembic commands ###
