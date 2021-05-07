from flask import Flask, Blueprint, render_template, jsonify, request
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
    if request.method == "POST":
        data = request.data
        data = data.decode()
        data = data.split(',')
        data = [w.replace('"',"").replace("[","").replace("]","") for w in data]

        colorDict = {"maroon": (128,0,0), "crimson": (220,20,60), "red": (255,0,0), "darkorange": (255,140,0), "orange": (255,165,0),
        "yellow": (255,255,0), "khaki": (240,230,140),"olive": (128,128,0), "purple": (128,0,128), "fuchsia": (255,0,255), "hotpink": (255,105,180), "pink": (255,192,203), 
        "white": (255,255,255), "greenyellow": (173,255,47), "green": (0, 128, 0), "navy": (0,0,128), 
        "blue": (0,0,255), "aqua": (0,255,255), "teal": (0,128,128), "blank": (192,192,192)}

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

@main.route('/message')
@login_required
def message():
    text = request.form.get("text")
    if text:
        sense = SenseHat()
        sense.clear()
        sense.show_message(text)
    return render_template('message.html')