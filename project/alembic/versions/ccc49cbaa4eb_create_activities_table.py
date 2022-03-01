"""create activities table
Revision ID: ccc49cbaa4eb
Revises: 
Create Date: 2022-02-28 14:11:25.593390
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import create_engine


revision = 'ccc49cbaa4eb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "activities_info",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("activite_name", sa.String(100), nullable=False),
        sa.Column("activite_description", sa.String(300), nullable=False),
        sa.Column("activite_todo_list", sa.String(300), nullable=False),
        sa.Column("activite_conditions", sa.Integer, nullable=False), # słownik {numer: link do jpg}, osobna tabel?
        sa.Column("activite_calories", sa.String(300)), 
        sa.Column("activite_favorite", sa.Boolean),
    )
def downgrade():
    op.drop_table("activities_info")
