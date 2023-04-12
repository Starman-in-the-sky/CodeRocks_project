from flask import Flask, render_template, request, jsonify
from Client.sqlite3_client import SQLiteClient
from Workers.exacuter import Users, Employee, Employer, EmployeeResponses, EmployerResponses
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_msearch import Search
from flask import request
import psycopg2

app = Flask(__name__)
app.secret_key = "caircocoders-ednalan"

conn = psycopg2.connect(dbname='hachatryan', user='hachatryan', password='367878Artem', host='pg2.sweb.ru')




@app.route('/')
def index():
    return render_template('index.html')


@app.route("/ajaxlivesearch", methods=["POST", "GET"])
def ajaxlivesearch():
    cur = conn.cursor()
    if request.method == 'POST':
        search_word = request.form['query']
        print(search_word)
        if search_word == '':
            query = "SELECT * from employers ORDER BY employer_id"
            cur.execute(query)
            employer = cur.fetchall()
        else:
            cur.execute('SELECT * FROM employers WHERE vacancy LIKE %(vacancy)s', {'vacancy': '%{}%'.format(search_word)})
            numrows = int(cur.rowcount)
            employer = cur.fetchall()
            print(numrows)
    return jsonify({'htmlresponse': render_template('response.html', employer=employer, numrows=numrows)})

if __name__ == "__main__":
     app.run(debug=True)
