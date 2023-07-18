import bcrypt


def generate_hashed_password(password: str) -> str:
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed_password.decode("utf-8")


def check_password(password: str, db_password: str) -> str:
    return bcrypt.checkpw(password.encode("utf-8"), db_password.encode("utf-8"))
