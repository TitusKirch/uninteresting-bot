"""base

Revision ID: 6b3c595a7a1e
Revises: 
Create Date: 2020-01-25 02:19:35.458545

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b3c595a7a1e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    settings_table = op.create_table('settings',
        sa.Column('name', sa.String, primary_key=True),
        sa.Column('value', sa.String))
    op.create_table('extensions',
        sa.Column('name', sa.String, primary_key=True),
        sa.Column('isLoaded', sa.Boolean, server_default=u'false'),
        sa.Column('description', sa.Text))
    
    op.bulk_insert(settings_table,[
        {
            'name': 'status_name',
            'value': 'uninteresting.dev'
        },
    ])

def downgrade():
    op.drop_table('settings')
    op.drop_table('extensions')
