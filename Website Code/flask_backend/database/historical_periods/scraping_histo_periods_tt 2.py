from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import historical_periods.module_dates as md
from historical_periods.history_terminology_dictionary import getHistoricalTerminologyDict
from datetime import date
import json

def formatting_dates_for_dictionary(row):
    """Formatting dates to be a list with both start and end dates of the time period. 
    dates = [start date, end date ] """

    dates = row.text.split(" – ")
    for item in dates:
        if item[-2:] != "CE" and item[-3:] != "ago": # Remove undesired HTML tags
            if item[5:7] == "BC":
                dates[1] = item[:8]
            else:
                dates[1] = item[:7]
    if dates[1] == "Present":
        dates[1] = str(date.today())[:-6] + " CE"

    return dates

def get_historical_dictionary(history_terminology):

    """Scrape the historical time periods from website.

    {1:     {'period_name': 'ABC', 
            'dates': ['start date', 'end date'], 
            'sub-periods:   {1:     {'sub-period_name': 'abc', 
                                    'period_location': 'abc',
                                    'dates': ['start date', 'end date']},
                            2:      {...}
                            }
            },
    2:      {...}
    }
    """

    periods = {}

    url = "https://www.totallytimelines.com/historical-time-periods/"

    req = Request(url, headers = {"User-Agent": "Mozilla/5.0"})

    with urlopen(req) as fn:

        soup = BeautifulSoup(fn, 'html.parser') #lxml parser?

        # print(soup.prettify())

        table = soup.find("div", class_= "timeline-container")
        rows = table.find_all("div")

        counter = 0
        subperiod_counter = 0
        for row in rows:

            # Get all the period headers:
            if row.attrs["class"] == ["timeline-heading"]:

                counter += 1
                subperiod_counter = 0
                if row.text[-1] == "–":
                    period_heading_name = str(row.text)+ " " + str(date.today())[:-6] + " CE"
                    p_list = period_heading_name.split(" – ")
                else:
                    p_list = str(row.text).split(" – ")

                inside_dict = {}
                inside_dict["period_name"] = p_list[0]
                inside_dict["dates"] = [p_list[1], p_list[2]]
                inside_dict["sub-periods"] = {}
            
                periods[counter] = inside_dict

            # Get all the period sub-headers' name:
            elif row.attrs["class"] == ["timeline-date"]:
                subperiod_counter += 1
                data_dict = {}
                data_dict["sub-period_name"] = row.text

                periods[counter]["sub-periods"][subperiod_counter] = data_dict

            # Get all the period sub-headers' locations:
            elif row.attrs["class"] == ["timeline-subheading"]:
                periods[counter]["sub-periods"][subperiod_counter]["period_location"] = row.text

            # Get all the period sub-headers' dates:
            elif row.attrs["class"] == ["timeline-details"]:
                dates = formatting_dates_for_dictionary(row)
                periods[counter]["sub-periods"][subperiod_counter]["dates"] = dates

            # Adding keywords for each sub-header:
                subperiod_name = periods[counter]["sub-periods"][subperiod_counter]["sub-period_name"]
                keywords = history_terminology[subperiod_name]
                periods[counter]["sub-periods"][subperiod_counter]["keywords"] = keywords

        return periods

def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError

def save_dictionary_as_json(dictionary, filename):
    """Save the dictionnary as json file"""

    json_f = json.dumps(dictionary, default= set_default, indent = 4)
    f = open(filename, "w")
    f.write(json_f)
    f.close()

    print(f"\n{filename} was created.\n")
    
def get_dictionary_from_json(filename):
    """ Returns dictionary from Json file"""

    f = open(filename, "r")
    data = json.load(f)

    f.close()

    return data


####### TESTING AREA #######

# # Create json file with history_terminology dictionary
# save_dictionary_as_json(getHistoricalTerminologyDict(), "history_terminology.json")

## Create json file with periods dictionary:
# history_terminology = get_dictionary_from_json("history_terminology.json")
# historical_dictionary = get_historical_dictionary(history_terminology)
# print(historical_dictionary)
# save_dictionary_as_json(historical_dictionary, "historical_periods.json")

## Get periods dictionary:
# periods = get_dictionary_from_json("historical_periods.json")



