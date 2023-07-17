from datetime import datetime
from typing import List
from pydantic import BaseModel
from bson.objectid import ObjectId


class NoteBaseSchema(BaseModel):
    id: str | None = None
    title: str = "Morgan"
    content: str = "book"
    category: str = "book"
    published: bool = False
    createdAt: datetime | None = None
    updatedAt: datetime | None = None

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True


class UpdateNoteSchema(BaseModel):
    title: str | None = None
    content: str | None = None
    category: str | None = None
    published: bool | None = None

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True


class NoteResponse(BaseModel):
    status: str
    note: NoteBaseSchema


class ListNoteResponse(BaseModel):
    status: str
    results: int
    notes: List[NoteBaseSchema]
