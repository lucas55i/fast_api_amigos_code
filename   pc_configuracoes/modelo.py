from typing import Optional
from uuid import UUID
import uuid
from pydantic import BaseModel
from uuid import UUID, uuid4


class PcConfig(BaseModel):
    id: Optional[UUID] = uuid4()
    cpu: str
    ram: str
    motherboard: str
    video_card: str
    hd_ssd: str
    source: str


class UpdateConfig(BaseModel):
    cpu: Optional[str]
    ram: Optional[str]
    motherboard: Optional[str]
    video_card: Optional[str]
    hd_ssd: Optional[str]
    source: Optional[str]
