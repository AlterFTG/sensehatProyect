from flask import Flask, Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
import time

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

        colorDict = {"maroon": (128,0,0), "brown": (165,42,42), "sienna": (160,82,45), "chocolate": (210,105,30), "crimson": (220,20,60), "red": (255,0,0), "salmon": (250,128,114), "darkorange": (255,140,0), "orange": (255,165,0),
        "yellow": (255,255,0), "khaki": (240,230,140),"olive": (128,128,0), "purple": (128,0,128), "fuchsia": (255,0,255), "hotpink": (255,105,180), "pink": (255,192,203), 
        "white": (255,255,255), "greenyellow": (173,255,47), "green": (0, 128, 0), "navy": (0,0,128), 
        "blue": (0,0,255), "aqua": (0,255,255), "teal": (0,128,128), "silver": (192,192,192), "blank": (0,0,0)}

        draw = []
        for x in range(len(data)):
            draw.append(colorDict[data[x]])  

        print(draw)

    return render_template('profile.html')

@main.route('/weather')
@login_required
def weather():
    sense = SenseHat();
    sense.clear()
    humidity = round(sense.get_humidity(), 1)
    pressure = round(sense.get_pressure(), 1)
    temperature = sense.get_temperature()
    celcius = round(temperature, 1)
    fahrenheit = 1.8 * round(temperature, 1) + 32
    temperature = 32

    if temperature < 20:
        tempColor = "is-info"
    elif temperature < 30:
        tempColor = "is-warning" 
    else:
        tempColor = "is-danger"

    return render_template('weather.html', celcius=celcius, fahrenheit=fahrenheit, humidity=humidity, pressure=pressure, tempColor = tempColor)

@main.route('/message', methods=["GET", "POST"])
@login_required
def message():
    if request.method == "POST":  
        text = request.form.get("text")
        slide = request.form.get("slide")

        print(slide)

        if slide != None:
            print("sí")
            for i in range(len(text)):
                print("dentro dle for")
                sense.show_letter(text[i])
                time.sleep(1)
        elif len(text) > 1:
            sense.show_message(text)
            print(text)
        else:
            sense.show_letter(text) 

    return render_template('message.html')