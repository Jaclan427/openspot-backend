from pydantic import BaseModel
from datetime import datetime 
from typing import Literal, Optional


class SensorEvent(BaseModel):
  side_id: str
  direction: Literal["IN", "OUT"]
  timestamp: Optional[datetime] = None


