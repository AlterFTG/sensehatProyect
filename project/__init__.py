from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Se inicia SQLAlchemy para posteriormente poder usar nuestros modelos.
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # Como user_id es la primary key de nuestra tabla user, lo usaremos en la query para el usuario.
        return User.query.get(int(user_id))    

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    # blueprint para las rutas de autenticación de nuestra app.
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint para las partes de la app que no requieran autenticación.
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
