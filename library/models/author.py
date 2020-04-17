from dataclasses import dataclass


@dataclass
class Author:
    name: str
    id: int = None
