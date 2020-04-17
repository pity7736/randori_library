from attr import dataclass


@dataclass
class Editor:
    name: str
    id: int = None