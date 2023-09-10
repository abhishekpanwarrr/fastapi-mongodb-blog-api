from fastapi import APIRouter, HTTPException, status
from fastapi.encoders import jsonable_encoder
from ..schemas import User


router = APIRouter(
    tags=["User Routes"]
)


@router.post("/registration", response_description="Register a user")
async def registration(user_info: User):
    user_info = jsonable_encoder(user_info)
#     Duplicate user
    username_found = await db["users"].find_one({"name": user_info["name"]})
    email_found = await db["users"].find_one({"email": user_info["email"]})
    if username_found:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)


