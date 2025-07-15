from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from auth import router as auth_router

app = FastAPI()

app.include_router(auth_router)

register_tortoise(
    app,
    db_url="mysql://root:1234@192.168.1.10/ipas",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)