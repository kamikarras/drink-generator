"""Utility file to seed mixes database from letter-drinks csv file"""

from model import Mix
from model import connect_to_db, db
from model import app
import csv

def load_mixes():
    """loads the letter ingredient combos from csv"""

    with open('drink-letters.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            letter, ingredient = row[:2]
            if row[2] == "TRUE":
                spirit = True
            elif row[2] == "":
                spirit = None
            mix = Mix(ingredient=ingredient,
                      letter=letter,
                      alcohol=spirit)
            db.session.add(mix)

    db.session.commit()

connect_to_db(app)
load_mixes()