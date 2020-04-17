import asyncpg


class PostgresPersistence:

    async def _get_connection(self):
        conn = await asyncpg.connect(
            user='admin',
            password='postgres',
            database='randori',
            host='10.0.160.85',
            port=5432
        )
        return conn

    async def filter(self, external_id):
        pass

    async def insert_author(self, author):
        conn = await self._get_connection()
        author_id = await conn.fetchval('''
            INSERT INTO author (name) VALUES ($1) RETURNING id
        ''', author.name)
        conn.close()
        author.id = author_id
        return author

    async def insert_category(self, category):
        conn = await self._get_connection()
        category_id = await conn.fetchval('''
            INSERT INTO category (title) VALUES ($1) RETURNING id
        ''', category.title)
        conn.close()
        category.id = category_id
        return category

    async def insert_editor(self, editor):
        conn = await self._get_connection()
        editor_id = await conn.fetchval('''
            INSERT INTO editor (name) VALUES ($1) RETURNING id
        ''', editor.name)
        conn.close()
        editor.id = editor_id
        return editor

    async def insert_book(self, book):
        conn = await self._get_connection()
        book_id = await conn.fetchval('''
            INSERT INTO book (external_id, title, subtitle, published_year, editor_id, description) 
            VALUES ($1, $2, $3, $4, $5, $6) RETURNING id
        ''', book.external_id, book.title, book.subtitle, book.published_year, book.editor.id, book.description)
        book.id = book_id

        for author in book.authors:
            await conn.execute('''
            INSERT INTO author_book (book_id, author_id) VALUES ($1, $2)
            ''', book_id, author.id)

        for category in book.categories:
            await conn.execute('''
            INSERT INTO category_book (book_id, category_id) VALUES ($1, $2)
            ''', book_id, category.id)

        conn.close()
        return book
