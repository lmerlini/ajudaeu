from pymongo import mongo_client, ASCENDING
from src.config import settings

client = mongo_client.MongoClient(settings.DATABASE_URL)

db = client[settings.MONGO_INITDB_DATABASE]
