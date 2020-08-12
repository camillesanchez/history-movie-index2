from models import *
from module_db import *
from sqlalchemy.orm import sessionmaker
import csv, json

# File names:
DATABASE = "history_movies_index2.db"
IMDB_file = "title.basics.tsv"

# Connect to DB
engine = create_engine('sqlite:///' + DATABASE)
Base.metadata.create_all( engine )
Session = sessionmaker(bind=engine)
session = Session()

# Import movie titles in DB
tsv_f = open(IMDB_file, 'r')
read_tsv = csv.reader(tsv_f, delimiter = "\t")

counter =0

for row in read_tsv:
    print(counter)
    print(row)
    if counter <= 2000:
        # Create film in DB:
        if row[1] == "movie":

            film = Film()
            film.id_imdb = row[0]

            indexes1 = [2,3,5,7,8]
            normal_table_len = 9
            # Makes sure that the index exists in row:
            if (len(row)-1) >= indexes1[-1]:
                # Sets value to Null in DB if equal to "\n":
                for index in indexes1:
                    if row[index] == ("\\N"):
                        row[index] = None
            else:
                # Sets values to Null in DB if length of row inferior to index of item:     
                for index in indexes1:
                    for every_blank_column_index in range(index, normal_table_len):
                        row[every_blank_column_index]= None
                        print(f"Check film {film.id_imdb} that item missing is now Null in DB.")

            # Sets fields in DB      
            film.primary_title = row[2]
            film.original_title = row[3]
            film.year = row[5]
            film.runtime = row[7]

            ## STEP to reduce database (takes too long to load) - 
            ## This if...elif...else statement will only add films after 2015:

            if film.year == None or film.year == '\\N':
                pass
            elif int(film.year) == 2019 or int(film.year) == 2020:
                # Add Genres to table in DB
                if row[8] != None:
                    genres_list = row[8].split(",")
                    for genre in genres_list:
                        query = session.query(Genre).filter_by(genre_type = genre)
                        genre_instance = Genre()
                        if query.count() ==0:
                            genre_instance.genre_type = genre
                            session.add(genre_instance)
                        else:
                            genre_instance = query.one()
                        genre_instance.associated_films.append(film) 

                # Retreiving data from IMDb and setting them to Null in DB or value:
                retrieved_data = getIMDbDataFromFields(film.id_imdb, "plot", "synopsis","director","writer","cast", "cover url")
                
                for item_index in range(len(retrieved_data)):
                    if retrieved_data[item_index] == "None" or retrieved_data[item_index] == "\\N" or retrieved_data[item_index] == None:
                        retrieved_data[item_index] = None

                # Sets fields in DB
                film.director = retrieved_data[2]
                film.writer = retrieved_data[3]
                film.cast = retrieved_data[4]
                film.image_url = retrieved_data[5]
                film.imdb_url = retrieved_data[6]

                if retrieved_data[0] != None or retrieved_data[1] != None:  # If no plots or synopsis can't do the sorting
                    
                    # Create Plot table:
                    if retrieved_data[0] !=None:
                        for plot in retrieved_data[0]:
                            # WARNING some plot might be there twice
                            plot_instance = Plot()
                            plot_instance.plot_script = plot
                            plot_instance.associated_film = film
                            session.add(plot_instance)

                    # Create Synopsis table:
                    if retrieved_data[1] !=None:
                        for synopsis in retrieved_data[1]:
                            synopsis_instance = Synopsis()
                            synopsis_instance.synopsis_script = synopsis
                            synopsis_instance.associated_film = film
                            session.add(synopsis_instance)

                    session.add(film)
                    counter+=1
                    print(f"{film.id_imdb} added.")
    
    else:
        break

tsv_f.close()
session.commit()

print(f"\nTables Film, Plot, Synopsis and Genre were created.\n")


