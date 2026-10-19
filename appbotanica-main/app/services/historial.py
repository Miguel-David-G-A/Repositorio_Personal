from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

router = APIRouter(
    prefix="/api/v1/historial",
    tags=["Historial y Recomendaciones"]
)

class HistorialItemResponse(BaseModel):
    id: int
    fecha: datetime
    planta_nombre: str
    enfermedad_detectada: str
    nivel_confianza: float
    tratamiento: str

    class Config:
        from_attributes = True


@router.get("", response_model=List[HistorialItemResponse], summary="Consultar historial general")
def listar_historial(skip: int = 0, limit: int = 10):
    """
    Retorna el historial de todas las fotos y diagnósticos previos del usuario activo.
    """
    return []


@router.get("/{id}", response_model=HistorialItemResponse, summary="Ver detalle de un diagnóstico")
def obtener_detalle_historial(id: int):
    """
    Obtiene el detalle específico de un diagnóstico pasado y su tratamiento recomendado.
    """
    registro_encontrado = None
    
    if not registro_encontrado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El registro de historial especificado no existe."
        )
    
    return registro_encontrado

@router.delete("/{id}", status_status_code=status.HTTP_204_NO_CONTENT, summary="Eliminar registro del historial")
def eliminar_historial(id: int):
    """
    Elimina un registro antiguo del historial personal del usuario.
    """
    registro_existe = True
    
    if not registro_existe:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No se pudo eliminar: el registro no fue encontrado."
        )
        
    return None