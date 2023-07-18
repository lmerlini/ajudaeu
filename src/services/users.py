from datetime import datetime
from src.serializers.users import UserSerializer
from src.repositories.users import UserRepository
from bson.objectid import ObjectId
from src.helpers.config import generate_hashed_password


class UserService:
    repository: UserRepository

    def __init__(self) -> None:
        self.repository = UserRepository()

    def list(self, page, limit, search):
        skip = (page - 1) * limit
        user = self.repository.list(limit, search, skip)
        users = UserSerializer.user_list_entity(user)
        return len(users), users

    def create(self, user):
        user.createdAt = datetime.utcnow()
        user.updatedAt = user.createdAt
        user.password = generate_hashed_password(user.password)
        user = user.dict(exclude_none=True)
        return UserSerializer.user_entity(self.repository.create(user))

    def update(self, id, user) -> dict:
        id = ObjectId(id)
        user.password = generate_hashed_password(user.password)
        user = user.dict(exclude_none=True)
        result = self.repository.update(id, user)
        return UserSerializer.user_entity(result)

    def delete(self, id):
        id = ObjectId(id)
        return self.repository.delete(id)

    def get(self, id):
        id = ObjectId(id)
        user = self.repository.get(id)
        return UserSerializer.user_entity(user)
