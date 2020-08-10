from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import inspect, Column, Integer, String, Float, ForeignKey, Table, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.types import PickleType
from datetime import datetime
from weakref import WeakValueDictionary
from flask.json import jsonify

Base = declarative_base()

class BaseModel:

    def json(self):
        return {
            column: self._format_value(value)
            for column, value in self._to_dict().items()
        }

    to_json_datetime_format = "%Y-%m-%dT%H:%M:%S"

    def _format_value(self, value):
        """ Format value depending on type """
        if isinstance(value, datetime):
            return value.strftime(self.to_json_datetime_format)
        if isinstance(value, BaseModel):
            print("hello")
            return value.json()
        return value

    def _to_dict(self):
        return {column.key: getattr(self, column.key) for column in inspect(self.__class__).attrs}

# ASSOCIATION TABLES:

keyword_plot = Table('keyword_plot', Base.metadata,
    Column('plot_id', Integer, ForeignKey('plot.id')),
    Column('keyword_id', Integer, ForeignKey('keyword.id'))
)

keyword_synopsis = Table('keyword_synopsis', Base.metadata,
    Column('synopsis_id', Integer, ForeignKey('synopsis.id')),
    Column('keyword_id', Integer, ForeignKey('keyword.id'))
)

film_genre = Table('film_genre', Base.metadata,
    Column('film_id', Integer, ForeignKey('film.id')),
    Column('genre_id', Integer, ForeignKey('genre.id'))
)

keyword_subperiod = Table('keyword_subperiod', Base.metadata,
    Column('subperiod_id', Integer, ForeignKey('subperiod.id')),
    Column('keyword_id', Integer, ForeignKey('keyword.id'))
)

# TABLES REGARDING FILMS:
class Film(Base, BaseModel):
    __tablename__ = "film"
    id = Column(Integer, primary_key = True)
    id_imdb = Column(String)
    primary_title = Column(String)
    original_title = Column(String)
    associated_genres = relationship('Genre', back_populates='associated_films', secondary='film_genre', lazy="joined")
    runtime = Column(String)
    year = Column(String)
    director = Column(PickleType)
    writer = Column(PickleType)
    cast = Column(PickleType)
    image_url = Column(String)
    imdb_url = Column(String)
    ## keywords per film ?

    def __repr__(self):
        if self.primary_title == None:
            return "Film Primary Title Unknown"
        else:
            return "Film Primary Title: " + self.primary_title + "(IMDb ID: "+ self.id_imdb + ")"

class Genre(Base, BaseModel):
    __tablename__ = "genre"
    id = Column(Integer, primary_key = True)
    genre_type = Column(String)
    associated_films = relationship('Film', back_populates='associated_genres', secondary='film_genre')

    def __repr__(self):
        if self.genre_type == None:
            return "Genre Unknown"
        else:
            return "Genre: " + self.genre_type

class Plot(Base):
    __tablename__ = "plot"
    id = Column(Integer, primary_key = True)
    plot_script = Column(String)
    film_id = Column(Integer, ForeignKey('film.id'), nullable = False)
    associated_film = relationship("Film", backref = "plots")
    associated_keywords = relationship('Keyword', back_populates='associated_plots', secondary='keyword_plot')

    def __repr__(self):
        if self.plot_script == None:
            return "Plot Unknown"
        else:
            return "Plot: " + self.plot_script

class Synopsis(Base):
    __tablename__ = "synopsis"
    id = Column(Integer, primary_key = True)
    synopsis_script = Column(String)
    film_id = Column(Integer, ForeignKey('film.id'), nullable = False)
    associated_film = relationship("Film", backref = "synopses")
    associated_keywords = relationship('Keyword', back_populates='associated_synopses', secondary='keyword_synopsis')

    def __repr__(self):
        if self.synopsis_script == None:
            return "Synopsis Unknown"
        else:
            return "Synopsis: " + self.synopsis_script

# TABLES REGARDING HISTORY:
class Period(Base):
    __tablename__= "period"
    id = Column(Integer, primary_key = True)
    period_name = Column(String)
    start_date = Column(String)
    end_date = Column(String)

    def __repr__(self):
        if self.period_name == None:
            return "Period Unknown"
        else:
            return "Period: " + self.period_name

class Subperiod(Base):
    __tablename__= "subperiod"
    id = Column(Integer, primary_key = True)
    subperiod_name = Column(String)
    start_date = Column(String)
    end_date = Column(String)
    period_location = Column(String)
    period_id = Column(Integer, ForeignKey('period.id'), nullable = False)
    associated_period = relationship("Period", backref = "subperiods")
    associated_keywords = relationship("Keyword", back_populates="associated_subperiods", secondary="keyword_subperiod")

    def __repr__(self):
        if self.subperiod_name == None:
            return "Sub-period Unknown"
        else:
            return "Sub-period: " + self.subperiod_name

class Keyword(Base):
    __tablename__= "keyword"
    id = Column(Integer, primary_key = True)
    keyword_word = Column(String)
    associated_subperiods = relationship("Subperiod", back_populates="associated_keywords", secondary="keyword_subperiod")
    associated_plots = relationship('Plot', back_populates='associated_keywords', secondary='keyword_plot')
    associated_synopses = relationship('Synopsis', back_populates='associated_keywords', secondary='keyword_synopsis')

    def __repr__(self):
        if self.keyword_word == None:
            return "Keyword Unknown"
        else:
            return "Keyword: " + self.keyword_word


