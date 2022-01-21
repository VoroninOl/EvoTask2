import sqlite3
from flask import Flask, render_template
from flask import redirect, request, url_for, jsonify
import json

app = Flask(__name__)

db = sqlite3.connect('database/server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users(
    name TEXT,
    surname TEXT
)""")

db.commit()

db.close()

@app.route('/')
def index():
    """Route to render main page"""
    return render_template('index.html')


@app.route('/checkUser', methods=['POST'])
def check_user():
    """Route to check add user or inform if user are already in the database"""
    data = json.loads(request.get_data().decode('utf-8'))
    name = data['name']
    surname = data['surname']
    db_route = sqlite3.connect('database/server.db')
    sql_route = db_route.cursor()
    sql_route.execute(f"SELECT * FROM users WHERE name = '{name}' AND surname = '{surname}'")
    if sql_route.fetchone() is None:
        sql_route.execute(f"INSERT INTO users VALUES (?, ?)", (name, surname))
        db_route.commit()
        db_route.close()
        return jsonify({'answer': 'Привіт, {} {}'.format(name, surname)})
    else:
        db_route.close()
        return jsonify({'answer': 'Вже бачилися, {}'.format(name)})



@app.route('/userList', methods=['GET', 'POST'])
def user_list():
    """Route to render users list page"""
    db_route = sqlite3.connect('database/server.db')
    sql_route = db_route.cursor()
    sql_route.execute("SELECT * FROM users")
    users = sql_route.fetchall()
    return render_template('userList.html', users=users)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)

