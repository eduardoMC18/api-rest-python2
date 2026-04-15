from fastapi import FastAPI
from reelsRouter import reels_router

app = FastAPI()


app.include_router(reels_router)
# para rodar: python -m uvicorn main:app --reload