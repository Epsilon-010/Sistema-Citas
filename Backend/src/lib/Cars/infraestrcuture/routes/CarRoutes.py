from ....Shared.ServicesContainer.CarServiceContainer import CarServiceContainer
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi import status
from ..schemas.CarSchemas import CarBase
from ...application.use_cases.CreateCar import CreateCar
from ...application.use_cases.UpdateCar import UpdateCar
from ...application.use_cases.DeleteCar import DeleteCar
from ...application.use_cases.GetAllCars import GetAllCars
from ...application.use_cases.GetCarById import GetCarById
from ...application.use_cases.GetCarByPlates import GetCarByPlates
from fastapi import Depends

car_routers = APIRouter(prefix='/cars',tags=['cars'])


@car_routers.post('/create',status_code=status.HTTP_201_CREATED)
async def create_car(car:CarBase,use_case:CreateCar = Depends(CarServiceContainer.create_car)):
    try:
        await use_case.run(
            brand=car.Brand,
            model=car.Model,
            color=car.Color,
            plates=car.Plates
        )
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@car_routers.patch('/update/{id}',status_code=status.HTTP_200_OK)
async def update_car(car:CarBase,id:str,use_case:UpdateCar = Depends(CarServiceContainer.update_car)):
    try:
        await use_case.run(
            id = id,
            brand=car.Brand,
            model=car.Model,
            color=car.Color,
            plates=car.Plates
        )
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@car_routers.delete('/delete',status_code=status.HTTP_200_OK)
async def delete_car(id:str,use_case:DeleteCar = Depends(CarServiceContainer.delete_car)):
    try:
        await use_case.run(id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@car_routers.get('/id/{id}',status_code=status.HTTP_200_OK,response_model=CarBase)
async def get_by_id(id:str,use_case:GetCarById = Depends(CarServiceContainer.get_car_by_id)):
    user_domain = await use_case.run(id)
    user = CarBase.from_domain(user_domain)
    return user

@car_routers.get('/',status_code=status.HTTP_200_OK,response_model=list[CarBase])
async def get_all_users(use_case:GetAllCars = Depends(CarServiceContainer.get_all_cars)):
    try:
        users_domain = await use_case.run()
        users = [CarBase.from_domain(user) for user in users_domain]
        return users
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@car_routers.get('/plates',status_code=status.HTTP_200_OK,response_model=CarBase)
async def get_car_by_plates(plates:str,use_case:GetCarByPlates = Depends(CarServiceContainer.get_car_by_plates)):
    try:
        user_domain = await use_case.run(plates)
        user = CarBase.from_domain(user_domain)
        return user
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))




