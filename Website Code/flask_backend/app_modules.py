from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import math

def formatsFilmRuntime(runtime):
    """ Formats Film runtime for Web app template. """

    if runtime != None:
        number_hours = math.floor(int(runtime)/60)
        number_minutes = math.floor(int(runtime) - (number_hours * 60))
        if number_minutes < 10:
            number_minutes = f"0{number_minutes}"

        if number_hours ==0:
            film_runtime = f"{number_minutes}min"
        elif number_minutes == 0:
            film_runtime = f"{number_hours}h"
        else:
            film_runtime = f"{number_hours}h{number_minutes}min"
    else:
        film_runtime = "Unknown"
    return film_runtime

def formatsGenres(genres_list):
    """ Formats Genres for Web app template. """
    
    genres = ""
    try:
        for item in genres_list:
            print(item.genre_type)
    except:
        genres = "Unknown"
    else:
        for genre in genres_list:
            print(genre, genres_list[-1])
            if len(genres_list) == 1 or genre == genres_list[-2]:
                genres = genre.genre_type
            elif genre != genres_list[-2] and genre != genres_list[-1]:
                genres += genre.genre_type + ", "
            elif genre == genres_list[-1]:
                genres += " & " + genre.genre_type
    return genres

def formatsDirectorsField(directors_list):
    """ Formats Directors field for Web app template. """

    film_directors=""
    if directors_list != None:
        for director in directors_list:
            if len(directors_list) == 1 or director == directors_list[-2]:
                film_directors = director
            elif director != directors_list[-1] and director != directors_list[-2]:
                film_directors += director + ", "
            elif director == directors_list[-1]:
                film_directors += " & " + director
    else:
        film_directors = "Unknown"
    return film_directors

def formatsWritersField(writers_list):
    """ Formats Writers field for Web app template. """
    
    film_writers=""
    if writers_list != None:
        for writer in writers_list:
            if len(writers_list) == 1 or writer == writers_list[-2]:
                film_writers = writer
            elif writer != writers_list[-1] and writer != writers_list[-2]:
                film_writers += writer + ", "
            elif writer == writers_list[-1]:
                film_writers += " & " + writer 
    else:
        film_writers = "Unknown"
    return film_writers

def getsTrailerUrl(imdb_url):
    """ Returns IMDb trailer link from imdb_url """

    req = Request(imdb_url, headers = {"User-Agent": "Mozilla/5.0"})

    with urlopen(req) as fn:

        soup = BeautifulSoup(fn, 'html.parser') #lxml parser?

        # print(soup.prettify())

        video_section = soup.find("div", class_= "slate")
        try:
            link = video_section.a
        except:
            return None
        else:
            video_link = link.get('href')
            full_video_link = "https://www.imdb.com" + video_link
            return full_video_link