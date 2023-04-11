from flask import Flask
from Client.sqlite3_client import SQLiteClient
from Workers.exacuter import Users, Employee, Employer, EmployeeResponses, EmployerResponses
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

database_client = SQLiteClient("users_cunem.db")
email = 'a'
phone_number = 'a'
password = 'a'
FIO = 'a'

# cl = Users(database_client=database_client)
# cl.setup()
# # cl.create_user(email=email, phone_number=phone_number, password=password, FIO=FIO)
# mas = cl.get_user(14)
# print(mas[0])
# cl.shutdown()
#
# cl = Employee(database_client=database_client)
# cl.setup()
# # cl.create_user(1, 1, 'a', 'a', 'a', 'a', mas[0][0])
# mas = cl.get_user(3)
# print(mas[0])
#
#
# cl = Employer(database_client=database_client)
# cl.setup()
# # cl.create_user(1, 1, 'a', 'a', 'a', 'a', mas[0][0])
# mas = cl.get_user(1)
# print(mas[0])

# cl = EmployerResponses(database_client=database_client)
# cl.setup()
# cl.create_user('a', 1, 3, 1)
# mas = cl.get_user(1)
# print(mas[0])

#
# if __name__ == "__main__":
#     app.run(debug=True)