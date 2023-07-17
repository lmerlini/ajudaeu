from bson import ObjectId
from fastapi import HTTPException, status

class NoteValidator:
    
    @staticmethod
    def validate_note_id(note_id):

        if not ObjectId.is_valid(note_id):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f"Invalid id: {note_id}")
        