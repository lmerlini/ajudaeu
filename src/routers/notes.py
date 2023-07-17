from fastapi import HTTPException, status, APIRouter, Response
from src.models.notes import (
    ListNoteResponse,
    NoteBaseSchema,
    NoteResponse,
    UpdateNoteSchema,
)
from pymongo.errors import DuplicateKeyError
from src.services.notes import NoteService
from src.validators.notes import NoteValidator

router = APIRouter()
service = NoteService()


@router.get("/", response_model=ListNoteResponse)
def list(limit: int = 10, page: int = 1, search: str = ""):
    count, notes = service.list(page, limit, search)
    return {"status": "success", "results": count, "notes": notes}


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=NoteResponse)
def create(payload: NoteBaseSchema):
    try:
        new_note = service.create(payload)
        return {"status": "success", "note": new_note}
    except:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Note with title: {payload.title} already exists",
        )


@router.patch("/{note_id}", response_model=NoteResponse)
def update(note_id: str, payload: UpdateNoteSchema):
    NoteValidator.validate_note_id(note_id)
    updated_note = service.update(note_id, payload)

    if not updated_note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No note with this id: {note_id} found",
        )

    return {"status": "success", "note": updated_note}


@router.get("/{note_id}", response_model=NoteResponse)
def get(note_id: str):
    NoteValidator.validate_note_id(note_id)
    note = service.get(note_id)

    if not note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No note with this id: {note_id} found",
        )
    return {"status": "success", "note": note}


@router.delete("/{note_id}")
def delete(note_id: str):
    NoteValidator.validate_note_id(note_id)
    note = service.delete(note_id)

    if not note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No note with this id: {note_id} found",
        )
    return Response(status_code=status.HTTP_204_NO_CONTENT)
