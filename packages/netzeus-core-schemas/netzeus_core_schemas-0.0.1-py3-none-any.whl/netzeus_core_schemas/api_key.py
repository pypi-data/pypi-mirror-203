from pydantic import BaseModel, Field, constr
from typing import Optional
from uuid import uuid4
from datetime import datetime


class NetZeusAPIKeyBase(BaseModel):
    description: Optional[str] = None
    write_enabled: Optional[bool] = False
    user_id: Optional[int]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None


class NetZeusAPIKeyCreate(NetZeusAPIKeyBase):
    api_key: str = uuid4()
    user_id: int
    created_at: datetime = datetime.utcnow()


class NetZeusAPIKeyUpdate(NetZeusAPIKeyBase):
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class NetZeusAPIKey(NetZeusAPIKeyBase):
    id: int
    api_key: Optional[str] = None

    class Config:
        orm_mode = True
