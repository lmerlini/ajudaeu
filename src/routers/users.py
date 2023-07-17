from fastapi import APIRouter, status, HTTPException, Response
from src.models.users import (
    UpdateUserSchema,
    UserBaseSchema,
    UserResponse,
    ListUserResponse,
)
from src.services.users import UserService

# no validator acho que da pra algo generico, nao troquei pra analisar
from src.validators.notes import NoteValidator
from src.validators.users import UserValidator

router = APIRouter()
service = UserService()


@router.get("/", response_model=ListUserResponse)
def list(limit: int = 10, page: int = 1, search: str = ""):
    count, users = service.list(page, limit, search)
    return {"status": "success", "results": count, "users": users}


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def create(payload: UserBaseSchema):
    try:
        new_user = service.create(payload)
        return {"status": "success", "user": new_user}
    except:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"User with: {payload} already exists",
        )


@router.patch("/{user_id}", response_model=UserResponse)
def update(user_id: str, payload: UpdateUserSchema):
    UserValidator.validate_user_id(user_id)
    updated_user = service.update(user_id, payload)

    if not updated_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No user with this id: {user_id} found",
        )

    return {"status": "success", "user": updated_user}


@router.get("/{user_id}", response_model=UserResponse)
def get(user_id: str):
    UserValidator.validate_user_id(user_id)
    user = service.get(user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No user with this id: {user_id} found",
        )
    return {"status": "success", "user": user}


@router.delete("/{user_id}")
def delete(user_id: str):
    NoteValidator.validate_user_id(user_id)
    user = service.delete(user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No user with this id: {user_id} found",
        )
    return Response(status_code=status.HTTP_204_NO_CONTENT)
