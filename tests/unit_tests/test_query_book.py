from unittest.mock import MagicMock
from pytest import mark

from library.controllers import InsertBookController, QueryBookController
from library.dtos import BookDTO
from library.models import Author, Category, Editor, Book
from library.persistence import PostgresPersistence


@mark.asyncio
async def test_query_book(mocker):

    class AsyncMock(MagicMock):
        async def __call__(self, *args, **kwargs):
            return super(AsyncMock, self).__call__(*args, **kwargs)


    book_id = '1'
    double = mocker.patch.object(PostgresPersistence, 'filter', new_callable=AsyncMock)
    author = Author(name='martin fowler')
    category = Category(title='software engineering')
    book = Book(
        id=1,
        external_id=book_id,
        title='refactoring',
        subtitle='improving the design of existing code',
        authors=[author],
        categories=[category],
        published_year=1999,
        editor=Editor(name='addison wesley'),
        description='whatever',
        saved=True
    )

    double.return_value = [book]


    book_DTO = BookDTO(
        external_id=book_id,
        title='refactoring',
        subtitle='improving the design of existing code',
        authors=[{'name': 'martin fowler'}],
        categories=[{'title': 'software engineering'}],
        published_year=1999,
        editor={'name': 'addison wesley'},
        description='whatever',
    )
    insert_controller = InsertBookController(data=book_DTO)
    await insert_controller.insert()
    controller = QueryBookController()

    books = await controller.filter(external_id=book_id)

    book = books[0]
    double.assert_called_once_with(external_id=book_id)
    assert book.id
    assert book.external_id == book_id
    assert book.title == 'refactoring'
    assert book.subtitle == 'improving the design of existing code'
    assert book.authors[0].name == 'martin fowler'
    assert book.categories[0].title == 'software engineering'
    assert book.published_year == 1999
    assert book.editor.name == 'addison wesley'
    assert book.description == 'whatever'
    assert book.saved is True
