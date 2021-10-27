from flask import Flask, render_template, json, redirect, jsonify, url_for, flash
from flask import request

app = Flask(__name__)

# this is the route to the main page
@app.route('/')
def index():
    return render_template("index.html")