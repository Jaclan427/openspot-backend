from app.database.supabaseClient import getSupabase

def getGrandStudentParking():
    supabase = getSupabase()

    response = (
        supabase
        .table("garage_status")
        .select("*")
        .eq("garage_name", "Grand")
        .eq("parking_type", "student")
        .single()
        .execute()
    )

    row = response.data

    return {
        "occupied": row["occupied"],
        "available": row["available"],
        "capacity": row["capacity"]
    }


def updateGrandStudentParking(direction: str):
  supabase = getSupabase()

  response = (
    supabase
    .table("garage_status")
    .select("*")
    .eq("garage_name", "Grand")
    .eq("parking_type", "student")
    .single()
    .execute()
  )

  
  row = response.data

  occupied = row["occupied"]
  available = row["available"]
  capacity = row["capacity"]

  if direction == "IN":
    if occupied < capacity:
        occupied += 1
        available -= 1

  elif direction == "OUT":
     if occupied > 0:
        occupied -= 1
        available += 1

  update_response = (
     supabase
     .table("garage_status")
     .update({
          "occupied": occupied,
          "available": available
     })
     .eq("garage_name", "Grand")
     .eq("parking_type", "student")
     .execute()
  )

  return {
     "occupied": occupied,
     "available": available,
     "capacity": capacity
  }