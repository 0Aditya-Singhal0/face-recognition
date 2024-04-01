from fastapi import APIRouter, HTTPException
from .model import User
from .services import add_user_to_collection, get_users, update_user_data, delete_users


userRouter = APIRouter()


@userRouter.post("/create_user/")
async def create_user(user: User):
    return await add_user_to_collection(user)


@userRouter.post("/get_users/")
async def read_user(user_id: str):
    user = await get_users(ids=[user_id])
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")


@userRouter.post("/update_user/")
async def update_user(user_id: str, user: User):
    return await update_user_data(ids=[user_id], user_data=user)


@userRouter.post("/delete_user/")
async def delete_user(user_id: str):
    return await delete_users(ids=[user_id])
