from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    supabase_url: str = os.getenv("SUPABASE_URL")
    supabase_key: str = os.getenv("SUPABASE_KEY")
    
    class Config:
        env_file = ".env"

settings = Settings()