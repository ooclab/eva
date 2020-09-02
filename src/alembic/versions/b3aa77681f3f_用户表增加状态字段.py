"""用户表增加状态字段

Revision ID: b3aa77681f3f
Revises: 2c831198c168
Create Date: 2020-09-01 17:31:52.197160

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b3aa77681f3f"
down_revision = "2c831198c168"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        "eva_credential_identity_id_fkey", "eva_credential", type_="foreignkey"
    )
    op.create_foreign_key(
        None,
        "eva_credential",
        "eva_identity",
        ["identity_id"],
        ["id"],
        ondelete="CASCADE",
    )
    op.drop_constraint(
        "eva_identity__role_identity_id_fkey", "eva_identity__role", type_="foreignkey"
    )
    op.drop_constraint(
        "eva_identity__role_role_id_fkey", "eva_identity__role", type_="foreignkey"
    )
    op.create_foreign_key(
        None,
        "eva_identity__role",
        "eva_identity",
        ["identity_id"],
        ["id"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        None, "eva_identity__role", "eva_role", ["role_id"], ["id"], ondelete="CASCADE"
    )
    op.drop_constraint(
        "eva_password_credential_id_fkey", "eva_password", type_="foreignkey"
    )
    op.create_foreign_key(
        None,
        "eva_password",
        "eva_credential",
        ["credential_id"],
        ["id"],
        ondelete="CASCADE",
    )
    op.drop_constraint(
        "eva_role__permission_permission_id_fkey",
        "eva_role__permission",
        type_="foreignkey",
    )
    op.drop_constraint(
        "eva_role__permission_role_id_fkey", "eva_role__permission", type_="foreignkey"
    )
    op.create_foreign_key(
        None,
        "eva_role__permission",
        "eva_permission",
        ["permission_id"],
        ["id"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        None,
        "eva_role__permission",
        "eva_role",
        ["role_id"],
        ["id"],
        ondelete="CASCADE",
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "eva_role__permission", type_="foreignkey")
    op.drop_constraint(None, "eva_role__permission", type_="foreignkey")
    op.create_foreign_key(
        "eva_role__permission_role_id_fkey",
        "eva_role__permission",
        "eva_role",
        ["role_id"],
        ["id"],
    )
    op.create_foreign_key(
        "eva_role__permission_permission_id_fkey",
        "eva_role__permission",
        "eva_permission",
        ["permission_id"],
        ["id"],
    )
    op.drop_constraint(None, "eva_password", type_="foreignkey")
    op.create_foreign_key(
        "eva_password_credential_id_fkey",
        "eva_password",
        "eva_credential",
        ["credential_id"],
        ["id"],
    )
    op.drop_constraint(None, "eva_identity__role", type_="foreignkey")
    op.drop_constraint(None, "eva_identity__role", type_="foreignkey")
    op.create_foreign_key(
        "eva_identity__role_role_id_fkey",
        "eva_identity__role",
        "eva_role",
        ["role_id"],
        ["id"],
    )
    op.create_foreign_key(
        "eva_identity__role_identity_id_fkey",
        "eva_identity__role",
        "eva_identity",
        ["identity_id"],
        ["id"],
    )
    op.drop_constraint(None, "eva_credential", type_="foreignkey")
    op.create_foreign_key(
        "eva_credential_identity_id_fkey",
        "eva_credential",
        "eva_identity",
        ["identity_id"],
        ["id"],
    )
    # ### end Alembic commands ###
