from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi import status,Depends
from ...application.CreateAppoiment import CreateAppoiment
from ...application.UpdateAppoiment import UpdateAppoiment
from ...application.GetAppoiments import GetAppoiments
from ...application.GetAppoimentByVisitante import GetAppoimentByVisitante
from ...application.GetAppoimentByVisitado import GetAppoimentByVisitado
from ...application.GetAppoimentByDate import GetAppoimentByDate
from ...application.GetAppoimentByArea import GetAppoimentByArea
from ....Shared.ServicesContainer.AppoimentServiceContainer import AppoimnetServiceContainer
from ..schemas.AppoimentSchemas import AppointmentSchema,CreateAppoimentSchema,FoundVisitor
from typing import List
from datetime import date

appoiment_routes = APIRouter(prefix='/appoiments',tags=['appoiments'])

@appoiment_routes.get('/',status_code=status.HTTP_200_OK,response_model=List[AppointmentSchema])
async def get_appoiments(use_case:GetAppoiments = Depends(AppoimnetServiceContainer.get_appoiments)):
    try:
        appoiments = await use_case.run()
        return appoiments
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@appoiment_routes.post('/create',status_code=status.HTTP_201_CREATED)
async def create_appoiment(payload:CreateAppoimentSchema,use_case:CreateAppoiment = Depends(AppoimnetServiceContainer.create_appoiment)):
    try:
        await use_case.run(
            fecha=payload.fecha,
            hora=payload.hora,
            visitado=payload.visitado,
            area=payload.area,
            nombre=payload.nombre,
            apellido_paterno=payload.apellido_paterno,
            apellido_materno=payload.apellido_materno,
            plates=payload.plates
        )
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
    


@appoiment_routes.get('/visitor',status_code=status.HTTP_200_OK,response_model=List[AppointmentSchema])
async def get_appoiment_by_visitor(visitor:FoundVisitor,use_case:GetAppoimentByVisitante = Depends(AppoimnetServiceContainer.get_by_visitante)):
    try:
        appoiments = await use_case.run(
            nombre=visitor.nombre,
            apellido_paterno=visitor.apellido_paterno,
            apellido_materno=visitor.apellido_materno
        
        )
        return appoiments
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
    
    
@appoiment_routes.get('/visited',status_code=status.HTTP_200_OK,response_model=List[AppointmentSchema])
async def get_appoiment_by_visied(visited:str,use_case:GetAppoimentByVisitado = Depends(AppoimnetServiceContainer.get_by_visitado)):
    try:
        appoiments = await use_case.run(visited)
        return appoiments
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))


@appoiment_routes.get('/area',status_code=status.HTTP_200_OK,response_model=List[AppointmentSchema])
async def get_appoiment_by_area(area:str,use_case:GetAppoimentByArea = Depends(AppoimnetServiceContainer.get_by_Area)):
    try:
        appoiments = await use_case.run(area)
        return appoiments
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@appoiment_routes.get('/date',status_code=status.HTTP_200_OK,response_model=List[AppointmentSchema])
async def get_appoiment_by_date(fecha:date,use_case:GetAppoimentByDate = Depends(AppoimnetServiceContainer.get_by_date)):
    try:
        appoiments = await use_case.run(fecha)
        return appoiments
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))



