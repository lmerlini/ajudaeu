from datetime import datetime
from src.serializers.notes import NoteSerializer
from src.repositories.notes import NoteRepository
from bson.objectid import ObjectId


class NoteService:
    repository: NoteRepository

    def __init__(self) -> None:
        self.repository = NoteRepository()

    def list(self, page, limit, search):
        skip = (page - 1) * limit
        notes = self.repository.list(limit, search, skip)
        notes = NoteSerializer.note_list_entity(notes)
        return len(notes), notes

    def create(self, book):
        book.createdAt = datetime.utcnow()
        book.updatedAt = book.createdAt
        book = book.dict(exclude_none=True)

        return NoteSerializer.note_entity(self.repository.create(book))

    def update(self, id, book) -> dict:
        id = ObjectId(id)
        book = book.dict(exclude_none=True)
        result = self.repository.update(id, book)
        return NoteSerializer.note_entity(result)

    def delete(self, id):
        id = ObjectId(id)
        return self.repository.delete(id)

    def get(self, id):
        id = ObjectId(id)
        note = self.repository.get(id)
        return NoteSerializer.note_entity(note)
