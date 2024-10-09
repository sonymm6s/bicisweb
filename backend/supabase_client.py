# backend/supabase_client.py
import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Cargar las variables de entorno (si usas dotenv)
load_dotenv()

# Configura el URL y la clave de Supabase
SUPABASE_URL = "https://hdnnlvszpzxjkuoenadf.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imhkbm5sdnN6cHp4amt1b2VuYWRmIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcyODQ2MTY1MCwiZXhwIjoyMDQ0MDM3NjUwfQ.NEeKUD_TMNnP8I-IXf0P52vu3NImpTS75BMKP2lhKRQ"

# Crear cliente de Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

