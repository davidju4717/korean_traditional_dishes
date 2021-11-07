from flask import Flask, render_template, json, redirect, jsonify, url_for, flash
from flask import request
import requests

app = Flask(__name__)

# this is the route to the main page
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dish', methods=['POST'])
def dish():
    if request.method == 'POST':
        dish = request.form.get("group1")

        # obtain dish summary with wikipedia scraper
        url = "https://wiki-scraper-331405.uc.r.appspot.com/"+dish+"/summary"
        dish_description = requests.get(url).json()["summary"]

        # obtain dish image url with google image scraper
        # data to be sent to api
        url = "https://mycovidupdatermicroservice.herokuapp.com/imgScraper"
        data = {"imgSize": "LARGE", "fileType": "jpeg", "imgType": "photo", "num": 1, "q": dish}
        dish_image = requests.post(url, json=data).json()["0"]

        return render_template("dish.html", dish=dish, dish_image=dish_image, dish_description=dish_description)
