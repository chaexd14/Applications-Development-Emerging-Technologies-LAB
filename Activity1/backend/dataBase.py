from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ServerSelectionTimeoutError

URI = "mongodb+srv://kingamato:chaeyoung0@projects.vdqopmy.mongodb.net/?appName=Projects"

client = AsyncIOMotorClient(URI)
database = client["Projects"]
collection = database["Activity1"]

async def check_db_connection():
    try:
        await client.admin.command("ping")
        print("Database connected")
        return True
    except ServerSelectionTimeoutError:
        print("Database connection failed!")
        return False