from dataclasses import dataclass
from typing import List, Dict


@dataclass
class BookDTO:
    external_id: str
    title: str
    subtitle: str
    authors: List[Dict[str, str]]
    categories: List[Dict[str, str]]
    published_year: int
    editor: Dict[str, str]
    description: str
