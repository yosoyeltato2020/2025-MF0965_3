from db import get_connection


from db import get_connection

class CountryRepository:
    def fetch_all(self):
        query = """
        SELECT country.Code, country.Name, country.Population,
               city.Name AS Capital, city.Population AS CapitalPopulation
          FROM country
          LEFT JOIN city ON country.Capital = city.ID;
        """
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

    
    # métodos add(id), update(id), etc.
