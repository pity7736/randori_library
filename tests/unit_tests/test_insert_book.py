from pytest import mark

from library.controllers import QueryBookController, InsertBookController


@mark.asyncio
async def test_insert_book(book_dto_fixture):
    insert_book_controller = InsertBookController(data=book_dto_fixture)

    await insert_book_controller.insert()

    query_controller = QueryBookController()
    books = await query_controller.filter(external_id=book_dto_fixture.external_id)
    book = books[0]
    assert book.id
    assert book.external_id == book_dto_fixture.external_id
    assert book.title == 'refactoring'
    assert book.subtitle == 'improving the design of existing code'
    assert book.authors[0].name == 'martin fowler'
    assert book.categories[0].title == 'software engineering'
    assert book.published_year == 1999
    assert book.editor.name == 'addison wesley'
    assert book.description == 'whatever'
    assert book.saved is True