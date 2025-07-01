from fastapi import APIRouter, HTTPException, Depends, Request
from jose import JWTError, jwt
from passlib.hash import bcrypt
from datetime import datetime, timedelta
from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator
from models.usuario import Usuario
from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter()

class UserCreate(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

UserOut = pydantic_model_creator(Usuario, name="UsuarioOut", exclude=["password"])

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(request: Request):
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=401, detail="Token requerido")

    token = token.replace("Bearer ", "")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Token inválido")
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")

    user = await Usuario.get_or_none(username=username)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

@router.post("/register", response_model=UserOut)
async def register(user: UserCreate):
    if await Usuario.get_or_none(username=user.username):
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    hashed_pw = bcrypt.hash(user.password)
    user_obj = await Usuario.create(username=user.username, password=hashed_pw)
    return await UserOut.from_tortoise_orm(user_obj)

@router.post("/login", response_model=Token)
async def login(user: UserCreate):
    user_obj = await Usuario.get_or_none(username=user.username)
    if not user_obj or not bcrypt.verify(user.password, user_obj.password):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    access_token = create_access_token(data={"sub": user.username},
                                       expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=UserOut)
async def read_users_me(current_user: Usuario = Depends(get_current_user)):
    return await UserOut.from_tortoise_orm(current_user)
