from fastapi import APIRouter

reels_router = APIRouter(prefix="/reels", tags=['reels'])

@reels_router.get("/")
async def home():
    return {"msg": "esta funcionando"}