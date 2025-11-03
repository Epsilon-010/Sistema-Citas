from fastapi import APIRouter,status,Depends
from ....Shared.ServicesContainer.UserServicesContainer import UserServiceContainer
from fastapi.exceptions import HTTPException
from ..schemas.UserSchemas import UserDetailResponse,UserFoundResponse,UserCreateRequest,UserUpdateRequest
from typing import List
from ...application.UseCases.UserCreate import UserCreate
from ...application.UseCases.UserDelete import UserDelete
from ...application.UseCases.UserGetByApellidoMaterno import UserGetByApellidoMaterno
from ...application.UseCases.UserGetByApellidoPaterno import UserGetByApellidoPaterno
from ...application.UseCases.UserGetById import UserGetById
from ...application.UseCases.UserGetAll import UserGetAll
from ...application.UseCases.UserGetByNumero import UserGetByNumero
from ...application.UseCases.UserUpdate import UserUpdate
from ...application.UseCases.UserGetByName import UserGetByName



user_routes = APIRouter(prefix='/users',tags=['users'])
Services = UserServiceContainer()

@user_routes.get('/',response_model=list[UserFoundResponse],status_code=status.HTTP_200_OK)
async def getUsers(use_case:UserGetAll = Depends(UserServiceContainer.getAllUsers)):
    
    users_domain = await use_case.run()
    if users_domain is None:
        return []
    users = [UserFoundResponse.from_domain(user_domain) for user_domain in users_domain]
    return users


@user_routes.post('/add',status_code=status.HTTP_201_CREATED)
async def createUser(user_data:UserCreateRequest,use_case:UserCreate = Depends(UserServiceContainer.createUser)):
    try:
        await use_case.run(
            nombre=user_data.Nombre,
            apellido_paterno=user_data.Apellido_Paterno,
            apellido_materno=user_data.Apellido_Materno,
            genero=user_data.Genero,
            fecha_nacimiento=user_data.Fecha_Nacimiento,
            ine=user_data.Ine,
            correo=user_data.Correo,
            numero=user_data.Numero
        )
        
        return {"message": "User created successfully"}
        
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=str(e)
        )
        

@user_routes.get('/id/{id}',status_code=status.HTTP_200_OK,response_model=UserDetailResponse)
async def getUserById(id:str,use_case:UserGetById = Depends(UserServiceContainer.getUserById)):
    user_domain = await use_case.run(id)
    if user_domain is None:
        raise HTTPException(status_code=404, detail="User not found")
    user = UserDetailResponse.from_domain(user_domain)
    return user    

@user_routes.get('/name',status_code=status.HTTP_200_OK,response_model=List[UserFoundResponse])
async def getUserByName(name:str,use_case:UserGetByName = Depends(UserServiceContainer.getUserByName)):
    users_domain = await use_case.run(name)
    if users_domain is None:
        raise HTTPException(status_code=404, detail="User not found")
    users = [UserFoundResponse.from_domain(user_domain) for user_domain in users_domain]
    return users


@user_routes.get('/lastnameMom',status_code=status.HTTP_200_OK,response_model=List[UserFoundResponse])
async def getUserByMoLastName(lastname:str,use_case:UserGetByApellidoMaterno = Depends(UserServiceContainer.getUserByApellidoMaterno)):
    users_domain = await use_case.run(lastname)
    if users_domain is None:
        raise HTTPException(status_code=404, detail="User not found")
    users = [UserFoundResponse.from_domain(user_domain) for user_domain in users_domain]
    return users


@user_routes.get('/lastnamePa',status_code=status.HTTP_200_OK,response_model=List[UserFoundResponse])
async def getUserByPaLastName(lastname:str,use_case:UserGetByApellidoPaterno = Depends(UserServiceContainer.getUserByApellidoPaterno)):
    users_domain = await use_case.run(lastname)
    if users_domain is None:
        raise HTTPException(status_code=404, detail="User not found")
    users = [UserFoundResponse.from_domain(user_domain) for user_domain in users_domain]
    return users


@user_routes.get('/number',status_code=status.HTTP_200_OK,response_model=UserFoundResponse)
async def getByNumber(number:str,use_case:UserGetByNumero = Depends(UserServiceContainer.getUserByNumero)):
    user_domain = await use_case.run(number)
    if user_domain is None:
        raise HTTPException(status_code=404, detail="User not found")
    user = UserDetailResponse.from_domain(user_domain)
    return user



@user_routes.delete('/delete',status_code=status.HTTP_200_OK)
async def deleteUser(id:str,use_case:UserDelete = Depends(UserServiceContainer.deleteUser)):
    if await use_case.run(id) is None:
        raise HTTPException(status_code=404,detail='User not found')
    

@user_routes.patch('/update/{id}',status_code=status.HTTP_201_CREATED)
async def updateUser(id:str,user_data:UserUpdateRequest,use_case:UserUpdate = Depends(UserServiceContainer.updateUser)):
    await use_case.run(
        nombre=user_data.Nombre,
        apellido_paterno=user_data.Apellido_Paterno,
        apellido_materno=user_data.Apellido_Materno,
        genero=user_data.Genero,
        fecha_nacimiento=user_data.Fecha_Nacimiento,
        ine=user_data.Ine,
        correo=user_data.Correo,
        numero=user_data.Numero,
        id=id
    )



    

    
