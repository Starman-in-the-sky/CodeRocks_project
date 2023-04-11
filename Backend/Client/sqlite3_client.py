import sqlite3


class SQLiteClient:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.conn = None

    def Create_con(self):
        self.conn = sqlite3.connect(self.filepath, check_same_thread=False)

    def Close_con(self):
        self.conn.close()

    def Exacute_Command(self, Command: str, params: tuple):
        if self.conn is not None:
            self.conn.execute(Command, params)
            self.conn.commit()
        else:
            raise ConnectionError("You need to create conaction to database!")

    def Exacute_Select_Command(self, Command: str):
        if self.conn is not None:
            cur = self.conn.cursor()
            cur.execute(Command)
            return cur.fetchall()
        else:
            raise ConnectionError("You need to create conaction to database!")
