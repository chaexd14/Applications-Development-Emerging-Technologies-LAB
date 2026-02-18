# main.py
from fastapi import FastAPI, HTTPException
from dataBase import collection, check_db_connection
from pydantic import BaseModel
from typing import List
from faker import Faker

app = FastAPI()
fake = Faker()

class User(BaseModel):
    name: str
    age: int
def document_to_dict(doc):
    return {
        "id": str(doc["_id"]),
        "name": doc["name"],
        "age": doc["age"]
    }

@app.on_event("startup")
async def startup_event():
    connected = await check_db_connection()
    if not connected:
        raise Exception("Cannot connect to MongoDB!")

@app.post("/users/", response_model=User)
async def create_user(user: User):
    user_dict = user.dict()
    result = await collection.insert_one(user_dict)
    new_user = await collection.find_one({"_id": result.inserted_id})
    return document_to_dict(new_user)

@app.get("/users/", response_model=List[User])
async def get_users():
    users = []
    async for doc in collection.find():
        users.append(document_to_dict(doc))
    return users

@app.post("/dummy-users/")
async def generate_dummy_users():
    dummy_users = [{"name": fake.name(), "age": fake.random_int(min=18, max=80)} for _ in range(100)]
    try:
        result = await collection.insert_many(dummy_users)
        return {"message": f" Successfully inserted {len(result.inserted_ids)} dummy users."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database insertion failed: {str(e)}")
