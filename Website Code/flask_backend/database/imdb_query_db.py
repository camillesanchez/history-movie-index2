from sqlalchemy.orm import sessionmaker
from models import *

# Connect to DB
engine = create_engine('sqlite:///history_movies_index.db')
Base.metadata.create_all( engine )
Session = sessionmaker(bind=engine)
session = Session()

query = session.query(Film.id,Film.director,Film.plots)
for film in query:
    print(film,"\n")
    print(film[2], type(film[2]))
