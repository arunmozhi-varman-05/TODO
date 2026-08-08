import uuid
from sqlalchemy import Column, String, Boolean, ForeignKey, Enum as SQLEnum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import enum
from app.models.base import BaseModel

class WorkspaceRole(str, enum.Enum):
    OWNER = "OWNER"
    ADMIN = "ADMIN"
    MEMBER = "MEMBER"
    VIEWER = "VIEWER"

class Workspace(BaseModel):
    __tablename__ = "workspaces"

    name = Column(String, nullable=False)
    is_personal = Column(Boolean, default=True, nullable=False)

    members = relationship("WorkspaceMember", back_populates="workspace", cascade="all, delete-orphan")

class WorkspaceMember(BaseModel):
    __tablename__ = "workspace_members"

    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    workspace_id = Column(String(36), ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=False)
    role = Column(SQLEnum(WorkspaceRole), default=WorkspaceRole.OWNER, nullable=False)

    user = relationship("User", back_populates="workspace_memberships")
    workspace = relationship("Workspace", back_populates="members")
