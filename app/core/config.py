import os
from dotenv import load_dotenv
'''
os for global ambient variables 
dotenv for load .env
'''

load_dotenv()

class Settings:
    SUPABASE_URL = os.getenv("SUP_URL")
    SUPABASE_KEY = os.getenv("SUP_KEY")

settings = Settings()