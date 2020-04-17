from starlette.applications import Starlette
from starlette.routing import Route
from starlette.testclient import TestClient

from library.models import Book, Category, Author


def test_query_book(loop):
    def book_api(request):
        pass

    routes = [
        Route('/book', book_api)
    ]
    app = Starlette(routes=routes, debug=True)
    client = TestClient(app)
    book_id = 1
    book = Book(
        id=book_id,
        title='refactoring',
        subtitle='improving the design of existing code',
        author=[Author(name='martin fowler')],
        category=[Category(title='software engineering')],
        published_year=1999,
        editor='addison wesley',
        description='whatever',
        saved=True
    )
    loop.run_until_complete(book.save())

    query_response = client.get('/books', params={'title': 'refactoring'})

    result = query_response.json()[0]
    assert result == [
        {
            'id': book_id,
            'title': 'refactoring',
            'subtitle': 'improving the design of existing code',
            'author': [{'name': 'martin fowler'}],
            'category': [{'title': 'software engineering'}],
            'published_year': 1999,
            'editor': 'addison wesley',
            'description': 'whatever',
            'saved': True
        }
    ]
