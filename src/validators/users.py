from bson import ObjectId
from fastapi import HTTPException, status

class UserValidator:
    
    @staticmethod
    def validate_user_id(user_id):

        if not ObjectId.is_valid(user_id):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f"Invalid id: {user_id}")
        