from flask import Flask, render_template, json, redirect, jsonify, url_for, flash
from flask import request

app = Flask(__name__)

# this is the route to the main page
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dish', methods=['POST'])
def dish():
    if request.method == 'POST':
        dish = request.form.get("group1")
        description = "Bibimbap[1] (/ˈbiːbɪmbæp/ BEE-bim-bap,[2] from Korean 비빔밥 [pi.bim.p͈ap̚], literally 'mixed rice'), sometimes romanized as bi bim bap or bi bim bop, is a Korean rice dish. The term 'bibim' means mixing rice (burned rice at the bottom of the dish and cooked rice), while the 'bap' noun refers to rice. Bibimbap is served as a bowl of warm white rice topped with namul (sautéed and seasoned vegetables) or kimchi (traditional fermented vegetables) and gochujang (chili pepper paste), soy sauce, or doenjang (a fermented soybean paste). A raw or fried egg and sliced meat (usually beef) are common additions. The hot dish is stirred together thoroughly just before eating.[3] In South Korea, Jeonju, Jinju, and Tongyeong are especially famous for their versions of bibimbap.[4] In 2011, the dish was listed at number 40 on the World's 50 most delicious foods readers' poll compiled by CNN Travel."
        return render_template("dish.html", dish=dish, dish_description=dish_description)