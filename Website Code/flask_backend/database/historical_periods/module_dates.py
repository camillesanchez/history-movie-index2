from bs4 import BeautifulSoup
from datetime import date
from urllib.request import Request, urlopen
import re

def check_location_exists(period_location):

    location_list = additional_location_specific_to_wikipedia_page()

    if period_location in location_list:
        return period_location
    else:
        pass
        "NEED TO WRITE SPECIFIC CODE"

def additional_location_specific_to_wikipedia_page():

    world_country_list = scrapping_country_list()

    location_terminology = world_country_list

    additional_location_terminology = ["allied states", "Russia and other former Soviet States","Soviet Union", "Western World", "Europe", "Southeast Europe", "Middle East", "Mediterranean Sea", "England", "Earth", "Much of Earth"]

    for term in additional_location_terminology:
        location_terminology.append(term)

    return location_terminology

def scrapping_country_list():
    """Create World Country List by scrapping the web """

    world_country_list = []

    url = "https://www.worldometers.info/geography/alphabetical-list-of-countries/"
    req = Request(url, headers = {"User-Agent": "Mozilla/5.0"})
    with urlopen(req) as fn:

        soup = BeautifulSoup(fn, 'html.parser') #lxml parser?

        for section in soup.find_all("td"):
            try:
                if section["style"] == "font-weight: bold; font-size:15px":
                    country = section.text
                    world_country_list.append(country)
            except:
                pass

        return world_country_list
                
def formatting_dates(dates_list):
    """ Formatting of both the start and end dates of a historical period.
    dates = [period_start_date, period_end_date]"""

    new_dates = dates_list

    # Change all "BCE" into "BC":
    for index1 in range(len(new_dates)):       
        if " BCE" not in new_dates[index1]:
            if " BC" in new_dates[index1]:
                new_dates[index1] = str(new_dates[index1]) + "E"

    counter = 0

     # Change "present" into today's year:
    if "present" in new_dates[counter +1]:
        new_dates[counter +1] = str(date.today())[:-6]

    if "th century" in new_dates[counter]:
        pass
    
    # Adding Missing " BCE" and " CE":
    elif " CE" not in new_dates[counter] and " CE" not in new_dates[counter +1]:
        # Both dates "Before Common Era" - Add "BCE" if start date higher number than end date:
        if "BCE" not in new_dates[counter] and "BCE" in new_dates[counter +1]: 
            if int(new_dates[counter]) >= int(new_dates[counter+1][:-3]):
                new_dates[counter] = str(new_dates[counter]) + " BCE"
            else:
                print("Not a valid date.") #  PRINT ERROR

        # Both dates "Before Common Era" - Add "BCE" if start date higher number than end date:
        elif "BCE" in new_dates[counter] and "BCE" not in new_dates[counter +1]: 
            if int(new_dates[counter][:-3]) >= int(new_dates[counter+1]):
                new_dates[counter +1] = str(new_dates[counter +1]) + " BCE"
            else:
                print("Not a valid date, except if end date is CE.") #  PRINT ERROR

        elif "BCE" not in new_dates[counter] and "BCE" not in new_dates[counter +1]: 
            # Both dates "Before Common Era" - Add "BCE" if start date higher number than end date:
            if int(new_dates[counter]) >= int(new_dates[counter+1]):
                new_dates[counter] = str(new_dates[counter]) + " BCE"
                new_dates[counter+1] = str(new_dates[counter+1]) + " BCE"
            
            # Both dates "Common Era"
            else:
                new_dates[counter] = str(new_dates[counter]) + " CE"
                new_dates[counter+1] = str(new_dates[counter+1]) + " CE"
    
    # One date "Before Common Era" and one date "Common Era"
    elif " BCE" in new_dates[counter] and " CE" in new_dates[counter +1]:
        pass

    return new_dates

def get_century(dates_list):
    """ Get the Century from both start and end dates. 
    dates = [period_start_date, period_end_date] """

    centuries = []

    for date in dates_list:
    
        if " BCE" in date:
            century = int(date[:-4][:-2]) + 1
            centuries.append(-century)

        elif " CE" in date:
            century = int(date[:-3][:-2]) + 1
            centuries.append(century)

        elif "th century" in date:
            century = date[:-10]
            centuries.append(century)

    return centuries

def add_dates_to_dictionary(dictionary, century_list, period_name, period_location, formatted_dates):
    """ Add dates to dictionary """
    
    inside_dict = {}
    inside_dict["period"] = period_name
    inside_dict["start_date"] = formatted_dates[0]
    inside_dict["end_date"] = formatted_dates[1]
    inside_dict["location"] = period_location

    if century_list[0] == century_list[1]:                      # same century
        dictionary[century_list[0]].append(inside_dict)

    elif century_list[0] != century_list[1]:
        if int(century_list[0]) > int(century_list[1]):         # "BCE" - Before Common Erea
            for every_century in range(- int(century_list[0]), - int(century_list[1])+1, 1):
                dictionary[every_century].append(inside_dict)

        elif int(century_list[0]) < int(century_list[1]):       # "CE" - Common Era
            for every_century in range(int(century_list[0]), int(century_list[1])+1, 1):
                dictionary[every_century].append(inside_dict)

    return dictionary

def get_location_start_and_end_dates(section):
    """Using regular expressions, get the location, start date and end date of the time period. """

    print(section)
    period_all = str(section.text)
    period_name = str(section.a.text)
    period_info = period_all.replace(period_name + " ", "")

    print(period_name)
    print(period_info)

    expressions = [ r"()[between]{7}\s(\d{0,6})\s[and]{3}\s(\d{0,6}\s\D{3})",  
                    r"()\((\d{,4}\s{,1}\D{,3})\s\-\s(\d{,4}\s{,1}\D{,3})\)", 
                    r"(\D+)\s\((\d{0,6}\s{0,1}\D{0,3})\s[-]{1}\s(\d{0,6}\s{0,1}\D{0,3})\)",
                    r"\((\D+),\s(\d{,4}\s{,1}\D{,3})\s\-\s(\d{,4}\s{,1}\D{,3})\)", 
                    r"\((\D+)\s(\d{,4}\s{,1}\D{,3})\s\-\s(\d{,4}\s{,1}\D{,3})\)",

                    r"\((\D+)\s(\d{,4}[th century])\s\-\s(\d{,4}[th century])\)",

                    r"\D{0,8}\s{0,1}\((\D{0,6}),\s(\d{0,5}\s{0,1}\D{0,3})\s\-\s(\d{0,4}\s{0,1}\D{0,3})\)",

                    r"(\D+)\s[(](\d{,4}\s{,1}\D{,3})\s\-\s(\d{,4}\s{,1}\D{,3})\)", 
                    r"\((\D+)[,]\s(\d+)–(\d+)", r"\((\D+)[,]\s(\d+)–(present)", 
                    r"()\((\d+)–(present)", r"\((\d+)[,]\s(\d+th century)\s–\s(\d+th century)"]

    """
    Expressions equivalencies (in order):

        between date and date
        (date - date)
        country (date - date)
        (country, date - date)
        (country date - date)
        (country, date th century - date th century)

        text (country, date - date)

    """
    for expression in expressions:

        match = re.search(expression, period_info)
        print(expression)

        if period_name == period_info:
            print("no data")

        elif match:
            print("matched", expression, period_info)
            period_location = match.group(1).strip()
            period_start_date = match.group(2).strip()
            period_end_date = match.group(3).strip()
            print(period_location)
            print(period_start_date)
            print(period_end_date)

            dates = [period_start_date, period_end_date]

            return [period_location, dates]

        else:
            print("no match")
            if expression == expressions[-1]:
                print(ValueError(section))



centuries = {}

for century in range (-70,30, 1):
    centuries[century] = []

dates = ["1930", "present"]
period_name = "French Third Republic"
period_location = "France"

# check_location_exists(period_location)

# formatted_dates = formatting_dates(dates)
# print(formatted_dates)
# century_list = get_century(formatted_dates)
# print(century_list)
# updated_century_dict = add_dates_to_dictionary(centuries, century_list, period_name, period_location, formatted_dates)
# print(updated_century_dict)

