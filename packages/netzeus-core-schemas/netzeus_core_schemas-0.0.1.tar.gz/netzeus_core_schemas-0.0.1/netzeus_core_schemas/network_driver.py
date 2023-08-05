from pydantic import BaseModel, constr, Field
from typing import Optional, List, TYPE_CHECKING
from datetime import datetime

from netzeus_core_schemas.enums import NetZeusNetworkDriverConnectionMethodEnum
from netzeus_core_schemas.device import NetZeusDevice


class NetZeusNetworkDriverBase(BaseModel):
    vendor: str
    platform: Optional[str]
    # supported_versions: Optional[List[str]] = []
    connection_method: NetZeusNetworkDriverConnectionMethodEnum
    connection_parameters: Optional[dict]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    devices: Optional[List[NetZeusDevice]] = []


class NetZeusNetworkDriverCreate(NetZeusNetworkDriverBase):
    platform: str
    devices: List[int] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)


class NetZeusNetworkDriverUpdate(NetZeusNetworkDriverBase):
    platform: Optional[str]
    vendor: Optional[str]
    connection_method: Optional[NetZeusNetworkDriverConnectionMethodEnum]
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)


class NetZeusNetworkDriver(NetZeusNetworkDriverBase):
    id: int

    class Config:
        orm_mode = True
