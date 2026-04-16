from pydantic import BaseModel
from datetime import datetime 
from typing import Literal, Optional


class SensorEvent(BaseModel):
  direction: Literal["IN", "OUT"]
  timestamp: Optional[datetime] = None


