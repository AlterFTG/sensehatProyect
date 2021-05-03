from flask import Flask, Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user

from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile', methods=["GET", "POST"])
@login_required

def profile():
    if request.method == "POST":
        data = request.data
        data = data.decode()
        data = data.split(',')
        data = [w.replace('"',"").replace("[","").replace("]","") for w in data]

        blank = (0, 102, 102)
        black = (204, 0, 204)
        red = 2

        colorDict = {"blank": (0, 102, 102), "black": (0,0,0), "red": (202,202,202)}

        draw = []
        for x in range(len(data)):
            draw.append(colorDict[data[x]])


        print(draw)

    return render_template('profile.html')

@main.route('/weather')
@login_required
def weather():
    humidity = round(sense.get_humidity(), 1)
    pressure = round(sense.get_pressure(), 1)
    return render_template('weather.html', celcius=celcius, fahrenheit=fahrenheit, humidity=humidity, pressure=pressure)
