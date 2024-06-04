from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__,static_folder='static')

# Kết nối tới cơ sở dữ liệu MySQL
def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='01072004',
        database='login_system'
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return render_template('index.html', users=users)

@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO users (username, password, email) VALUES (%s, %s, %s)
    ''', (username, password, email))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
