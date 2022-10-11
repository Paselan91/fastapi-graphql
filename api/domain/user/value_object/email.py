import re
from dataclasses import dataclass
from typing import ClassVar


@dataclass(init=False, eq=True, frozen=True)
class Email:
    value: str
    MIN_LENGTH: ClassVar[int] = 1
    MAX_LENGTH: ClassVar[int] = 255
    REGEX: ClassVar[str] = "[A-Za-z0-9._+]+@[A-Za-z]+.[A-Za-z]"

    def __init__(self, value: str):
        length = len(value)
        if length < self.MIN_LENGTH:
            raise ValueError(f"must be less than {self.MIN_LENGTH}.")
        if length > self.MAX_LENGTH:
            raise ValueError(f"must be more than {self.MAX_LENGTH}.")
        if re.match(self.REGEX, value) is None:
            raise ValueError("must be an email format.")
        object.__setattr__(self, "value", value)

    def min(self) -> int:
        return self.MIN_LENGTH

    def max(self) -> int:
        return self.MAX_LENGTH
