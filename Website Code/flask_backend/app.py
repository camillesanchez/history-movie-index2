from database.models import *
from app_modules import *
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
    """ Returns a new session """

    engine = create_engine('sqlite:///'+DATABASE)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    return session

@app.route('/')
def home():
    """ Route to the homepage. """

    return 'Hello to the homepage!'

@app.route('/about')
def about():
    """ Route to the about page. """

    return 'Hello to the about page!'

@app.route('/period_timeline')
def getPeriodTimeline():
    """ Route to the Period Timeline Page.
    Returns a json with all the necessary information for the Period timeline page."""

    # Inits session and gets json file with periods information
    session = init_session()
    periods = session.query(Period).all()

    multiperiods = []
    # Gets necessary fiels from period query
    for period in periods:
        # gets period name & id
        period_id = period.id
        period_name = period.period_name
        
        # formats period dates
        period_start_date = period.start_date
        period_end_date = period.end_date
        period_dates = f"{period_start_date} - {period_end_date}"
        
        # formats subperiod content
        subperiods_string = ""
        for subperiod in period.subperiods:
            if subperiod != period.subperiods[-1]:
                subperiods_string += subperiod.subperiod_name + ", "
            else:
                subperiods_string += "& " + subperiod.subperiod_name
        
        # Create list of period dictionaries & close session
        period_dictionary = {"period_id": period_id, "period_name": period_name, "period_start_date": period_start_date, "period_dates": period_dates, "period_subperiods": subperiods_string}
        multiperiods.append(period_dictionary)

    # Transform list in Json format:
    periods_json =json.dumps(multiperiods, indent =4)
    print(periods_json)
    session.close()

    return periods_json

@app.route('/subperiod_timeline/<int:period_id>')
def getSubPeriodTimeline(period_id):
    """ Route to the Subperiod Timeline Page.
    Returns a json with all the necessary subperiod data from period_id."""

    # Inits a session & queries all subperiods for specific period_id
    session = init_session()
    subperiods = session.query(Subperiod).join(Subperiod.associated_period).filter(Period.id == period_id).all()

    multisubperiods = []
    for subperiod in subperiods:
        # Gets subperiod ID & name
        subperiod_id = subperiod.id
        subperiod_name = subperiod.subperiod_name
        
        # Formats subperiod dates:
        subperiod_start_date = subperiod.start_date
        subperiod_end_date = subperiod.end_date
        subperiod_dates = f"{subperiod_start_date} - {subperiod_end_date}"
        
        # Formats subperiod locations:
        subperiod_locations = subperiod.period_location
        
        # Create list of subperiod dictionaries
        subperiod_dictionary = {"subperiod_id": subperiod_id, "subperiod_name": subperiod_name, "subperiod_start_date": subperiod_start_date, "subperiod_dates": subperiod_dates, "subperiod_locations": subperiod_locations}
        multisubperiods.append(subperiod_dictionary)
    
    # Transforms list in Json format & close session:
    subperiods_json =json.dumps(multisubperiods, indent =4)
    session.close()

    return subperiods_json

@app.route('/subperiod_period_names/<int:subperiod_id>')
def getSubperiodPeriodNames(subperiod_id):
    """ Route that returns a dictionary with the name of the period and subperiod 
    that did not return a film list."""

    # Inits session with db
    session = init_session()
    
    # Query subperiod and period name from subperiod_id
    query_subperiod = session.query(Subperiod).filter(Subperiod.id ==subperiod_id).one()
    subperiod_name = query_subperiod.subperiod_name 
    period_name = query_subperiod.associated_period.period_name

    # Closes session
    session.close()

    return {"period_name": period_name, "subperiod_name": subperiod_name}

@app.route('/films_list/<int:subperiod_id>')
def getFilmsList(subperiod_id):
    """ Route to the films_list page.
    Returns a json of the films found after complex database query from subperiod_id."""

    # Gets page number from user
    args = request.args
    page_number = 1
    if "page_number" in args:
        page_number = int(args["page_number"])
    
    # Inits session
    session = init_session()

    # Query Database to get Subperiod and Period Names:
    query_subperiod = session.query(Subperiod).filter(Subperiod.id ==subperiod_id).one()
    subperiod_name = query_subperiod.subperiod_name 
    period_name = query_subperiod.associated_period.period_name

    ## Complex query:
        # Query Database from Film > Plots > Keywords > Subperiod
    query_films_par_plot = session.query(Film).join(Film.plots).join(Plot.associated_keywords).join(Keyword.associated_subperiods).filter(Subperiod.id == subperiod_id)
    
        # Query Database from Film > Synopses > Keywords > Subperiod
    query_films_par_synopsis = session.query(Film).join(Film.synopses).join(Synopsis.associated_keywords).join(Keyword.associated_subperiods).filter(Subperiod.id == subperiod_id)

        # Join queries to create a complete query & gets top 30
    number_of_films_per_page = 3
    query_totale = query_films_par_plot.union( query_films_par_synopsis ).limit(number_of_films_per_page).offset((page_number - 1) * number_of_films_per_page).all() 
    query_totale_count = query_films_par_plot.union( query_films_par_synopsis ).count() 

    # Gets data from films of query:
    multifilms = []
    for film in query_totale:

            # Gets film name & ID
            film_id = film.id
            film_name = film.primary_title

            # Formats film plot to remove author's name
            film_plot = film.plots[0].plot_script
            new_film_plot = film_plot.split("::")[0]
            film_image_url = film.image_url
            
            # Creates a list of dictionaries of the films selected from complexe query
            film_dictionary = {"period_name": period_name, "subperiod_name": subperiod_name, "film_id": film_id, "film_name": film_name, "film_plot": new_film_plot, "film_image_url": film_image_url}
            multifilms.append(film_dictionary)

    # Gets a dictionary from multifilms, number_of_films_per_page & query_totale_count
    total_films = { "total_films_number": query_totale_count, "films_per_page": number_of_films_per_page, "films_list": multifilms }
    print(total_films)

    session.close()

    return json.dumps(total_films, indent =4)

@app.route('/selected_film/<int:subperiod_id>/<int:film_id>')
def getSelectedFilm(subperiod_id, film_id):
    """ Route to selected_film page.
    Returns a dictionary with specific film data from film_id."""

    # Inits session
    session = init_session()

    selected_film_dictionary = {}

    # Queries period and subperiod names
    subperiod = session.query(Subperiod).filter(Subperiod.id == subperiod_id).one()
    film_subperiod = subperiod.subperiod_name
    selected_film_dictionary["film_subperiod"] = film_subperiod
    film_period = subperiod.associated_period.period_name
    selected_film_dictionary["film_period"] = film_period

    # Queries Film data
    film = session.query(Film).filter(Film.id == film_id).one()
        # Gets film ID, primary title, release year & film_URL
    film_id = film.id
    selected_film_dictionary["film_id"] = film_id
    film_title = film.primary_title
    selected_film_dictionary["film_title"] = film_title
    film_release_date = film.year
    selected_film_dictionary["film_release_date"] = film_release_date
    film_image_url = film.image_url
    selected_film_dictionary["film_image_url"] = film_image_url

        # Formats film runtime time
    print(film.runtime)
    film_runtime = formatsFilmRuntime(film.runtime)
    selected_film_dictionary["film_runtime"] = film_runtime

        # Formats film's genres
    print(film.associated_genres)
    genres = formatsGenres(film.associated_genres)
    selected_film_dictionary["film_genres"] = genres

        # Formats Directors' names:
    print(film.director)
    film_directors = formatsDirectorsField(film.director)
    selected_film_dictionary["film_directors"] = film_directors

        # Formats writers' names:
    print(film.writer)
    film_writers = formatsWritersField(film.writer)
    selected_film_dictionary["film_writers"] = film_writers

        # Formats film plot by removing author
    film_plot = film.plots[0].plot_script
    new_film_plot = film_plot.split("::")[0]
    selected_film_dictionary["film_plot"] = new_film_plot

        # Gets Trailer Url
    trailer_url = getsTrailerUrl(film.imdb_url)
    if trailer_url != None:
        selected_film_dictionary["trailer_url"] = trailer_url

    # Returns film dictionary
    print(selected_film_dictionary)
    return selected_film_dictionary


if __name__ == '__main__':
    app.run() 
