from tmdbv3api import TMDb
from tmdbv3api import Movie
from tmdbv3api import Person
import time
import pandas as pd

tmdb = TMDb()
tmdb.api_key = '56e6a88a9d6e60e1610f8821d326ff9e'

tmdb.language = 'en'
#tmdb.debug = True

movie = Movie()
latest_id = 5
#print(m)
#m = movie.latest()
'''if m:
  print(m.title)
  print(m.adult)
  print(m.belongs_to_collection)
  print(m.budget)
  print(m.genres)                                  #print(m.genres[0]['name'])
  print(m.homepage)
  print(m.id)
  print(m.imdb_id)
  print(m.original_language)
  print(m.original_title)
  print(m.overview)
  print(m.popularity)
  print(m.poster_path)
  print(m.production_companies)
  print(m.release_date)
  print(m.revenue)
  print(m.runtime)
  print(m.spoken_languages)
  print(m.status)
  print(m.tagline)
  print(m.title)
  print(m.video)
  print(m.vote_average)
  print(m.vote_count)'''

#person = Person()
#p = person.details(1223786)
#print(p.name)
columns = ['adult', 'belongs_to_collection', 'budget', 'genres', 'homepage', 'id', 'imdb_id', 'original_language', 'original_title', 'overview', 'popularity', 'poster_path', 'production_companies', 'production_countries', 'release_date', 'revenue', 'runtime', 'spoken_languages', 'status', 'tagline', 'title', 'video', 'vote_average', 'vote_count']
adult_list = []
belongs_to_collection_list = []
budget_list = []
genres_list = []
homepage_list = []
id_list = []
imdb_id_list = []
original_language_list = []
original_title_list = []
overview_list = []
popularity_list = []
poster_path_list = []
production_companies_list = []
production_countries_list = []
release_date_list = []
revenue_list = []
runtime_list = []
spoken_languages_list = []
status_list = []
tagline_list = []
title_list = []
video_list = []
vote_average_list = []
vote_count_list = []

df1 = pandas.read_csv('movies.csv')
#adult = belongs_to_collection = budget = genres = homepage = id = imdb_id = original_language = original_title = overview = popularity = poster_path = production_companies = production_countries = release_date = revenue = runtime = spoken_languages = status = tagline = title = video = vote_average = vote_count = []
#for j in range(0,4):
#    for i in range(j*37,j*37+37):
for i in range(0,20):
  m = movie.details(df1[movieId][i])
  if hasattr(m,'adult'):
    adult_list.append(m.adult)
    belongs_to_collection_list.append(m.belongs_to_collection)
    budget_list.append(m.budget)
    genres_list.append(m.genres)
    homepage_list.append(m.homepage)
    id_list.append(m.id)
    imdb_id_list.append(m.imdb_id)
    original_language_list.append(m.original_language)
    original_title_list.append(m.original_title)
    overview_list.append(m.overview)
    popularity_list.append(m.popularity)
    poster_path_list.append(m.poster_path)
    production_companies_list.append(m.production_companies)
    production_countries_list.append(m.production_countries)
    release_date_list.append(m.release_date)
    revenue_list.append(m.revenue)
    runtime_list.append(m.runtime)
    spoken_languages_list.append(m.spoken_languages)
    status_list.append(m.status)
    tagline_list.append(m.tagline)
    title_list.append(m.title)
    video_list.append(m.video)
    vote_average_list.append(m.vote_average)
    vote_count_list.append(m.vote_count)
#time.sleep(8)     

#data = list(zip(adult,belongs_to_collection,budget,genres,homepage,id,imdb_id,original_language,original_title,overview,popularity,poster_path,production_companies,production_countries,release_date,revenue,runtime,spoken_languages,status,tagline,title,video,vote_average,vote_count))
data = list(zip(adult_list,belongs_to_collection_list,budget_list,genres_list,homepage_list,id_list,imdb_id_list,original_language_list,original_title_list,overview_list,popularity_list,poster_path_list,production_companies_list,production_countries_list,release_date_list,revenue_list,runtime_list,spoken_languages_list,status_list,tagline_list,title_list,video_list,vote_average_list,vote_count_list))

df = pd.DataFrame(data,columns=columns)
df.to_csv('1.csv',index = False)

