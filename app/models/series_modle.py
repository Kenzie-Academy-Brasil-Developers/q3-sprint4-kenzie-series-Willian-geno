from readline import insert_text
from app.models import DatabaseConector

class Series(DatabaseConector):

    def __init__(self, **kwargs):
        self.serie = kwargs['serie']
        self.seasons = kwargs['seasons']
        self.released_date = kwargs['released_date']
        self.genre = kwargs['genre']
        self.imdb_rating = kwargs['imdb_rating']


    def cretate_serie(self):
        self.create_table()
        self.get_conn_cor()

        query = """
            INSERT INTO ka_series
                (serie, seasons, released_date, genre, imdb_rating)
            VALUES
                (%s, %s, %s, %s, %s)
            RETURNING *
        """

        query_values = tuple(self.__dict__.values())

        self.cor.execute(query, query_values)

        self.conn.commit()

        inserted_series = self.cor.fetchone()

        self.conn.close()
        self.cor.close()

        return inserted_series
        
    @classmethod
    def read_series(cls):
        cls.create_table()
        cls.get_conn_cor()

        query = """SELECT * FROM ka_series """

        cls.cor.execute(query)

        series = cls.cor.fetchall()

        cls.close_conn_cor()

        return series

    @classmethod
    def read_series_by_id(cls, id):

        cls.create_table()
        cls.get_conn_cor()

        serie_id = id

        query = """
            SELECT 
                * 
            FROM 
                ka_series
            WHERE
                id = %s
        """

        cls.cor.execute(query, serie_id)
        cls.conn.commit()

        serie = cls.cor.fetchone()

        cls.close_conn_cor()

        return serie
