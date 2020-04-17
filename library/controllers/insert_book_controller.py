from library.models import Book, Author, Category, Editor
from library.persistence import PostgresPersistence


class InsertBookController:

    def __init__(self, data):
        self._data = data

    async def insert(self):
        persistence = PostgresPersistence()

        authors = []
        for data_author in self._data.authors:
            author = Author(name=data_author.get('name'))
            new_author = await persistence.insert_author(author)
            authors.append(new_author)

        categories = []
        for data_category in self._data.categories:
            category = Category(title=data_category.get('title'))
            new_category = await persistence.insert_category(category)
            categories.append(new_category)

        editor = Editor(name=self._data.editor.get('name'))
        new_editor = await persistence.insert_editor(editor)

        book = Book(
            external_id=self._data.external_id,
            title=self._data.title,
            subtitle=self._data.subtitle,
            authors=authors,
            categories=categories,
            published_year=self._data.published_year,
            editor=new_editor,
            description=self._data.description,
            saved=True
        )
        return await persistence.insert_book(book)
