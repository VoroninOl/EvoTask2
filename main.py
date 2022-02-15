from flask import Flask, render_template
from flask import request, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    """Model for user
    Columns: name, surname"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id


@app.route('/',  methods=['GET', 'POST'])
def index():
    """Route to render main page"""
    return render_template('index.html')


@app.route('/checkUser', methods=['POST'])
def check_user():
    """Route to check add user or inform if user are already in the database"""
    data = json.loads(request.get_data().decode('utf-8'))
    name = data['name']
    surname = data['surname']
    users = User.query.all()
    for user in users:
        if user.name == name and user.surname == surname:
            return jsonify({'answer': 'Вже бачилися, {}'.format(name)})
    user = User(name=name, surname=surname)
    try:
        db.session.add(user)
        db.session.commit()
        return jsonify({'answer': 'Привіт, {} {}'.format(name, surname)})
    except Exception as ex:
        return 'Error in adding ' + str(ex)


@app.route('/userList', methods=['GET', 'POST'])
def user_list():
    """Route to render users list page"""
    users = User.query.all()
    return render_template('userList.html', users=users)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)

