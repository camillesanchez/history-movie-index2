from models import *

# Connects to DB
engine = create_engine('sqlite:///history_movies_index.db')
Base.metadata.create_all( engine )