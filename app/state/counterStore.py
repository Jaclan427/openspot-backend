
current_count = 0
capacity = 150


def applyEvent(event):
  global current_count 
  if event.direction == "IN":
    if current_count < capacity:
      current_count += 1
 
  elif event.direction == "OUT":
    if current_count > 0:
      current_count -= 1
  
    

def getStatus():
  return {
    "occupied": current_count,
    "available": capacity - current_count,
    "capacity": capacity
  }