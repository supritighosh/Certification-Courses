#Please copy the completed function from above into this active code window. Now write a function called get_movie_rating.
#It takes an OMDB dictionary result for one movie and extracts the Rotten Tomatoes rating as an integer.
#For example, if given the OMDB dictionary for “Black Panther”, it would return 97. If there is no Rotten Tomatoes rating, return 0.


# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_rating(get_movie_data("Deadpool 2"))
import requests_with_caching
import json


def get_movie_data(title):
    endpoint = 'http://www.omdbapi.com/'
    param = {}
    param['t'] = title
    param['r'] = 'json'
    this_page_cache = requests_with_caching.get(endpoint, params=param)
    return json.loads(this_page_cache.text)
print(get_movie_data("Black Panther")['Ratings'][1])
def get_movie_rating(dic):
    ranking = dic['Ratings']
    for dic_item in ranking:
        if dic_item['Source'] == 'Rotten Tomatoes':
            return int(dic_item['Value'][:-1])
    return 0


get_movie_rating(get_movie_data("Deadpool 2"))