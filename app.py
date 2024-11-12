from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Task
from forms import RegisterForm, LoginForm, TaskForm

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace 'your_secret_key' with a secure key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

# Initialize SQLAlchemy and LoginManager
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# User loader for LoginManager
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Registration Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # Update the hash method to 'pbkdf2:sha256'
        hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
        new_user = User(username=form.username.data, password=hashed_password)
        
        # Add the user to the database
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! You can now log in.')
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Find the user by username
        user = User.query.filter_by(username=form.username.data).first()
        
        # Check if the user exists and if the password matches
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Login unsuccessful. Please check your username and password.')
    
    return render_template('login.html', form=form)

# Logout Route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('login'))

# Index Route (Main Page)
@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = TaskForm()
    
    # If the form is submitted, add the task to the database
    if form.validate_on_submit():
        new_task = Task(title=form.title.data, user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('index'))
    
    # Fetch tasks for the current user
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    
    return render_template('index.html', tasks=tasks, form=form)

# Delete Task Route
@app.route('/delete_task/<int:task_id>')
@login_required
def delete_task(task_id):
    # Find the task by ID and ensure it belongs to the current user
    task = Task.query.get(task_id)
    if task and task.user_id == current_user.id:
        db.session.delete(task)
        db.session.commit()
        flash('Task deleted successfully.')
    else:
        flash('Task not found or unauthorized.')
    
    return redirect(url_for('index'))

# Run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables if they don't exist
    app.run(debug=True)
