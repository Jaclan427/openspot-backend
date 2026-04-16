from fastapi import FastAPI

from app.database.supabaseClient import getSupabase

from app.routes.garageEvent import router

app = FastAPI(
  title = "OpenSpot Backend API", 
  description = "Backend service for sensor ingestion and parking status",
  version = "1.0.0"
)

app.include_router(router)

@app.get("/")
def read_root():
  return {"message": "OpenSpot backend is running"}

@app.get("/db-ping")
def db_ping():
  try: 
    dbConnect = getSupabase()
    return {
      "status": "success",
      "message": "Supabase client initialized"
    }
  except Exception as e:
    return {
      "status": "error",
      "detail": str(e)
      }
  
