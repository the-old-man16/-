from flask import Flask,render_template,url_for,request,redirect,session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
app = Flask(__name__,static_url_path='/static')

app.secret_key = 'wongkarwai_key'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER '] = 'root'
app.config['MYSQL_PASSWORD'] = '' 
app.config['MYSQL_DB'] = 'program_login'

mysql = MySQL(app)

@app.route('/')
def home():    
    return render_template("home.html")

@app.route('/admin')
def admin():    
    return render_template("admin.html")

@app.route('/login')
def login():    
    return render_template("login.html")

@app.route('/register')
def register():    
    return render_template("register.html")

@app.route('/menu')
def menu():    
    return render_template("menu.html")

@app.route('/bill')
def bill():
    
    return render_template("bill.html")

@app.route('/order', methods=['GET','POST'])
def order():
    return render_template("order.html")


if __name__ =="__main__":
    app.run(debug=True,use_reloader=True)