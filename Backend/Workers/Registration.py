from Backend.Client.sqlite3_client import SQLiteClient
from Backend.Workers.exacuter import Users, Employee, Employer

database_client = SQLiteClient("pg2.sweb.ru/hachatryan")

class Registration:
    def __init__(self, password: str, FIO: str, email = "", phone_number=""):
        self.email = email
        self.FIO = FIO
        self.password = password
        self.phone_number = phone_number

    def check(self):
        if self.email == "" and self.phone_number == "":
            return False

        elif self.password == None:
            return False

        return True

    def add_user(self):
        u = Users(database_client=database_client)
        u.setup()
        u.create_user(email=self.email, phone_number=self.phone_number, password=self.password, FIO=self.FIO)
