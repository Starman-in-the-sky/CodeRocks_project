from flask import Flask
from Client.sqlite3_client import SQLiteClient
from Workers.exacuter import Users, Employee, Employer, EmployeeResponses, EmployerResponses
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_msearch import Search

search = Search()

def create_app():
    app = Flask(__name__)
    search.init_app(app)
@post.route('/search')
def search():
    keyword = request.args.get('q')
    search_posts = Post.query.msearch(keyword, fields=['title', 'content'], limit=6)
    return render_template('post/search.html', search_posts=search_posts)

if __name__ == "__main__":
     app.run(debug=True)