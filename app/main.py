from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.routes.assistant import router as assistant_router
import os

app = FastAPI(title="Helena Assistant")

# Criar diretório static se não existir
os.makedirs("static", exist_ok=True)

# Incluir rotas
app.include_router(assistant_router, prefix="/api/v1")

# Servir frontend simples
@app.get("/")
async def serve_frontend():
    return FileResponse('static/index.html')

# Montar arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "Helena Assistant"}