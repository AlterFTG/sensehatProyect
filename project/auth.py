from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from flask_login import login_user, logout_user, login_required
from .models import User

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() # Si devuelve un usuario es que ya existe en la base de datos.
                                                        

    if user: # Si este usuario existe, hacemos una redirección a la página de sign up para que lo intente otra vez.
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    # Crea un nuevo usuario en base a la información del formulario. Se hashea el password para que no se guarde en un texto plano.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # Agrega un nuevo usuario a la base de datos.
    db.session.add(new_user)
    db.session.commit()    

    return redirect(url_for('auth.login'))

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # Comprueba si el usuario existe
    # Recibe el password introducido por el usuario, lo hashea y lo compara con el otro password hasheado en la base de datos.
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # Si el usuario no existe o si el password es incorrecto, se recarga esta página.

    # Si el check de arriba sabemos que el usuario escribió la contraseña correcta.
    login_user(user, remember=remember)
    return redirect(url_for('main.draw'))

