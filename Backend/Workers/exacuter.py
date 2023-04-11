from Backend.Client.sqlite3_client import SQLiteClient

#Регистрация данные
class Users:

    def __init__(self, database_client: SQLiteClient):
        self.database_client = database_client
        self.setted_up = False

    def setup(self):
        self.database_client.Create_con()
        self.setted_up = True

    def shutdown(self):
        self.database_client.Close_con()
        self.setted_up = False

    def create_user(self, email: str, phone_number: str, password: str, FIO: str):
        ADD = """
            INSERT INTO users(email, phone_number, password, FIO) VALUES(?, ?, ?, ?);
            """
        self.database_client.Exacute_Command(ADD, (email, phone_number, password, FIO))

    def get_user(self, user_id: int):
        GET_USER = """
            SELECT user_id, email, phone_number, password FROM users WHERE user_id = %s;
            """
        user = self.database_client.Exacute_Select_Command(GET_USER % user_id)
        return user if user else user
#
class Employee:

    def __init__(self, database_client: SQLiteClient):
        self.database_client = database_client
        self.setted_up = False

    def setup(self):
        self.database_client.Create_con()
        self.setted_up = True

    def shutdown(self):
        self.database_client.Close_con()
        self.setted_up = False

    def create_user(self, sal_low: int, sal_big: int, education: str, information: str, profession: str, experience: str, user_id: int):
        ADD = """
            INSERT INTO employees(salary_lowest, salary_biggest, education, information, profession, experience, user_id) VALUES(?, ?, ?, ?, ?, ?, ?);
            """
        self.database_client.Exacute_Command(ADD, (sal_low, sal_big, education, information, profession, experience, user_id))

    def get_user(self, employee_id: int):
        GET_USER = """
            SELECT * FROM employees WHERE employee_id = %s;
            """
        user = self.database_client.Exacute_Select_Command(GET_USER % employee_id)
        return user if user else user

class Employer:

    def __init__(self, database_client: SQLiteClient):
        self.database_client = database_client
        self.setted_up = False

    def setup(self):
        self.database_client.Create_con()
        self.setted_up = True

    def shutdown(self):
        self.database_client.Close_con()
        self.setted_up = False

    def create_user(self, sal_low: int, sal_big: int, company_name: str, company_inf: str, vacancy: str, experience: str, user_id: int):
        ADD = """
            INSERT INTO employers(salary_lowest, salary_biggest, company_name, company_inf, vacancy, experience, user_id) VALUES(?, ?, ?, ?, ?, ?, ?);
            """
        self.database_client.Exacute_Command(ADD, (sal_low, sal_big, company_name, company_inf, vacancy, experience, user_id))

    def get_user(self, employer_id: int):
        GET_USER = """
            SELECT * FROM employers WHERE employer_id = %s;
            """
        user = self.database_client.Exacute_Select_Command(GET_USER % employer_id)
        return user if user else user

class EmployerResponses:

    def __init__(self, database_client: SQLiteClient):
        self.database_client = database_client
        self.setted_up = False

    def setup(self):
        self.database_client.Create_con()
        self.setted_up = True

    def shutdown(self):
        self.database_client.Close_con()
        self.setted_up = False

    def create_user(self, response: str, mark: int, employee_id: int, employer_id: int):
        ADD = """
            INSERT INTO employer_responses(response, mark, employee_id, employer_id) VALUES(?, ?, ?, ?);
            """
        self.database_client.Exacute_Command(ADD, (response, mark, employee_id, employer_id))

    def get_user(self, response_id: int):
        GET_USER = """
            SELECT * FROM employer_responses WHERE response_id = %s;
            """
        user = self.database_client.Exacute_Select_Command(GET_USER % response_id)
        return user if user else user

class EmployeeResponses:

    def __init__(self, database_client: SQLiteClient):
        self.database_client = database_client
        self.setted_up = False

    def setup(self):
        self.database_client.Create_con()
        self.setted_up = True

    def shutdown(self):
        self.database_client.Close_con()
        self.setted_up = False

    def create_user(self, response: str, mark: int, employee_id: int, employer_id: int):
        ADD = """
            INSERT INTO employee_responses(response, mark, employee_id, employer_id) VALUES(?, ?, ?, ?);
            """
        self.database_client.Exacute_Command(ADD, (response, mark, employee_id, employer_id))

    def get_user(self, response_id: int):
        GET_USER = """
            SELECT * FROM employee_responses WHERE response_id = %s;
            """
        user = self.database_client.Exacute_Select_Command(GET_USER % response_id)
        return user if user else user