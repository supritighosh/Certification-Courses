#Your next task will be to fetch data from OMDB. The documentation for the API is at https://www.omdbapi.com/
#Define a function called get_movie_data. It takes in one parameter which is a string that should represent the title of a movie you want to search.
#The function should return a dictionary with information about that movie.
#Again, use requests_with_caching.get(). For the queries on movies that are already in the cache, you won’t need an api key.
#You will need to provide the following keys: t and r.
#As with the TasteDive cache, be sure to only include those two parameters in order to extract existing data from the cache.


# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_data("Venom")
# get_movie_data("Baby Mama")
import requests_with_caching
import json


def get_movie_data(title):
    endpoint = 'http://www.omdbapi.com/'
    param = {}
    param['t'] = title
    param['r'] = 'json'
    this_page_cache = requests_with_caching.get(endpoint, params=param)

    return json.loads(this_page_cache.text)


get_movie_data("Venom")
get_movie_data("Baby Mama")

