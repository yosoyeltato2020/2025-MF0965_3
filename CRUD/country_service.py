from persistence import CountryRepository

class CountryService:
    def __init__(self):
        self.repo = CountryRepository()

    def list_countries(self):
        # Aquí podrías filtrar, paginar, formatear datos, etc.
        return self.repo.fetch_all()