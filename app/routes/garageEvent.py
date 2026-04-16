from fastapi import APIRouter
from app.models.sensorEvent import SensorEvent
from app.state.counterStore import applyEvent
from app.state.counterStore import getStatus
from app.database.supabaseClient import getSupabase
from app.services.garageService import getGrandStudentParking
from datetime import datetime

router = APIRouter()

supabase = getSupabase()

@router.get("/status")
def callStatus():
  return getGrandStudentParking()

@router.post("/event")
def recievesEvent(event: SensorEvent):
  if event.timestamp is None:
    event.timestamp = datetime.utcnow()
  
  supabase.table("Events").insert({
    "side_id": event.side_id,
    "direction": event.direction,
    "timestamp": event.timestamp.isoformat()
  }).execute()

  applyEvent(event)
  status = getStatus()

  supabase.table("garage_status").update({
    "occupied": status["occupied"],
    "available": status["available"],
    "capacity": status["capacity"]
  }).eq("id", 1).execute()

  return status
