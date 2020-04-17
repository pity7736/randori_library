from typing import List

from attr import dataclass

from .author import Author
from .category import Category
from .editor import Editor


@dataclass
class Book:
    external_id: str
    title: str
    subtitle: str
    authors: List[Author]
    categories: List[Category]
    published_year: int
    editor: Editor
    description: str
    saved: bool
    id: int = None
