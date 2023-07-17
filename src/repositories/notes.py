from src.database import db
from pymongo.collection import ReturnDocument


class NoteRepository:
    def __init__(self) -> None:
        self.notes = db["notes"]
        self.notes.create_index("title", unique=True)

    def list(self, limit, search, skip):
        pipeline = [
            {"$match": {"title": {"$regex": search, "$options": "i"}}},
            {"$skip": skip},
            {"$limit": limit},
        ]
        return self.notes.aggregate(pipeline)

    def create(self, note):
        result = self.notes.insert_one(note)
        return self.get(result.inserted_id)

    def update(self, id, note):
        return self.notes.find_one_and_update(
            {"_id": id}, {"$set": note}, return_document=ReturnDocument.AFTER
        )

    def delete(self, id):
        return self.notes.find_one_and_delete({"_id": id})

    def get(self, id):
        return self.notes.find_one({"_id": id})
