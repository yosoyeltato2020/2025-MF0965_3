from persistence import CountryRepository

class CountryService:
    def __init__(self):
        self.repo = CountryRepository()

    def list_countries(self):
        # Aquí podrías filtrar, paginar, formatear datos, etc.
        return self.repo.fetch_all()

    def add_country(self, country_data):
        # country_data: (Code, Name, Population, Capital, CapitalPopulation)
        self.repo.add(country_data)

    def update_country(self, country_data):
        # country_data: (Code, Name, Population, Capital, CapitalPopulation)
        self.repo.update(country_data)