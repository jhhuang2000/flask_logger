from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from time import sleep
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'deadbeef'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///log_users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(50), default=None)
    user_agent = db.Column(db.String(100), default=None)
    encoding = db.Column(db.String(100), default=None)
    languages = db.Column(db.String(100), default=None)
    mimetypes = db.Column(db.String(100), default=None)
    connection = db.Column(db.String(50), default=None)
    referer = db.Column(db.String(50), default=None)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<users {self.id}>"

@app.route("/")
def index():
    ip = str(request.remote_addr)
    encoding = str(request.accept_encodings)
    languages = str(request.accept_languages)
    mimetypes = str(request.accept_mimetypes)
    user_agent = str(request.headers.get('User-Agent'))
    headers = str(request.headers)
    connection = str(re.findall(r"Connection: .*\n",headers))
    if len(connection) > 10:
        connection = connection[14:-6]
    referer = str(request.headers.get('Referer'))
    try:
        u = Users(ip=ip, user_agent=user_agent, encoding=encoding, languages=languages,\
                   mimetypes=mimetypes, connection=connection, referer=referer)
        db.session.add(u)
        db.session.flush()
        db.session.commit()
    except:
        db.session.rollback()
        print("Ошибка добавления в БД")

    sleep(5)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=False)
