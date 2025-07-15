from fastapi import APIRouter, HTTPException, Depends, Request, Query
from tortoise.contrib.pydantic import pydantic_model_creator
from models.contenedor import Contenedor
from models.asignacion import Asignacion
from models.usuario import Usuario
from backend.auth import get_current_user
from typing import List

router = APIRouter()

ContenedorIn = pydantic_model_creator(Contenedor, name="ContenedorIn", exclude_readonly=True)
ContenedorOut = pydantic_model_creator(Contenedor, name="ContenedorOut")
AsignacionOut = pydantic_model_creator(Asignacion, name="AsignacionOut")

# Obtener todos los contenedores (admin) o solo los asignados (estudiante)
@router.get("/contenedores", response_model=List[ContenedorOut])
async def get_contenedores(current_user: Usuario = Depends(get_current_user)):
    if current_user.perfil.lower() == 'administrador':
        return await ContenedorOut.from_queryset(Contenedor.all())
    else:
        asignaciones = await Asignacion.filter(usuario=current_user.id).values_list('contenedor_id', flat=True)
        return await ContenedorOut.from_queryset(Contenedor.filter(id__in=asignaciones))

# Obtener un contenedor por id
@router.get("/contenedores/{contenedor_id}", response_model=ContenedorOut)
async def get_contenedor(contenedor_id: int, current_user: Usuario = Depends(get_current_user)):
    contenedor = await Contenedor.get_or_none(id=contenedor_id)
    if not contenedor:
        raise HTTPException(status_code=404, detail="Contenedor no encontrado")
    if current_user.perfil.lower() != 'administrador':
        asignado = await Asignacion.get_or_none(usuario=current_user.id, contenedor=contenedor_id)
        if not asignado:
            raise HTTPException(status_code=403, detail="No tienes acceso a este contenedor")
    return await ContenedorOut.from_tortoise_orm(contenedor)

# Crear un contenedor (solo admin)
@router.post("/contenedores", response_model=ContenedorOut)
async def create_contenedor(data: ContenedorIn, current_user: Usuario = Depends(get_current_user)):
    if current_user.perfil.lower() != 'administrador':
        raise HTTPException(status_code=403, detail="Solo administradores pueden crear contenedores")
    contenedor = await Contenedor.create(**data.dict())
    return await ContenedorOut.from_tortoise_orm(contenedor)

# Actualizar un contenedor (solo admin)
@router.put("/contenedores/{contenedor_id}", response_model=ContenedorOut)
async def update_contenedor(contenedor_id: int, data: ContenedorIn, current_user: Usuario = Depends(get_current_user)):
    if current_user.perfil.lower() != 'administrador':
        raise HTTPException(status_code=403, detail="Solo administradores pueden actualizar contenedores")
    contenedor = await Contenedor.get_or_none(id=contenedor_id)
    if not contenedor:
        raise HTTPException(status_code=404, detail="Contenedor no encontrado")
    await contenedor.update_from_dict(data.dict()).save()
    return await ContenedorOut.from_tortoise_orm(contenedor)

# Eliminar un contenedor (solo admin)
@router.delete("/contenedores/{contenedor_id}")
async def delete_contenedor(contenedor_id: int, current_user: Usuario = Depends(get_current_user)):
    if current_user.perfil.lower() != 'administrador':
        raise HTTPException(status_code=403, detail="Solo administradores pueden eliminar contenedores")
    contenedor = await Contenedor.get_or_none(id=contenedor_id)
    if not contenedor:
        raise HTTPException(status_code=404, detail="Contenedor no encontrado")
    await contenedor.delete()
    return {"detail": "Contenedor eliminado"}

# Crear una asignación (solo admin)
@router.post("/asignaciones", response_model=AsignacionOut)
async def create_asignacion(usuario_id: int, contenedor_id: int, current_user: Usuario = Depends(get_current_user)):
    if current_user.perfil.lower() != 'administrador':
        raise HTTPException(status_code=403, detail="Solo administradores pueden asignar contenedores")
    existe = await Asignacion.get_or_none(usuario_id=usuario_id, contenedor_id=contenedor_id)
    if existe:
        raise HTTPException(status_code=400, detail="La asignación ya existe")
    asignacion = await Asignacion.create(usuario_id=usuario_id, contenedor_id=contenedor_id)
    return await AsignacionOut.from_tortoise_orm(asignacion)

# Eliminar una asignación (solo admin)
@router.delete("/asignaciones/{asignacion_id}")
async def delete_asignacion(asignacion_id: int, current_user: Usuario = Depends(get_current_user)):
    if current_user.perfil.lower() != 'administrador':
        raise HTTPException(status_code=403, detail="Solo administradores pueden eliminar asignaciones")
    asignacion = await Asignacion.get_or_none(id=asignacion_id)
    if not asignacion:
        raise HTTPException(status_code=404, detail="Asignación no encontrada")
    await asignacion.delete()
    return {"detail": "Asignación eliminada"}

# Consultar asignaciones por usuario
@router.get("/asignaciones", response_model=List[AsignacionOut])
async def get_asignaciones(usuario_id: int = Query(...), current_user: Usuario = Depends(get_current_user)):
    if current_user.perfil.lower() != 'administrador' and current_user.id != usuario_id:
        raise HTTPException(status_code=403, detail="No tienes permiso para consultar asignaciones de otros usuarios")
    asignaciones = await AsignacionOut.from_queryset(Asignacion.filter(usuario_id=usuario_id))
    return asignaciones 