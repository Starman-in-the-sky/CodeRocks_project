from Backend.Client.sqlite3_client import SQLiteClient
from Backend.Workers.exacuter import Users, Employee, Employer

database_client = SQLiteClient(dbname='hachatryan', user='hachatryan', password='367878Artem', host='pg2.sweb.ru')

class Inf_about_users:
    def __init__(self, user_id: int):
        self.user_id = user_id


    def find_user(self):
        u = Users(database_client=database_client)
        u.setup()
        mas = u.get_user(user_id= self.user_id)
        u.shutdown()
        return mas

class Inf_about_resume:
    def __init__(self, employee_id: int):
        self.employee_id = employee_id

    def find_resume(self):
        u = Employee(database_client=database_client)
        u.setup()
        mas = u.get_user(employee_id= self.employee_id)
        u.shutdown()
        return mas

class Inf_about_vacancy:
    def __init__(self, employer_id: int):
        self.employer_id = employer_id

    def find_vacancy(self):
        u = Employer(database_client=database_client)
        u.setup()
        mas = u.get_user(employer_id= self.employer_id)
        u.shutdown()
        return mas


