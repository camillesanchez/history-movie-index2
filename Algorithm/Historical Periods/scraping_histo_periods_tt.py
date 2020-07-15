from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import module_dates as md
from datetime import date

history_terminology = {
    "Stone Age": {"prehistoric", "Stone Age"},
    "Ancient Mesopotamia": {},

    "Bronze Age": {},
    "Old Kingdom": {},
    "Indus Valley Civilisation": {},
    "Middle Kingdom": {},
    "Shang Dynasty": {},
    "New Kingdom": {},
    "Vedic Period": {}, 
    "Zhou Dynasty": {}, 
    "Iron Age": {}, 
    "Ancient Greece": {}, 
    "Jomon Period": {}, 
    "Mahajanpadas": {}, 
    "Ancient Rome": {}, 
    "Mayan Civilisation": {}, 
    "Yayoi Period": {}, 
    "Moche Civilisation": {}, 
    "Coptic Period": {},

    "Kofun Period": {}, 
    "Gupta Empire": {}, 
    "Anglo Saxon Period": {},

    "Srivijaya Period": {}, 
    "Chenla Kingdom": {}, 
    "Kingdom of the Sunda": {}, 
    "Golden Age of Islam": {}, 
    "Nara Period": {}, 
    "Pala Empire": {}, 
    "Kingdom of Mataram": {}, 
    "Viking Age": {}, 
    "Khmer Empire": {}, 
    "Chimu Culture": {}, 
    "Medieval Period": {},
    "Kediri Empire": {}, 
    "Ottoman Empire": {},  
    "Renaissance": {}, 
    "Age of Discovery": {}, 
    "Sengoku Period": {}, 
    "Aztec Empire": {}, 
    "Inca Empire": {}, 
    "Tudor Period": {},

    "Reformation": {},
    "Mughal Empire": {}, 
    "Elizabethan Age": {},
    "Stuart Period": {"Stuart Period", "House of Stuart", "Jacobites", "Gunpowder Plot", "Immortal Seven", "Act of Union", "United Kingdom", "War of the Spanish Succession", "Treaty of Utrecht", "English Act of Settlement", "Act of Settlement", "James Francis Edward Stuart", "Nine Years’ War", "Treaty of Ryswick", "Battle of the Boyne", "William of Orange", "Anglo-Dutch War", "Bloody Assizes", "George Villiers", "Short Parliament", "Long Parliament", "William Laud", "Battle of Sedgemoo", "Berwick", "Monmouth", "Pacification of Berwick", "First Anglo-Dutch War", "Second English Civil War", "Grand Remonstrance", "Thomas Wentworth", "personal rule", "Felton", "Great Britain", "Jacobean era", "James VI", "James VI of Scotland", "Caroline era", "Great Fire of London", "Whigs", "Monmouth Rebellion", "Rye House Plot", "Titus Oates", "Exclusion Crisis",  "Mary of Modena", "Aphra Behn", "Second Anglo-Dutch War", "Third Anglo-Dutch War", "Catherine of Braganza", "Book of Common Prayer", "Act of Uniformity", "Restoration", "declaration of Breda", "James I", "Richard Cromwell", "James I of England", "Charles I", "Charles II", "James II", "Mary II", "William III", "Queen Anne", "English Civil War", "Revolution of 1688", "Glorious Revolution"}, 
    "Tokugawa Shogunate": {}, 
    "Age of Enlightenment": {}, 
    "Industrial Revolution": {}, 
    "Georgian Period": {}, 
    "Victorian Age": {}, 
    "Edwardian Period": {}, 
    "World War One": {"Verdun", "First Battle of the Marne", "Western Front", "Eastern Front", "Alpine Front", "Treaty of Brest-Litvosk", "Balkans Theater", "Triple Entente", "Triple Alliance", "World War One", "WWI", "WW1", "world war", "Armistice of 11 November 1918", "Second Battle of the Marne", "tranchée", "Battle of Somme", "Second Battle of Somme", "Battle of Verdun", "Paris Peace Conference", "Armistice of Compiègne","Versailles Treaty"}, 
    "Inter War Years": {"Années Folles", "Washinfton Naval Treaty", "Women's suffrage", "Golden Twenties", "Francisco Franco", "Franco", "Weimar Republic", "Spanish Civil Wat", "Interwar period", "interwar", "between the wars", "October Revolution", "Chinese Civil War", "Great October Socialist Revolution", "Russian Civil War", "fascism", "roaring twenties", "Great Depression", "Vladimir Lennin", "Lenin", "Joseph Stalin", "Stalin", "USSR", "labor camp", "forced-labor", "POW", "Gulag", "Great Purge"}, 
    "World War Two": {"Munich Agreement", "Munich Betrayal", "German Reich", "Third Reich", "Charles de Gaulle", "Free France", "de Gaulle", "Philippe Pétain", "Pétain", "Marshal Pétain", "World War II", "POW", "Second World War", "WWII", "WW2", "World War Two", "German Army", "fascism", "world war", "Allies", "Axis", "total war", "Axis powers", "Allies powers", "death marches", "conflict", "Genocide", "Guadalcanal campaign", "collaborators", "deported", "deportation", "racial segregation","SS", "Schutzstaffel", "Final Solution", "Final Solution to the Jewish Question", "Nazi Party", "death squads", "forced-labor camp", "prisonners of war", "Great Patriotic War", "katorga", "forced-labor", "Gulag", "Wannsee Conference", "Jews", "Nazi Germany", "Nazi", "Gestapo", "IG Farben", "Mengele", "Josef Mengele", "Himmler", "Dachau", "Monowitz", "subcamp", "forced labor", "Anschluss", "Zyklon B", "Anschluss Osterreichs", "Kristallnacht", "Night of Broken Glass", "November Pogrom", "ghettos", "November Pogroms", "Nazi boycott", "Enabling Act", "Operation Watchtower", "Operation Neptune", "invasions", "German-occupied France", "Normandy landings", "Normandy", "Battle of Stalingrad", "concentration camp", "extermination camp", "Aktion 14f13", "Action 14f13", "gas chambers", "Gross-Rosen", "staellite camp", "Neuengamme", "Natzweiler", "Gau Baden", "Auschwitz", "Buchenwald", "Operation Himmler", "Flossenbürg", "Ravensbrück", "Great Depression", "Mauthausen", "Sachsenhausen-Oranienburg", "Sachsenhausen", "work camp", "kapo", "Heinrich Himmler", "Battle of Kursk", "Operation Overlord", "Battle of Dunkirk", "Dunkirk", "Battle of Monte Cassino", "Battle of Moscow", "Battle of Philippine Sea", "Operation Market Garden", "Battle of Hurtgen Forest", "Battle of Crete", "Battle of Anzio", "Battle of Leyte Gulf", "Battle of Bulge", "Battle of Okinawa", "Western Allied Invasion of Germany", "Allied Invasion", "Hiroshima", "Nuremberg Trials", "Proclamation Defining Terms of Japanese Surrender", "Battle of Berlin", "Fall of Berlin", "Berlin Strategic Offensive Operation", "V-day", "Victory Day", "Potsdam Declaration", "Operation Downfall", "Nuremberg", "Nagasaki", "Western Allied Invasion", "Stalingrad", "Stalin", "Joseph Stalin", "Churchill", "Winston Churchill", "Hirohito", "Mussolini", "Benito Mussolini", "Chiang Kai-shek", "Kai-shek", "Franklin Roosevelt", "Franklin D. Roosevelt", "Roosevelt", "Battle of Guadalcanal", "Holocaust", "Shoah", "The Shoah", "air warfare", "warfare", "bombing", "Battle of France", "Operation Barbarossa", "Eastern Front", "Wehrmacht", "Attrition warfare", "Malaya", "Battle of Midway", "Battle of the Coral Sea", "Japanese Invasion of Malaya", "Attack of Pearl Harbor", "Attack on Pearl Harbor", "Pearl Harbor", "Hitler", "Adolf Hitler", "Western Front", "fall of France", "startegic bombic", "terror bombing", "invasion", "Poland", "Invasion of Poland", "Molotov–Ribbentrop Pact", "Battle of the Atlantic", "Blitz", "Battle of Britain", "Balkans Campaign", "Balkans", "occupation", "occupation of Baltic states"}, 
    "Atomic Age": {"Atomic era", "atomic age", "AEC", "united states Atomic energy commission", "nuclear warfare", "trinity test", "the gadget", "Hiroshima", "Nagasaki", "Atomic energy commission", "chernobyl", "chernobyl disaster", "dirty bombs", "anti-nuclear movement", "three mile island accident", "nuclear meltdown", "nuclear arms race", "Nevada Test Site", "Fukushima", "Fukushima I Nuclear Power Plant", "Tōhoku earthquake", "START I", "START I treaty", "New START", "New START treaty", "GPM", "Great Peace March for Global Nuclear Disarmament"},
    "Cold War Period": {"Trente Glorieuses", "Cold War", "Black Sea Bumping incident", "USS Yorktown", "Soviet Bloc", "Socialist Bloc", "Bezzavetny", "Fall of Berlin Wall", "Berlin Wall", "Mikhail Gorbachev", "NATO", "USSR", "OTAN", "North Atlantic Treaty", "Chinese Civil War", "Suez Crisis", "Soviet–Afghan War", "Second Arab-Israeli War", "Prague Spring", "Decolonization", "Decolonization of Africa", "Korean War", "Vietnam war", "Second Indochina War", "Washington Treaty", "Russia", "Berlin Blockade", "glasnost", "perestroika", "Fall of Nations", "Communist Bloc", "Iron Curtain", "Capitalist Bloc", "Automn of Nations","August Coup", "August Coup of 1991", "revolutions of 1989", "Fall of Communism", "Operation Danube", "Strategic Arms Limitation Talks", "SALT I", "SALT II", "People's Republic of China", "Cuban Missile Crisis", "Missile Scare", "Sino-Soviet split", "Caribbean Crisis", "October Crisis of 1962", "Berlin Crisis of 1961", "Containment", "Warsaw Pact", "liberal democratic", "democratic", "Communist Party", "communist", "cold war period", "Soviet Union", "Eastern Bloc", "United States", "Western Bloc", "Truman Doctrine", "Reagan doctrine", "Era of Stagnation", "Reagan", "Truman", "Dissolution of Soviet Union"}, 
    "Space Age": {"Space Age", "Space Race", "Space Exploration", "Sputnik 1", "Space Technology", "Apollo program", "Apollo 11", "Space Shuttle Challenger", "Space Shuttle Challenger disaster", "Challenger", "Challenger disaster", "Space Shuttle", "NASA", "International Space station", "ISS", "Ansari X Prize", "Space Ship One", "SpaceX", "private spaceflight"}, 
    "Age of Information": {"Age of Information", "Information Age", "Computer Age", "Digital Age", "New Media Age", "United Nations Public Administration Network", "innovations", "computers", "data"}
}


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

        print(periods)

        return periods

get_historical_dictionary(history_terminology)
