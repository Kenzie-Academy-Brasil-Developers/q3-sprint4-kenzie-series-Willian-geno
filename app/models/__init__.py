import psycopg2
import os

configs = {
    'host' : os.getenv('DB_HOST'),
    'database' : os.getenv('DB_NAME'),
    'user' : os.getenv('DB_USER'),
    'password' : os.getenv('DB_PASSWORD'),
}

class DatabaseConector:
    @classmethod
    def get_conn_cor(cls):

        cls.conn = psycopg2.connect(**configs)
        cls.cor = cls.conn.cursor()

    @classmethod
    def close_conn_cor(cls):
        cls.conn.close();
        cls.cor.close

    @classmethod
    def create_table(self):
        print(configs)
        self.get_conn_cor()

        query = """
            CREATE TABLE IF NOT EXISTS ka_series (
                id              BIGSERIAL                   PRIMARY KEY,
                serie           VARCHAR(100)    NOT NULL    UNIQUE,
                seasons         INTEGER         NOT NULL,
                released_date   DATE            NOT NULL,
                genre           VARCHAR(50)     NOT NULL,
                imdb_rating     FLOAT           NOT NULL
                )
        """

        self.cor.execute(query)

        self.conn.commit()

        self.close_conn_cor()
