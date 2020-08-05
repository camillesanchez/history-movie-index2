from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.types import PickleType

Base = declarative_base()

# TABLE BETWEEN PLOT AND KEYWORD & BETWEEN SYNOPSIS AND KEYWORD: 
keyword_plot = Table('keyword_plot', Base.metadata,
    Column('plot_id', Integer, ForeignKey('plot.id')),
    Column('keyword_id', Integer, ForeignKey('keyword.id'))
)

keyword_synopsis = Table('keyword_synopsis', Base.metadata,
    Column('synopsis_id', Integer, ForeignKey('synopsis.id')),
    Column('keyword_id', Integer, ForeignKey('keyword.id'))
)

# TABLES REGARDING FILMS:
class Film(Base):
    __tablename__ = "film"
    id = Column(Integer, primary_key = True)
    id_imdb = Column(String)
    primary_title = Column(String)
    original_title = Column(String)
    genre = Column(String)
    runtime = Column(String)
    year = Column(String)
    director = Column(PickleType)
    writer = Column(PickleType)
    cast = Column(PickleType)
    # plots = Column(PickleType)
    # synopsis = Column(PickleType)
    image_url = Column(String)
    imdb_url = Column(String)
    ## keywords per film ?

    def __repr__(self):
        return self.primary_title

class Plot(Base):
    __tablename__ = "plot"
    id = Column(Integer, primary_key = True)
    plot_script = Column(String)
    film_id = Column(Integer, ForeignKey('film.id'), nullable = False)
    associated_film = relationship("Film", backref = "plots")
    associated_keywords = relationship('Keyword', back_populates='associated_plots', secondary='keyword_plot')

    def __repr__(self):
        return "Plot: " + self.plot_script

class Synopsis(Base):
    __tablename__ = "synopsis"
    id = Column(Integer, primary_key = True)
    synopsis_script = Column(String)
    film_id = Column(Integer, ForeignKey('film.id'), nullable = False)
    associated_film = relationship("Film", backref = "synopses")
    associated_keywords = relationship('Keyword', back_populates='associated_synopses', secondary='keyword_synopsis')

    def __repr__(self):
        return "Synopsis: " + self.synopsis_script

# TABLES REGARDING HISTORY:
class Period(Base):
    __tablename__= "period"
    id = Column(Integer, primary_key = True)
    period_name = Column(String)
    start_date = Column(String)
    end_date = Column(String)

    def __repr__(self):
        return "Period: " + self.period_name

# association_table = Table('subperiods_to_keywords', Base.metadata,
#     Column('subperiod_id', Integer, ForeignKey('subperiod.id')),
#     Column('keyword_id', Integer, ForeignKey('keyword.id'))
# )

class Subperiod(Base):
    __tablename__= "subperiod"
    id = Column(Integer, primary_key = True)
    subperiod_name = Column(String)
    start_date = Column(String)
    end_date = Column(String)
    period_location = Column(String)
    period_id = Column(Integer, ForeignKey('period.id'), nullable = False)
    associated_period = relationship("Period", backref = "subperiods")
    # associated_keywords = relationship("Keyword", secondary=association_table, back_populates="subperiods") # Not sure about the relationship

    def __repr__(self):
        return "Sub-period: " + self.subperiod_name

class Keyword(Base):
    __tablename__= "keyword"
    id = Column(Integer, primary_key = True)
    keyword_word = Column(String)
    subperiod_id = Column(Integer, ForeignKey('subperiod.id'), nullable = False)
    associated_subperiod = relationship("Subperiod", backref="keywords") # Not sure about the relationship
    # associated_subperiods = relationship("Subperiod", secondary=association_table, back_populates="keywords") # Not sure about the relationship
    associated_plots = relationship('Plot', back_populates='associated_keywords', secondary='keyword_plot')
    associated_synopses = relationship('Synopsis', back_populates='associated_keywords', secondary='keyword_plot')

    def __repr__(self):
        return "Keyword: " + self.keyword_word


