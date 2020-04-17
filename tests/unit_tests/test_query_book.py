from unittest.mock import MagicMock
from pytest import mark

from library.controllers import InsertBookController, QueryBookController
from library.dtos import BookDTO


@mark.asyncio
async def test_query_book(mocker):

    class AsyncMock(MagicMock):
        async def __call__(self, *args, **kwargs):
            return super(AsyncMock, self).__call__(*args, **kwargs)

    persistence = PostgresPersistence()
    double = mocker.patch.object(persistence, 'filter', new_callabcle=AsyncMock)
    double.return_value = ''

    book_id = '1'
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
