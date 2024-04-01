from fastapi import FastAPI
import uvicorn
from user.database import client, create_collection
from user.router import userRouter

list_of_collections = ["Users"]
app = FastAPI()

app.include_router(userRouter)


@app.on_event("startup")
async def startup_event():
    print("Initializing DB...")
    print(f"Collections in DB -> \t{client.list_collections()}")
    collections_not_in_DB = [
        item
        for item in client.list_collections()
        if item.name not in list_of_collections
    ]
    if not collections_not_in_DB == []:
        print(f"{collections_not_in_DB} not in DB")
        for names in collections_not_in_DB:
            print(f"Creating collection {names}")
            create_collection(names)
    pass


@app.get("/")
async def root():
    return {"message": "Hello to face recognition"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
