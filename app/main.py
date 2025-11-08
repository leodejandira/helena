from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.assistant_routes import router
from app.core.database import test_connection
'''
FastAPI for organize and resolve modular endpoints. Cormiddleware for blocking or free access with frontends os domains
import all routers and conections modules
'''

app = FastAPI(title="Helenna Assistant", version="0.1.0")
'''
instance of fastAPI
'''

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
'''
add middleware cores for all domains, methods and headers
'''

app.include_router(router, prefix="/api/v1")
'''
register of all router, with prefix "api/v1..."
'''

@app.get("/")
def read_root():
    return {"message": "Hellena Assistant API", "status": "running"}
'''
register square endpoint, with dict "
'''

@app.on_event("startup")
async def startup_event():
    test_connection()
'''
event for start aplication. runnign test conection function 
'''


