import pytest

from library.dtos import BookDTO


@pytest.fixture
def book_dto_fixture():
    return BookDTO(
        external_id='1',
        title='refactoring',
        subtitle='improving the design of existing code',
        authors=[{'name': 'martin fowler'}],
        categories=[{'title': 'software engineering'}],
        published_year=1999,
        editor={'name': 'addison wesley'},
        description='whatever',
    )