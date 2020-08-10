from models import *
from sqlalchemy.orm import sessionmaker

# File names:
DATABASE = "history_movies_index.db"
IMDB_file = "title.basics.tsv"

# Connect to DB
engine = create_engine('sqlite:///' + DATABASE)
Base.metadata.create_all( engine )
Session = sessionmaker(bind=engine)
session = Session()

# Make connections between tables

keywords = session.query(Keyword).all()
for keyword in keywords:

    # Search synopisis that match keyword
    synopses = session.query(Synopsis).filter(Keyword.keyword_word.like(f'%{keyword.keyword_word}%')).all()

    # For each associates synposis, add association with current keyword
    for synposis in synopses:
        keyword.associated_synopses.append(synposis)

    #Search for plots matching keyword:
    plots = session.query(Plot).filter(Plot.plot_script.like(f'%{keyword.keyword_word}%')).all()

    # For each associated plots, add association to current keyword
    for plot in plots:
        print(plot)
        keyword.associated_plots.append(plot)

    session.commit()

