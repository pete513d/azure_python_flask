from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

db_url = 'mysql://elbek:8200AarhusN!@elbek-mysql.mysql.database.azure.com/elbekdb'
app.config ['SQLALCHEMY_DATABASE_URI'] = db_url

db = SQLAlchemy(app)

class people(db.Model):
    personID = db.Column('personID', db.Integer, primary_key = True)
    name = db.Column(db.String(255))

def __init__(self, name):
    self.name = name

@app.route('/')
def index():
    print('Request for index page received')
    return render_template('index.html')

@app.route('/database')
def show_db():
    print('Request for database page received')
    return render_template('database.html', people = people.query.all() )


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
    db.create_all()
    app.run(debug = True)