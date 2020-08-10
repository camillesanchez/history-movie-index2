from database.models import *
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from flask import Flask, g, request
from flask.json import jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DATABASE = '/Users/camillesanchez/Desktop/hmi/Website Code/flask_backend/database/history_movies_index.db'

def init_session():
    """
    :return: Session
    """
    engine = create_engine('sqlite:///'+DATABASE)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    return session

@app.route('/')
def home():
    return 'Hello to the homepage!'

@app.route('/period_timeline')
def getPeriodTimeline():
    return "Here you will find a timeline with all the periods!"

@app.route('/subperiod_timeline')
def getSubPeriodTimeline():
    return "Here you will find a timeline with all the subperiods!"

@app.route('/films_list')
def getFilmsList():
    session = init_session()
    films = session.query(Film).all()
    results = [film.json() for film in films]
    for result in results:
        keys = ["associated_genres", "plots", "synopses"]
        for key in keys:
            del result[key]
    return jsonify(results)

@app.route('/selected_film')
def getSelectedFilm():
    return "Here you will find your selecetd film!"


if __name__ == '__main__':
    app.run() 
