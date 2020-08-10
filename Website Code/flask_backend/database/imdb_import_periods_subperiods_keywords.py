from models import *
from module_db import *
from sqlalchemy.orm import sessionmaker
import csv, json
from historical_periods.scraping_histo_periods_tt import get_dictionary_from_json

# File names:
DATABASE = "history_movies_index.db"
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
            every_keyword = every_keyword.lower()
            print(every_keyword)
            keyword_instance = Keyword()

            query = session.query(Keyword).filter_by(keyword_word = every_keyword)
            if query.count() == 0:
                keyword_instance.keyword_word = every_keyword
                keyword_instance.associated_subperiods.append(subperiod_instance)
                print("{keyword_instance} added")
                session.add(keyword_instance)
            elif query.count() != 0:
                print("{keyword_instance} set to Null?")
                keyword_instance.associated_subperiods.append(subperiod_instance)

        session.add(subperiod_instance)
    session.add(period_instance)

session.commit()

print(f"\nTables Subperiod, Subperiod and Keyword were created.\n")


