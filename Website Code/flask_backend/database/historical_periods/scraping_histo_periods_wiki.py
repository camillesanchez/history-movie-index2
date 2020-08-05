from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import module_dates as md

centuries = {}

for century in range (-70,30, 1):
    centuries[century] = []
print(centuries)

wiki_url = "https://en.wikipedia.org/wiki/History_by_period"

with urlopen(wiki_url) as fn:

    soup = BeautifulSoup(fn, 'html.parser') #lxml parser?

    # print(soup.prettify())

    for section in soup.find_all("li"):
        # print(section)

        if "class" in section.attrs:
            # print(section.attrs)
            if "toclevel-1" in section.attrs['class'] or "toclevel-2" in section.attrs['class']:
                pass
        
        elif "/wiki/Category:" in section.a.attrs["href"] :
            pass

        elif "/wiki/List_of_time_periods" in section.a.attrs["href"] :
            pass

        elif section.cite:
            pass
            
        else:
            # print(section)
            # period_all = str(section.text)
            # period_name = str(section.a.text)
            # period_info = period_all.replace(period_name + " ", "")

            # print(period_name)
            # print(period_info)

            # expressions = [r"()\((\d{,4}\s{,1}\D{,3})\s\-\s(\d{,4}\s{,1}\D{,3})\)", r"\((\D+),\s(\d{,4}\s{,1}\D{,3})\s\-\s(\d{,4}\s{,1}\D{,3})\)", r"\((\D+)\s(\d{,4}\s{,1}\D{,3})\s\-\s(\d{,4}\s{,1}\D{,3})\)", r"(\D+)\s[(](\d{,4}\s{,1}\D{,3})\s\-\s(\d{,4}\s{,1}\D{,3})\)", r"\((\D+)[,]\s(\d+)–(\d+)", r"\((\D+)[,]\s(\d+)–(present)", r"()\((\d+)–(present)", r"\((\d+)[,]\s(\d+th century)\s–\s(\d+th century)"]

            # for expression in expressions:

            #     match = re.search(expression, period_info)

            #     if match:
            #         print(expression)
            #         period_location = match.group(1).strip()
            #         period_start_date = match.group(2).strip()
            #         period_end_date = match.group(3).strip()
            #         print(period_location)
            #         print(period_start_date)
            #         print(period_end_date)


            #         dates = [period_start_date, period_end_date]
            #         formatted_dates = md.formatting_dates(dates)
            #         century_list = md.get_century(formatted_dates)
            #         updated_century_dict = md.add_dates_to_dictionary(centuries, century_list, period_name, period_location, formatted_dates)
                # else:
                #     print("no match")
            data = md.get_location_start_and_end_dates(section)
            print(data)


        print()

    print("done")
    print(centuries)



