from src.database import db
from pymongo.collection import ReturnDocument


class UserRepository:
    def __init__(self) -> None:
        self.users = db["users"]
        self.users.create_index("username", unique=True)

    def list(self, limit, search, skip):
        pipeline = [
            {"$match": {"username": {"$regex": search, "$options": "i"}}},
            {"$skip": skip},
            {"$limit": limit},
        ]
        return self.users.aggregate(pipeline)

    def create(self, user):
        result = self.users.insert_one(user)
        return self.get(result.inserted_id)

    def update(self, id, user):
        return self.users.find_one_and_update(
            {"_id": id}, {"$set": user}, return_document=ReturnDocument.AFTER
        )

    def delete(self, id):
        return self.users.find_one_and_delete({"_id": id})

    def get(self, id):
        return self.users.find_one({"_id": id})
