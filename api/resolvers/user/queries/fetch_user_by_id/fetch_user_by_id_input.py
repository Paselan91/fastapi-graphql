# import strawberry


class FetchUserByIdInput:
    def __init__(self, id: int):
        self.validate(id)
        self.id: int = id

    def validate(self, id: int) -> None:
        if id < 0:
            raise ValueError(f"id must be positive int. id:{id}")

    def get_id(self) -> int:
        return self.id
