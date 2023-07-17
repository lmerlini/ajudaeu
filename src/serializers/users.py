class UserSerializer:
    @classmethod
    def user_entity(cls, user) -> dict:
        return {
            "id": str(user["_id"]),
            "name": user["name"],
            "username": user["username"],
            "password": user["password"],
            "active": user["active"],
            "profile_id": user["profile_id"],
            "company_id": user["company_id"],
            "createdAt": user["createdAt"],
            "updatedAt": user["updatedAt"],
        }

    @classmethod
    def user_list_entity(cls, users) -> list:
        return [cls.user_entity(user) for user in users]
