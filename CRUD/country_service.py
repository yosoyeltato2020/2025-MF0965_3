from persistence import CountryRepository

class CountryService:
    def __init__(self):
        self.repo = CountryRepository()

    def list_countries(self):
        return self.repo.fetch_all()

    def add_country(self, country_data):
        self.repo.add(country_data)

    def update_country(self, country_data):
        self.repo.update(country_data)