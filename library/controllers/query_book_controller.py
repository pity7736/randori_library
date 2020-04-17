from library.persistence import PostgresPersistence


class QueryBookController:

    def __init__(self):
        pass

    async def filter(self, external_id):
        persistence = PostgresPersistence()
        return await persistence.filter(external_id=external_id)
