from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse 

import models
from database import engine

from user_controller import user_router_v1
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="User CRUD")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router_v1)
app.mount("/assets", StaticFiles(directory="static/assets"), name="static")

@app.get("/")
async def serveHTML():
    return FileResponse('static/index.html')


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)