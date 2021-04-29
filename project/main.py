from flask import Flask, Blueprint, render_template, request
from flask_login import login_required, current_user

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
        sense.clear()
        sense.show_message(text)
    return render_template('profile.html', name=current_user.name, )

@main.route('/weather')
@login_required
def weather():
    humidity = round(sense.get_humidity(), 1)
    pressure = round(sense.get_pressure(), 1)
    return render_template('weather.html', celcius=celcius, fahrenheit=fahrenheit, humidity=humidity, pressure=pressure)

@main.route('/message', methods=["GET", "POST"])
@login_required

def message():
    text = request.form.get("text")
    print(text)
    if text:
        sense = SenseHat()
        sense.clear()
        sense.show_message(text)
    return render_template('message.html')