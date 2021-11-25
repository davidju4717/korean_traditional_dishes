from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# route to the main page
@app.route('/')
def index():
    return render_template("index.html")

# route to the selected dish page
@app.route('/dish', methods=['POST'])
def dish():
    if request.method == 'POST':

        # obtain summary of selected dish using wikipedia scraper
        dish = request.form.get("group1")
        url = "https://wiki-scraper-331405.uc.r.appspot.com/"+dish+"/summary"
        dish_description = requests.get(url).json()["summary"]

        # obtain dish image url with google image scraper
        url = "https://mycovidupdatermicroservice.herokuapp.com/imgScraper"
        data = {"imgSize": "LARGE", "fileType": "jpeg", "imgType": "photo", "num": 1, "q": dish}
        dish_image = requests.post(url, json=data).json()["0"]

        # display both summary and image of the dish
        return render_template("dish.html", dish=dish, dish_image=dish_image, dish_description=dish_description)
