from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import text

app = Flask(__name__)
app.secret_key = "supersecretkey"

# MySQL (XAMPP) config
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/luto'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Recipe model
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)


# Create tables if they don't exist
with app.app_context():
    db.create_all()

# ------------------- ROUTES -------------------

@app.route('/')
def login_page():
    return render_template('login.html')

# Protected home route

@app.route('/home')
def home():
    if 'username' not in session:
        flash("Please log in to access this page.", "error")
        return redirect(url_for('login_page'))

    # Use text() for raw SQL
    result = db.session.execute(text("SELECT name FROM Recipe")).fetchall()
    recipes_list = [r[0] for r in result]

    return render_template('home.html', username=session['username'], recipes=recipes_list)

# Signup route
@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    if User.query.filter_by(username=username).first():
        flash("Username already exists!", "error")
        return redirect(url_for('login_page'))
    if User.query.filter_by(email=email).first():
        flash("Email already registered!", "error")
        return redirect(url_for('login_page'))

    hashed_pw = generate_password_hash(password, method='pbkdf2:sha256')
    new_user = User(username=username, email=email, password=hashed_pw)
    db.session.add(new_user)
    db.session.commit()

    flash("Account created successfully!", "success")
    return redirect(url_for('login_page'))

#login
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        session['username'] = user.username
        flash("Logged in successfully!", "success")
        return redirect(url_for('home'))
    else:
        flash("Invalid username or password", "error")
        return redirect(url_for('login_page'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash("Logged out successfully", "success")
    return redirect(url_for('login_page'))

# ------------------- END ROUTES -------------------

if __name__ == '__main__':
    app.run(debug=True)
