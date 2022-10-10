import re
from dataclasses import dataclass
from typing import ClassVar


@dataclass(init=False, eq=True, frozen=True)
class Email:
    value: str
    MIN_LENGTH: ClassVar[int] = 1
    MAX_LENGTH: ClassVar[int] = 255

    REGEX: ClassVar[str] = "r^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$"
    pattern: ClassVar[str] = re.compile(REGEX)

    def __init__(self, value: str):
        length = len(value)
        if length < self.MIN_LENGTH:
            raise ValueError(f"must be less than {self.MIN_LENGTH}.")
        if length > self.MAX_LENGTH:
            raise ValueError(f"must be more than {self.MAX_LENGTH}.")
        if self.pattern.match(value) is None:
            raise ValueError("must be an email format.")
        object.__setattr__(self, "value", value)

    def min(self) -> int:
        return self.MIN_LENGTH

    def max(self) -> int:
        return self.MAX_LENGTH
