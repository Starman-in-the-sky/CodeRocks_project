import psycopg2


class SQLiteClient:
    def __init__(self, dbname: str, user: str, password: str, host: str):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.conn = None
        self.cur = None

    def Create_con(self):
        self.conn = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host)
        self.cur = self.conn.cursor()

    def Close_con(self):
        self.conn.close()

    def Exacute_Command(self, Command: str, params: tuple):
        if self.conn is not None:
            self.cur.execute(Command, params)
            self.conn.commit()
        else:
            raise ConnectionError("You need to create conaction to database!")

    def Exacute_Select_Command(self, Command: str):
        if self.conn is not None:
            self.cur.execute(Command)
            return self.cur.fetchall()
        else:
            raise ConnectionError("You need to create conaction to database!")
