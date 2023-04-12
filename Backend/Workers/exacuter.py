from Backend.Client.sqlite3_client import SQLiteClient


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

    def create_user(self, user_id: int, email: str, phone_number: str, password: str, FIO: str):
        ADD = """
           INSERT INTO users(user_id, email, phone_number, password, fio) VALUES(%s, %s, %s, %s, %s);
            """
        self.database_client.Exacute_Command(ADD, (user_id, email, phone_number, password, FIO))

    def get_user(self, user_id: int):
        GET_USER = """
            SELECT user_id, email, phone_number, password, fio FROM users WHERE user_id = %s;
            """
        user = self.database_client.Exacute_Select_Command(GET_USER % user_id)
        return user if user else user

    def select(self, params_text: str, params: tuple):
        GET_USERS = """
                    SELECT * FROM users
                    """
        if params_text != None and params_text != "":
            GET_USERS += " WHERE " + params_text
        user = self.database_client.Exacute_Select_Command_With_params(GET_USERS, params)
        return user if user else user


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

    def create_user(self, employee_id: int, sal_low: int, sal_big: int, education: str, information: str, profession: str, experience: str, user_id: int):
        ADD = """
            INSERT INTO employees(employee_id, salary_lowest, salary_biggest, education, information, profession, experience, user_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
            """
        self.database_client.Exacute_Command(ADD, (employee_id, sal_low, sal_big, education, information, profession, experience, user_id))

    def get_user(self, employee_id: int):
        GET_USER = """
            SELECT * FROM employees WHERE employee_id = %s;
            """
        user = self.database_client.Exacute_Select_Command(GET_USER % employee_id)
        return user if user else user

    def select(self, params_text: str, params: tuple):
        GET_USERS = """
                    SELECT * FROM employees
                    """
        if params_text != None and params_text != "":
            GET_USERS += " WHERE " + params_text
        user = self.database_client.Exacute_Select_Command_With_params(GET_USERS, params)
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

    def create_user(self, employer_id: int, sal_low: int, sal_big: int, company_name: str, company_inf: str, vacancy: str, experience: str, user_id: int):
        ADD = """
            INSERT INTO employers(employer_id, salary_lowest, salary_biggest, company_name, company_inf, vacancy, experience, user_id) VALUES(%s, %s, %s, %s, %s, %s, %s, %s);
            """
        self.database_client.Exacute_Command(ADD, (employer_id, sal_low, sal_big, company_name, company_inf, vacancy, experience, user_id))

    def get_user(self, employer_id: int):
        GET_USER = """
            SELECT * FROM employers WHERE employer_id = %s;
            """
        user = self.database_client.Exacute_Select_Command(GET_USER % employer_id)
        return user if user else user

    def select(self, params_text: str, params: tuple):
        GET_USERS = """
                    SELECT * FROM employers
                    """
        if params_text != None and params_text != "":
            GET_USERS += " WHERE " + params_text
        user = self.database_client.Exacute_Select_Command_With_params(GET_USERS, params)
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

    def create_user(self, response_id: int, response: str, mark: int, employee_id: int, employer_id: int):
        ADD = """
            INSERT INTO employer_responses(response_id, response, mark, employee_id, employer_id) VALUES(%s, %s, %s, %s, %s);
            """
        self.database_client.Exacute_Command(ADD, (response_id, response, mark, employee_id, employer_id))

    def get_user(self, response_id: int):
        GET_USER = """
            SELECT * FROM employer_responses WHERE response_id = %s;
            """
        user = self.database_client.Exacute_Select_Command(GET_USER % response_id)
        return user if user else user

    def select(self, params_text: str, params: tuple):
        GET_USERS = """
                    SELECT * FROM employer_responses
                    """
        if params_text != None and params_text != "":
            GET_USERS += " WHERE " + params_text
        user = self.database_client.Exacute_Select_Command_With_params(GET_USERS, params)
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

    def create_user(self, response_id: int, response: str, mark: int, employee_id: int, employer_id: int):
        ADD = """
            INSERT INTO employee_responses(response_id, response, mark, employee_id, employer_id) VALUES(%s, %s, %s, %s, %s);
            """
        self.database_client.Exacute_Command(ADD, (response_id, response, mark, employee_id, employer_id))

    def get_user(self, response_id: int):
        GET_USER = """
            SELECT * FROM employee_responses WHERE response_id = %s;
            """
        user = self.database_client.Exacute_Select_Command(GET_USER % response_id)
        return user if user else user

    def select(self, params_text: str, params: tuple):
        GET_USERS = """
                    SELECT * FROM employee_responses
                    """
        if params_text != None and params_text != "":
            GET_USERS += " WHERE " + params_text
        user = self.database_client.Exacute_Select_Command_With_params(GET_USERS, params)
        return user if user else user


# cl = SQLiteClient(dbname='hachatryan', user='hachatryan', password='367878Artem', host='pg2.sweb.ru')
# u = Employee(database_client=cl)
# u.setup()
# mas = u.select(params_text="(education) in (%s) and (experience) in (%s)", params=(('a'), ('a')))
# print(mas)
# u.shutdown()
