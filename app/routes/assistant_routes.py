from fastapi import APIRouter
'''
FastAPI for organize and resolve modular endpoints
'''


router = APIRouter()
''''
router creation
'''

@router.get("/test")
async def test_endpoint():
    return {"message": "Assistant API is working!"}
'''
definition of /test endpoint with get action. 
return dict message
'''

@router.get("/health")
async def health_check():
    return {"status": "healthy", "service": "Helenna assistent"}
'''
definition of /test endpoint with get action. 
return dict message
'''