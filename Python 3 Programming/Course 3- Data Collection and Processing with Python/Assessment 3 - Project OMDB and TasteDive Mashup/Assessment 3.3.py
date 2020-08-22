#Please copy the completed functions from the two code windows above into this active code window.
#Next, you’ll write a function, called get_related_titles. It takes a list of movie titles as input.
#It gets five related movies for each from TasteDive, extracts the titles for all of them, and combines them all into a single list.
#Don’t include the same movie twice.


# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_related_titles(["Black Panther", "Captain Marvel"])
# get_related_titles([])
import requests_with_caching
import json


def get_movies_from_tastedive(title):
    endpoint = 'https://tastedive.com/api/similar'
    param = {}
    param['q'] = title
    param['limit'] = 5
    param['type'] = 'movies'

    this_page_cache = requests_with_caching.get(endpoint, params=param)
    return json.loads(this_page_cache.text)


def extract_movie_titles(dic):
    return ([i['Name'] for i in dic['Similar']['Results']])


def get_related_titles(movie_list):
    li = []
    for movie in movie_list:
        li.extend(extract_movie_titles(get_movies_from_tastedive(movie)))
    return list(set(li))


get_related_titles(["Black Panther", "Captain Marvel"])

