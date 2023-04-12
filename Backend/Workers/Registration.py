from Backend.Client.sqlite3_client import SQLiteClient
from Backend.Workers.exacuter import Users, Employee, Employer

database_client = SQLiteClient(dbname='hachatryan', user='hachatryan', password='367878Artem', host='pg2.sweb.ru')

class Registration_users:
    def __init__(self, user_id: int, email: str, password: str, FIO: str, phone_number=""):
        self.user_id = user_id
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
        u.create_user(user_id= self.user_id, email=self.email, phone_number=self.phone_number, password=self.password, FIO=self.FIO)
        u.shutdown()


class Registration_resume:
    def __init__(self, employee_id: int, sal_low: int, sal_big: int, education: str, information: str, profession: str, experiense: str, user_id):
        self.employee_id = employee_id
        self.sal_low = sal_low
        self.sal_big = sal_big
        self.education = education
        self.information = information
        self.profession = profession
        self.experience = experiense
        self.user_id = user_id

    def add_resume(self):
        u = Employee(database_client=database_client)
        u.setup()
        u.create_user(employee_id= self.employee_id, sal_low=self.sal_low, sal_big=self.sal_big, education=self.education, information=self.information, profession=self.profession, experience=self.experience, user_id=self.user_id)
        u.shutdown()


class Registration_vacancy:
    def __init__(self, employer_id: int, sal_low: int, sal_big: int, company_name: str, company_inf: str, vacancy: str, experiense: str, user_id):
        self.employer_id = employer_id
        self.sal_low = sal_low
        self.sal_big = sal_big
        self.company_name = company_name
        self.company_inf = company_inf
        self.vacancy = vacancy
        self.experience = experiense
        self.user_id = user_id

    def add_vacancy(self):
        u = Employer(database_client=database_client)
        u.setup()
        u.create_user(employer_id= self.employer_id, sal_low=self.sal_low, sal_big=self.sal_big, company_name=self.company_name, company_inf=self.company_inf, vacancy=self.vacancy, experience=self.experience, user_id=self.user_id)
        u.shutdown()

