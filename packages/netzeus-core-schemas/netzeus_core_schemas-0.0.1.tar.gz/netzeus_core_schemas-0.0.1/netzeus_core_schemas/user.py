from pydantic import BaseModel, constr, Field
from typing import Optional, List
from datetime import datetime

from netzeus_core_schemas.api_key import NetZeusAPIKey


class NetZeusUserBase(BaseModel):
    email: str
    first_name: Optional[str]
    last_name: Optional[str]
    is_active: Optional[bool]
    is_superuser: Optional[bool]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    api_keys: Optional[List[NetZeusAPIKey]]


class NetZeusUserCreate(NetZeusUserBase):
    password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)


class NetZeusUserUpdate(NetZeusUserBase):
    email: Optional[str]
    password: Optional[str]
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)


class NetZeusUserWithPassword(NetZeusUserBase):
    password: Optional[constr(max_length=64)]


class NetZeusUserWithHashedPassword(NetZeusUserBase):
    hashed_password: str


class NetZeusUser(NetZeusUserBase):
    id: int

    class Config:
        orm_mode = True
