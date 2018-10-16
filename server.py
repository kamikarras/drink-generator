from flask import Flask, render_template, redirect, request, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from model import app, Mix, connect_to_db, db

app = Flask(__name__)


@app.route('/')
def show_home():
    """shows the hompage"""

    return render_template("homepage.html")

@app.route('/results')
def show_drink():
    """displays the drink"""
    name = request.args.get('name')
    ingredients = []
    vowels = 0
    for letter in name:
        if letter.isalpha():
            letter = letter.upper()
            if letter in "AEIUOY" and vowels > 0:
                ingredients.append("Ice")
            else:
                mix = Mix.query.filter(Mix.letter==letter).first()
                ingredients.append(mix.ingredient)
                if letter in "AEIUOY":
                    vowels += 1
    ingredients = set(ingredients)

    return render_template("homepage.html",
                            ingredients=ingredients,
                            name=name)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    # app.debug = True
    # make sure templates, etc. are not cached in debug mode
    # app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    app.run(port=5000, host='0.0.0.0')
