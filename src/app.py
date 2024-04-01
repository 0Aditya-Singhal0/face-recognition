from fastapi import FastAPI
import uvicorn
from user.router import userRouter

app = FastAPI()

app.include_router(userRouter)


@app.get("/")
async def root():
    return {"message": "Hello to face recognition"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
