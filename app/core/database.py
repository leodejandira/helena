from supabase import create_client, Client
from app.core.config import settings
import os

def get_supabase() -> Client:
    '''
    Return supabase client configured with url and key environment variables
    '''
    # Force clean client creation without proxy parameters
    client = create_client(
        supabase_url=settings.SUPABASE_URL,
        supabase_key=settings.SUPABASE_KEY
    )
    return client

# Connection test
def test_connection():
    '''
    Test for supabase connection with a simple query on plans table
    '''
    try:
        supabase = get_supabase()
        result = supabase.table('plans').select('*').limit(1).execute()
        print("✅ Supabase connection established!")
        print(f"Test data: {result.data}")
        return True
    except Exception as e:
        print(f"❌ Connection error: {e}")
        return False

# Test on import
if __name__ == "__main__":
    test_connection()