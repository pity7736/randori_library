from attr import dataclass


@dataclass
class Category:
    title: str
    id: int = None
