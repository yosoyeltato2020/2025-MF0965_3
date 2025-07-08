from db import get_connection


class CountryRepository:
    def fetch_all(self):
        query = """
        SELECT Code, Name, Population
          FROM country;
                    
        """
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

    
    # métodos add(id), update(id), etc.
