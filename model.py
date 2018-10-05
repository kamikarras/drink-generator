from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import load_only, relationship

db = SQLAlchemy()


class Mix(db.Model):
    """Ingredient Model"""

    __tablename__ = "mixes"

    mix_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ingredient = db.Column(db.String(64), nullable=False)
    letter = db.Column(db.String(1), nullable=False)

    def __repr__(self):
        """displays mix"""

        return f"""<Mix
                    mix_id={self.mix_id}
                    ingredient={self.ingredient}
                    letter={self.letter}"""




def connect_to_db(app):
    """Connect to database."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///mixes'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)                    


app = Flask(__name__)

if __name__ == "__main__":
    connect_to_db(app)
    # load_jobs()
    # load_skills()
    # load_job_skill_counts()
    db.create_all()
