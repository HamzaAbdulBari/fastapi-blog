from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, status
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
)
from fastapi.exceptions import RequestValidationError
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as starletteHTTPException

from database import Base, engine
from routers import posts, users


@asynccontextmanager
async def lifespan(_app: FastAPI):
    #Startup
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    #shutdown
    await engine.dispose()

app= FastAPI(lifespan=lifespan)
templates = Jinja2Templates(directory="templates")

app.include_router(users.router,prefix="/api/users" , tags=["users"])
app.include_router(posts.router,prefix="/api/posts" , tags=["posts"])


app.mount("/static", StaticFiles(directory="static"),name="static")
app.mount("/media", StaticFiles(directory="media"),name="media")




@app.exception_handler(starletteHTTPException)
async def general_http_exceptin_handler(request: Request, exception: starletteHTTPException):
    message=(
        exception.detail
        if exception.detail
        else "An error occured please check your request and try again"
    )
    if request.url.path.startswith("/api"):
        return await http_exception_handler(request,exception)
        
    return templates.TemplateResponse(
        request,
        "error.html",
        {
            "status_code":exception.status_code,
            "title":exception.status_code,
            "message":message,
        },
        status_code=exception.status_code,
    )
@app.exception_handler(RequestValidationError)
async def validation_exceptin_handler(request: Request, exception: RequestValidationError):
    if request.url.path.startswith("/api"):
        return await request_validation_exception_handler(request,exception)
    return templates.TemplateResponse(
        request,
        "error.html",
        {
            "status_code":status.HTTP_422_UNPROCESSABLE_CONTENT,
            "title":status.HTTP_422_UNPROCESSABLE_CONTENT,
            "message":"Invalid Request",
        },
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
    )    