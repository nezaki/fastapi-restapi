class UserNotFoundError(Exception):
    def __init__(self, user_id: object) -> None:
        super().__init__(f"User not found: {user_id}")


class UserAlreadyExistsError(Exception):
    def __init__(self, email: str) -> None:
        super().__init__(f"User already exists with email: {email}")
