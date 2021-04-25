from flask import Flask, Blueprint, render_template, request
from flask_login import login_required, current_user
from sense_hat import SenseHat

from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile', methods=["GET", "POST"])
@login_required

def profile():
    text = request.form.get("text")
    print(text)
    if text:
        sense = SenseHat()
        sense.show_message(text)
    return render_template('profile.html', name=current_user.name, )
