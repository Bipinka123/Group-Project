"import json"
import math
import os
import requests
import geocoder
from dotenv import load_dotenv, find_dotenv
import flask

app = flask.Flask(__name__)
app.secret_key = "Hithisisbipin"
load_dotenv(find_dotenv())

g = geocoder.ip("me")
latitude = g.lat
longitude = g.lng

NYT_BOOK_BEST_SELLER_API_BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
response = requests.get(
    NYT_BOOK_BEST_SELLER_API_BASE_URL,
    params={
        "lat": f"{latitude}",
        "lon": f"{longitude}",
        "units": "metric",
        "appid": os.getenv("WEATHER_API_KEY"),
    },
    timeout=10,
)

json_data = response.json()

temp_list = json_data["main"]
CURRENT_TEMP = str(math.ceil(temp_list["temp"])) + "˚ C"
MAX_TEMP = str(math.ceil(temp_list["temp_max"])) + "˚ C"
MIN_TEMP = str(math.ceil(temp_list["temp_min"])) + "˚ C"
FEELS_LIKE = str(math.ceil(temp_list["feels_like"])) + "˚ C"

image_icon_list = json_data["weather"]
WEATHER_IMAGE_BASE_URL = "http://openweathermap.org"
IMAGE_PATH = "/img/wn/"

def image_icon():
    "get image icon"
    for images in image_icon_list:
        return images["icon"] + "@2x"

image = image_icon()
weather_image_full_url = f"{WEATHER_IMAGE_BASE_URL}{IMAGE_PATH}{image}.png"
location = json_data["name"]

def weather_description():
    "get weather description"
    for images in image_icon_list:
        return images["description"]

description = weather_description()
