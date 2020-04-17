import pytest
from pytest import mark

from library.controllers import InsertBookController, QueryBookController
from library.dtos import BookDTO
from library.models import Author, Category, Editor, Book
from library.persistence import PostgresPersistence
from tests.utils import AsyncMock


@pytest.fixture
def book_fixture():
    author = Author(name='martin fowler')
    category = Category(title='software engineering')
    book = Book(
        id=1,
        external_id='1',
        title='refactoring',
        subtitle='improving the design of existing code',
        authors=[author],
        categories=[category],
        published_year=1999,
        editor=Editor(name='addison wesley'),
        description='whatever',
        saved=True
    )
    return book


@mark.asyncio
async def test_query_book(mocker, book_fixture, book_dto_fixture):
    double = mocker.patch.object(PostgresPersistence, 'filter', new_callable=AsyncMock)
    double.return_value = [book_fixture]

    insert_controller = InsertBookController(data=book_dto_fixture)
    await insert_controller.insert()
    controller = QueryBookController()

    books = await controller.filter(external_id=book_fixture.external_id)

    book = books[0]
    double.assert_called_once_with(external_id=book_fixture.external_id)
    assert book.id
    assert book.external_id == book_fixture.external_id
    assert book.title == 'refactoring'
    assert book.subtitle == 'improving the design of existing code'
    assert book.authors[0].name == 'martin fowler'
    assert book.categories[0].title == 'software engineering'
    assert book.published_year == 1999
    assert book.editor.name == 'addison wesley'
    assert book.description == 'whatever'
    assert book.saved is True
