from pydantic import BaseModel, constr, Field
from typing import Optional, List, TYPE_CHECKING
from datetime import datetime
from ipaddress import IPv4Address, IPv6Address


class NetZeusDeviceBase(BaseModel):
    slug: constr(regex="^[A-Za-z0-9-]*$", min_length=1)
    friendly_name: Optional[str]
    ipv4_address: Optional[IPv4Address]
    ipv6_address: Optional[IPv6Address]
    openconfig_supported: Optional[bool]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    network_driver_id: Optional[int]


class NetZeusDeviceCreate(NetZeusDeviceBase):
    created_at: datetime = Field(default_factory=datetime.utcnow)


class NetZeusDeviceUpdate(NetZeusDeviceBase):
    slug: Optional[str]
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)


class NetZeusDevice(NetZeusDeviceBase):
    id: int

    class Config:
        orm_mode = True
