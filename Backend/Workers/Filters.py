from Backend.Client.sqlite3_client import SQLiteClient
from Backend.Workers.exacuter import Users, Employee, Employer, EmployeeResponses, EmployerResponses

database_client = SQLiteClient(dbname='hachatryan', user='hachatryan', password='367878Artem', host='pg2.sweb.ru')


class Filter_Employees:
    def __init__(self):
        self.sal_low = -1
        self.sal_big = -1
        self.education = ""
        self.information = ""
        self.profession = ""
        self.experience = ""
        self.user_id = -1

    def change_sal_low(self, num: int):
        self.sal_low = num

    def change_sal_big(self, num: int):
        self.sal_big = num

    def change_education(self, num: str):
        self.education = num

    def change_information(self, num: str):
        self.information = num

    def change_profession(self, num: str):
        self.profession = num

    def change_experience(self, num: str):
        self.experience = num

    def change_user_id(self, num: int):
        self.user_id = num

    def clear(self):
        self.sal_low = -1
        self.sal_big = -1
        self.education = ""
        self.information = ""
        self.profession = ""
        self.experience = ""
        self.user_id = -1

    def search(self):
        text = ""
        mas = []
        if self.sal_low >= 0:
            text += "salary_lowest >= " + str(self.sal_low) + " "
        if self.sal_big >= 0:
            if text != "":
                text += "AND "
            text += "salary_biggest <= " + str(self.sal_big) + " "
        if self.education != "":
            if text != "":
                text += "AND "
            text += "(education) in (%s) "
            mas.append(self.education)
        if self.information != "":
            if text != "":
                text += "AND "
            text += "(information) in (%s) "
            mas.append(self.information)
        if self.profession != "":
            if text != "":
                text += "AND "
            text += "(profession) in (%s) "
            mas.append(self.profession)
        if self.experience != "":
            if text != "":
                text += "AND "
            text += "(experience) in (%s) "
            mas.append(self.experience)
        if self.user_id > 0:
            if text != "":
                text += "AND "
            text += "user_id in (" + str(self.sal_low) + ") "
        m = tuple(mas)
        cl = Employee(database_client=database_client)
        cl.setup()
        users = cl.select(params_text=text, params=m)
        cl.shutdown()
        return users


class Filter_Employers:
    def __init__(self):
        self.sal_low = -1
        self.sal_big = -1
        self.company_name = ""
        self.company_inf = ""
        self.vacancy = ""
        self.experience = ""
        self.user_id = -1

    def change_sal_low(self, num: int):
        self.sal_low = num

    def change_sal_big(self, num: int):
        self.sal_big = num

    def change_company_name(self, num: str):
        self.company_name = num

    def change_company_inf(self, num: str):
        self.company_inf = num

    def change_vacancy(self, num: str):
        self.vacancy = num

    def change_experience(self, num: str):
        self.experience = num

    def change_user_id(self, num: int):
        self.user_id = num

    def clear(self):
        self.sal_low = -1
        self.sal_big = -1
        self.company_name = ""
        self.company_inf = ""
        self.vacancy = ""
        self.experience = ""
        self.user_id = -1

    def search(self):
        text = ""
        mas = []
        if self.sal_low >= 0:
            text += "salary_lowest >= " + str(self.sal_low) + " "
        if self.sal_big >= 0:
            if text != "":
                text += "AND "
            text += "salary_biggest <= " + str(self.sal_big) + " "
        if self.company_name != "":
            if text != "":
                text += "AND "
            text += "(company_name) in (%s) "
            mas.append(self.company_name)
        if self.company_inf != "":
            if text != "":
                text += "AND "
            text += "(company_inf) in (%s) "
            mas.append(self.company_inf)
        if self.vacancy != "":
            if text != "":
                text += "AND "
            text += "(vacancy) in (%s) "
            mas.append(self.vacancy)
        if self.experience != "":
            if text != "":
                text += "AND "
            text += "(experience) in (%s) "
            mas.append(self.experience)
        if self.user_id > 0:
            if text != "":
                text += "AND "
            text += "user_id in (" + str(self.sal_low) + ") "
        m = tuple(mas)
        cl = Employer(database_client=database_client)
        cl.setup()
        users = cl.select(params_text=text, params=m)
        cl.shutdown()
        return users


# cl = Filter_Employers()
# cl.change_sal_low(num=1)
# cl.change_sal_big(num=1)
# cl.change_company_name(num='a')
# cl.change_vacancy(num='a')
# cl.change_user_id(num=1)
# mas = cl.search()
# print(mas)

