from historical_periods.scraping_histo_periods_tt import get_dictionary_from_json, get_historical_dictionary, save_dictionary_as_json
import sys, os
sys.path.insert(0,"/Users/camillesanchez/Desktop/hmi/imdbpy-master/")
from imdb import IMDb

def getIMDbDataFromFields(IMDb_id, *fields):
    """ Returns IMDb Datas from IMDb film ID 

    Note: All IMDB ID starts with tt (i.e. "tt8579674" for the film "1917"), 
    which need to be removed to use the IMDbPy modules. """

    ia = IMDb()
    film = ia.get_movie(IMDb_id[2:])
    
    person_fields = ["director","writer","cast"]

    fields_data = []
    for field in fields:
        try:
            if field in person_fields:
                data = []
                for person_name in film[field]:
                    data.append(str(person_name))
            else:
                data = film.get(field)
        except KeyError:
            data = None

        fields_data.append(data)

    url = ia.get_imdbURL(film)
    fields_data.append(url)

    return fields_data

def getHistoricalPeriodsJSON(history_terminology_json, new_filename):
    """ From history_terminology.json and the totallytimelines webscraping, 
    returns updated JSON file of historical_periods.json """

    # Gets history_terminology dictionary:
    history_terminology_path = os.path.join("./historical_periods/", history_terminology_json)
    history_terminology = get_dictionary_from_json(history_terminology_path)
    
    # Creates json file with the scraped website data & historical terminology to make periods dictionary:
    historical_dictionary = get_historical_dictionary(history_terminology)
    
    save_dictionary_as_json(historical_dictionary, "historical_periods.json")

    return new_filename




####### TESTING AREA #######

# # To test getHistoricalPeriodsJSON(history_terminology_json, new_filename):
# print(getHistoricalPeriodsJSON("history_terminology.json", "historical_periods.json"))

# To test getIMDbDataFromFields(IMDb_id, field):
# print(getIMDbDataFromFields("tt8579674", "plot", "synopsis","director","writer","cast", "cover url"))



