from fastapi import APIRouter, HTTPException
from app.models.task import TaskCreate, TaskResponse
from app.core.database import get_supabase
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/process-voice")
async def process_voice_command(audio_data: dict):
    """Processa comando de voz e retorna resposta"""
    try:
        # TODO: Implementar processamento de áudio
        text = "Comando recebido - implementar STT"
        
        # Lógica simples para demonstração
        if "tarefa" in text.lower() and "adicionar" in text.lower():
            return {
                "response": "Vou adicionar uma tarefa. Qual é o título?",
                "next_step": "get_task_title"
            }
        
        return {"response": "Comando processado: " + text}
    
    except Exception as e:
        logger.error(f"Erro ao processar comando: {e}")
        raise HTTPException(status_code=500, detail="Erro interno")