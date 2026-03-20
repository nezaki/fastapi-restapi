from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass
class User:
    name: str
    email: str
    id: UUID = field(default_factory=uuid4)

    def change_email(self, new_email: str) -> None:
        if "@" not in new_email:
            raise ValueError("Invalid email format")
        self.email = new_email
