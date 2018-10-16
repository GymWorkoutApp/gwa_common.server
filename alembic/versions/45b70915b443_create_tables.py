"""create tables

Revision ID: 45b70915b443
Revises: 
Create Date: 2018-10-16 13:20:41.504004

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy.dialects.postgresql import UUID

revision = '45b70915b443'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'goals',
        sa.Column('id', UUID(as_uuid=True), nullable=False, unique=True),
        sa.Column('description', sa.String(100), nullable=False, unique=True)
    )


def downgrade():
    op.drop_table('goals')