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

    def add(self, country_data):
        code, name, population, capital_name, capital_population = country_data
        conn = get_connection()
        cursor = conn.cursor()
        # Insertar o buscar la ciudad capital
        cursor.execute("SELECT ID FROM city WHERE Name = %s AND Population = %s LIMIT 1", (capital_name, capital_population))
        city = cursor.fetchone()
        if city:
            capital_id = city[0]
        else:
            cursor.execute("INSERT INTO city (Name, Population, CountryCode) VALUES (%s, %s, %s)", (capital_name, capital_population, code))
            capital_id = cursor.lastrowid
        # Insertar el país
        cursor.execute(
            "INSERT INTO country (Code, Name, Population, Capital) VALUES (%s, %s, %s, %s)",
            (code, name, population, capital_id)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def update(self, country_data):
        code, name, population, capital_name, capital_population = country_data
        conn = get_connection()
        cursor = conn.cursor()
        # Insertar o buscar la ciudad capital
        cursor.execute("SELECT ID FROM city WHERE Name = %s AND Population = %s LIMIT 1", (capital_name, capital_population))
        city = cursor.fetchone()
        if city:
            capital_id = city[0]
        else:
            cursor.execute("INSERT INTO city (Name, Population, CountryCode) VALUES (%s, %s, %s)", (capital_name, capital_population, code))
            capital_id = cursor.lastrowid
        # Actualizar el país
        cursor.execute(
            "UPDATE country SET Name=%s, Population=%s, Capital=%s WHERE Code=%s",
            (name, population, capital_id, code)
        )
        conn.commit()
        cursor.close()
        conn.close()