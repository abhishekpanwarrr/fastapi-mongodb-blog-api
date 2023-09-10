from fastapi import APIRouter

router = APIRouter(
    tags=["User Routes"]
)


@router.get("/")
async def get():
    return {"msg": "Hello world"}


