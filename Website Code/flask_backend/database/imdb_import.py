from models import *
from module_db import *
from sqlalchemy.orm import sessionmaker
import csv, json
from historical_periods.scraping_histo_periods_tt import get_dictionary_from_json

# File names:
DATABASE = "history_movies_index.db"
IMDB_file = "title.basics.tsv"
HISTORICAL_TERMINOLOGY_JSON = "history_terminology.json"
HISTORICAL_PERIODS_JSON  = "historical_periods.json"

# Connect to DB
engine = create_engine('sqlite:///' + DATABASE)
Base.metadata.create_all( engine )
Session = sessionmaker(bind=engine)
session = Session()

# Import Periods, Subperiods and Keyword Tables in DB:
json_f = getHistoricalPeriodsJSON(HISTORICAL_TERMINOLOGY_JSON , HISTORICAL_PERIODS_JSON)
data = get_dictionary_from_json(json_f)

for period_index in data:
    
    # Create a period in DB:
    period_instance = Period()
    period_instance.period_name = data[period_index]["period_name"]
    period_instance.start_date = data[period_index]["dates"][0]
    period_instance.end_date = data[period_index]["dates"][1]

    # Create a subperiod in DB:
    sub_period_dict = data[period_index]["sub-periods"]

    for subperiod_index in sub_period_dict:
        subperiod_instance = Subperiod()
        subperiod_instance.subperiod_name = sub_period_dict[subperiod_index]['sub-period_name']
        subperiod_instance.start_date = sub_period_dict[subperiod_index]['dates'][0]
        subperiod_instance.end_date = sub_period_dict[subperiod_index]['dates'][1]
        subperiod_instance.period_location = sub_period_dict[subperiod_index]['period_location']

        try: 
            period_instance.subperiods
        except:
            subperiod_instance.associated_period = period_instance
        else:
            period_instance.subperiods.append(subperiod_instance)
        
        # Create a keyword in DB:
        keyword_list = sub_period_dict[subperiod_index]["keywords"]

        for every_keyword in keyword_list:
            # WARNING: A keyword can appear twice in DB (for multiple subperiods):
            keyword_instance = Keyword()
            keyword_instance.keyword_word = every_keyword

            try:
                subperiod_instance.keywords
            except:
                keyword_instance.associated_subperiods = subperiod_instance
            else:
                subperiod_instance.keywords.append(keyword_instance)

# Import movie titles in DB
            tsv_f = open(IMDB_file, 'r')
            read_tsv = csv.reader(tsv_f, delimiter = "\t")

            counter = 0
            for row in read_tsv:
                print(row)
                
                if counter <=10:
                    # Create film in DB:
                    if row[1] == "movie":
                        counter +=1
                        film = Film()
                        film.id_imdb = row[0]

                        try:
                            # Sets film year to Null in DB or a value:
                            indexes1 = [2,3,5,7,8]
                            for index in indexes1:
                                if row[index] == ("\\N"):
                                    row[index] = None

                            # Sets fields in DB      
                            film.primary_title = row[2]
                            film.original_title = row[3]
                            film.year = row[5]
                            film.runtime = row[7]
                            film.genre = row[8]

                        # Sets values to Null in DB if length of row inferior to index of item: 
                        except OperationalError:
                            indexes2 = [2,3,5,7,8]
                            normal_table_len = 9

                            for index in indexes2:
                                if index > (len(row) -1):
                                    for every_blank_column_index in range(index, normal_table_len):
                                        row[every_blank_column_index]= None

                            film.primary_title = row[2]
                            film.original_title = row[3]
                            film.year = row[5]
                            film.runtime = row[7]
                            film.genre = row[8]
                            print(f"Check film {film.id_imdb} that item missing is now Null in DB.")

                        ## STEP to reduce database (takes too long to load) - 
                        ## This if...elif...else statement will only add films after 2010:

                        # print(film.year)

                        if film.year == None or film.year == '\\N':
                            pass
                        elif int(film.year) < 2010:
                            pass
                        else:
                            # Retreiving data from IMDb and setting them to Null in DB or value:
                            retrieved_data = getIMDbDataFromFields(film.id_imdb, "plot", "synopsis","director","writer","cast", "cover url")
                            
                            for item_index in range(len(retrieved_data)):
                                if retrieved_data[item_index] == "None" or retrieved_data[item_index] == "\\N" or retrieved_data[item_index] == None:
                                    retrieved_data[item_index] = None

                            # Sets fields in DB
                            # film.plots = retrieved_data[0]
                            # film.synopsis = retrieved_data[1]
                            film.director = retrieved_data[2]
                            film.writer = retrieved_data[3]
                            film.cast = retrieved_data[4]
                            film.image_url = retrieved_data[5]
                            film.imdb_url = retrieved_data[6]

                            if retrieved_data[0] != None or retrieved_data[1] != None:  # If no plots or synopsis can't do the sorting
                                
                                # Create Plot table:
                                for plot in retrieved_data[0]:
                                    plot_instance = Plot()
                                    plot_instance.plot_script = plot
                                    plot_instance.associated_film = film
                                    session.add(plot_instance)

                                    if keyword_instance in plot:
                                        plot_instance.associated_keywords.append(keyword_instance)

                                # Create Synopsis table:
                                for synopsis in retrieved_data[1]:
                                    synopsis_instance = Synopsis()
                                    synopsis_instance.synopsis_script = synopsis
                                    synopsis_instance.associated_film = film
                                    session.add(synopsis_instance)

                                    if keyword_instance in synopsis:
                                        synopsis_instance.associated_keywords.append(keyword_instance)

                                session.add(film)
                                print(f"{film.id_imdb} added.")
              
            tsv_f.close()

            session.add(keyword_instance)
        session.add(subperiod_instance)
    session.add(period_instance)

session.commit()

print(f"\nDatabase {DATABASE} was created.\n")


