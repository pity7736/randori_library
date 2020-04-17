from library.models import Author, Category, Editor, Book


class QueryBookController:

    def __init__(self):
        pass

    async def filter(self, external_id):
        author = Author(name='martin fowler')
        category = Category(title='software engineering')
        book = Book(
            id=1,
            external_id=external_id,
            title='refactoring',
            subtitle='improving the design of existing code',
            authors=[author],
            categories=[category],
            published_year=1999,
            editor=Editor(name='addison wesley'),
            description='whatever',
            saved=True
        )
        return [book]
