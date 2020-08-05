from database.models import *
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from flask import Flask, g, request
import sqlite3

app = Flask(__name__)

DATABASE = '/Users/camillesanchez/Desktop/hmi/Website Code/flask_backend/database/history_movies_index_shortversion.db'

def init_session():
    """
    :return: Session
    """
    engine = create_engine('sqlite:///'+DATABASE)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    return session

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    if rv:
        print("Gets data from DB")
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/')
def index():
    return "hello"

@app.route('/json_test')
def json_test():
    session = init_session()



@app.route('/selected_film')
def getSelectedFilm():

    test = request.args.get('test')
    print(test)

    res = query_db('select * from film')

    for user in res:
        # print(user[0], user[1])
        pass

    return "1917 is the best film!"


@app.route('/')
def home():
    return 'Hello to the homepage!'

@app.route('/timeline')
def getTimeline():
    return "Here you will find a timeline with all the periods!"

@app.route('/film_list_for_subperiod')
def getFilmListForSubperiod():
    return "Here you will find a timeline with all the subperiods!"


if __name__ == '__main__':
    app.run() 
