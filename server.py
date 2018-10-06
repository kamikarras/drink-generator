from flask import Flask, render_template, redirect, request, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from model import app, Mix, connect_to_db, db

app = Flask(__name__)

app.secret_key = "ABC"

@app.route('/', methods=["GET"])
def show_home():
    """shows the hompage"""

    return render_template("homepage.html")

@app.route('/', methods=["POST"])
def show_drink():
    """displays the drink"""
    name = request.form.get('name')
    ingredients = []
    for letter in name:
        if letter.isalpha():
            letter = letter.upper()
            mix = Mix.query.filter(Mix.letter==letter).first()
            ingredients.append(mix.ingredient)
    ingredients = set(ingredients)

    return render_template("homepage.html",
                            ingredients=ingredients)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    app.run(port=5000, host='0.0.0.0')
