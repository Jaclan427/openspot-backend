#Implemented the OS module to use the SUPABASE_URL 
import os

#Import load_dotenv to rad variables from a .env file 
from dotenv import load_dotenv

#Import the Supabase client creator and the client type 
#create_client() establish the connection to Supabase
#Client is a type hint
from supabase import create_client, Client



#Load environement variables from the .env file into the memory 
load_dotenv()

#Reads the SUPABASE_URL and SUPABASE_KEY from the environement variables
#Creating a Supabase client connection 
def getSupabase() -> Client:
  #Getting the Supabase URL from the environment variables 
  supabase_url = os.getenv("SUPABASE_URL")
  #Getting the key for the backend to communicate with the Supabase 
  supabase_key = os.getenv("SUPABASE_KEY")

  #If the key or the URL is missing, stop execution 
  if not supabase_url or not supabase_key:
    raise RuntimeError(
      "SUPABASE_URL and SUPABASE_KEY must be set in your .env file"
    )
  
  #Creating the Supabase client using the URL and the API key
  supabase: Client = create_client(supabase_url, supabase_key)

  #Returning the connected Supabase Client 
  return supabase