from database.models import *
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from flask import Flask, g, request
from flask.json import jsonify
from flask_cors import CORS
import sqlite3, json, math

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

@app.route('/about')
def about():
    return 'Hello to the about page!'

@app.route('/period_timeline')
def getPeriodTimeline():
    """ Returns a dictionary with all the necessary period data."""

    # Gets json file with periods information
    session = init_session()
    periods = session.query(Period).all()
    print(periods)

    multiperiods = []
    for period in periods:
        # period name & id
        period_id = period.id
        period_name = period.period_name
        
        # period dates:
        period_start_date = period.start_date
        period_end_date = period.end_date
        period_dates = f"{period_start_date} - {period_end_date}"
        
        # Subperiod content:
        periods_subperiods = period.subperiods
        subperiods= ""
        for subperiod in period.subperiods:
            if subperiod != period.subperiods[-1]:
                subperiods += subperiod.subperiod_name + ", "
            else:
                subperiods += "& " + subperiod.subperiod_name
        
        # Json format:
        period_json = {"period_id": period_id, "period_name": period_name, "period_start_date": period_start_date, "period_dates": period_dates, "periods_subperiods": subperiods}
        multiperiods.append(period_json)

    periods_json =json.dumps(multiperiods, indent =4)
    print(periods_json)
    session.close()

    return periods_json

@app.route('/subperiod_timeline/<int:period_id>')
def getSubPeriodTimeline(period_id):
    """ Returns a dictionary with all the necessary subperiod data from period_id, 
    passed from the /period_timeline/ page."""

    # Gets json file with periods information
    session = init_session()

    subperiods = session.query(Subperiod).join(Subperiod.associated_period).filter(Period.id == period_id).all()

    multisubperiods = []
    for subperiod in subperiods:
        # Subperiod name
        subperiod_id = subperiod.id
        subperiod_name = subperiod.subperiod_name
        
        # Subperiod dates:
        subperiod_start_date = subperiod.start_date
        subperiod_end_date = subperiod.end_date
        subperiod_dates = f"{subperiod_start_date} - {subperiod_end_date}"
        
        # Subperiod locations:
        subperiods_locations = subperiod.period_location
        
        # Json format:
        subperiod_json = {"subperiod_id": subperiod_id, "subperiod_name": subperiod_name, "subperiod_start_date": subperiod_start_date, "subperiod_dates": subperiod_dates, "subperiods_locations": subperiods_locations}
        multisubperiods.append(subperiod_json)
        
    subperiods_json =json.dumps(multisubperiods, indent =4)

    session.close()

    return subperiods_json

@app.route('/subperiod_period_names/<int:subperiod_id>')
def getSubperiodPeriodNames(subperiod_id):
    """ Returns a dictionary with the name of the period and subperiod 
    that did not return a film list."""

    session = init_session()
    
    query_subperiod = session.query(Subperiod).filter(Subperiod.id ==subperiod_id).one()
    subperiod_name = query_subperiod.subperiod_name 
    period_name = query_subperiod.associated_period.period_name

    return {"period_name": period_name, "subperiod_name": subperiod_name}

@app.route('/films_list/<int:subperiod_id>')
def getFilmsList(subperiod_id):
    """ Returns a json of the films found from subperiod (subperiod_id 
    passed from the /subperiod_timeline/ page."""

    session = init_session()

    query_films_par_plot = session.query(Film).join(Film.plots).join(Plot.associated_keywords).join(Keyword.associated_subperiods).filter(Subperiod.id == subperiod_id)
    
    query_films_par_synopsis = session.query(Film).join(Film.synopses).join(Synopsis.associated_keywords).join(Keyword.associated_subperiods).filter(Subperiod.id == subperiod_id)

    query_totale = query_films_par_plot.union( query_films_par_synopsis )

    query_subperiod = session.query(Subperiod).filter(Subperiod.id ==subperiod_id).one()
    subperiod_name = query_subperiod.subperiod_name 
    period_name = query_subperiod.associated_period.period_name

    counter = 0
    multifilms = []
    for film in query_totale:
        counter +=1
        if counter <=10:
            film_id = film.id
            film_name = film.primary_title

            # Format film plot
            film_plot = film.plots[0].plot_script
            new_film_plot = film_plot.split("::")[0]
            film_image_url = film.image_url
            
            # Json format:
            film_json = {"period_name": period_name, "subperiod_name": subperiod_name, "film_id": film_id, "film_name": film_name, "film_plot": new_film_plot, "film_image_url": film_image_url}
            multifilms.append(film_json)
        else:
            break
        
    films_json =json.dumps(multifilms, indent =4)
    print(films_json)
    session.close()

    return films_json

@app.route('/selected_film/<int:subperiod_id>/<int:film_id>')
def getSelectedFilm(subperiod_id, film_id):
    """ Returns a dictionary of all the necesarry selected film data 
    from film_id passed from the /films_list/ page."""

    print(subperiod_id, film_id)
    session = init_session()

    # Get period and subperiod info
    subperiod = session.query(Subperiod).filter(Subperiod.id == subperiod_id).one()
    
    film_subperiod = subperiod.subperiod_name
    film_period = subperiod.associated_period.period_name

    # Get Film info
    film = session.query(Film).filter(Film.id == film_id).one()

    film_id = film.id
    film_title = film.primary_title
    film_release_date = film.year

    # Format runtime
    if film.runtime != None:
        number_hours = math.floor(int(film.runtime)/60)
        number_minutes = math.floor(int(film.runtime) - (number_hours * 60))
        if number_hours ==0:
            film_runtime = f"{number_minutes}min"
        elif number_minutes == 0:
            film_runtime = f"{number_hours}h"
        else:
            film_runtime = f"{number_hours}h {number_minutes}min"
    else:
        film_runtime = "Unknown"

    # Format genres
    genres = ""
    if len(film.associated_genres) >=0:
        print("here", len(film.associated_genres))
        genres = "Unknown"
    else:
        for genre in film.associated_genres:
            if len(film.associated_genres) == 1:
                print("here2")
                genres = genre.genre_type
            elif genre != film.associated_genres[-1]:
                genres += genre.genre_type + ", "
            elif genre == film.associated_genres[-1]:
                genres += "& " + genre.genre_type

    # Directors:
    film_directors=""
    for director in film.director:
        if len(film.director) == 1:
            film_directors = director
        elif director != film.director[-1]:
            film_directors += director + ", "
        else:
            film_directors += "& " + director 

    # Writers:
    film_writers=""
    if film.writer != None:
        for writer in film.writer:
            if len(film.writer) == 1:
                film_writers = director
            elif writer != film.writer[-1]:
                film_writers += writer + ", "
            else:
                film_writers += "& " + writer 
    else:
        film_writers = "Unknown"

    # Format film plot
    film_plot = film.plots[0].plot_script
    new_film_plot = film_plot.split("::")[0]

    film_image_url = film.image_url

    selected_film_json = {"film_subperiod":film_subperiod, "film_period": film_period, "film_id": film_id, "film_title": film_title, "film_release_date": film_release_date, "film_genres": genres, "film_runtime": film_runtime, "film_directors": film_directors, "film_writers": film_writers, "film_plot": new_film_plot, "film_image_url": film_image_url}
    print(selected_film_json)
    return selected_film_json


if __name__ == '__main__':
    app.run() 
