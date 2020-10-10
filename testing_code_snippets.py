from tmdbv3api import TMDb
from tmdbv3api import Movie
from tmdbv3api import Person
import time
import ast
import pandas as pd
from ast import literal_eval

tmdb = TMDb()
tmdb.api_key = '56e6a88a9d6e60e1610f8821d326ff9e'

tmdb.language = 'en'
#tmdb.debug = True

movie = Movie()

lista = []


smd = pd.read_csv('/home/axg/Desktop/project1/p4/Movie_recommendation_engine/test_dataset/ml-latest-small/test_output/mars/credits/credits_test.csv')
#smd['cast'] = smd['cast'].apply(literal_eval)
#print(str(type(smd['cast'][0])))s
#smd['cast'] = ((smd['cast'][0].decode('utf-8')).encode("ascii","ignore")).apply(literal_eval)


smdn = pd.read_csv('/home/axg/Desktop/project1/p4/Movie_recommendation_engine/test_dataset/ml-latest-small/ctest.csv')
#print(smdn)
smdn['cast'] = smdn['cast'].apply(literal_eval)
print(smdn['cast'][0][0]['name'])

id_list = []
keywords_list = []

'''m = movie.details(862.0)
if hasattr(m,'id') or hasattr(m,'keywords'):
  id_list.append(m.id)
  print str(m.keywords['keywords'][0]['id'])+str(type(m.keywords['keywords'][0]))
  #keywords_list.append((m.keywords['keywords'].decode('utf-8')).encode("ascii","ignore"))
'''


smd = pd.read_csv('/home/axg/Desktop/project1/p4/Movie_recommendation_engine/test_dataset/ml-latest-small/test_output/mars/keywords/2/keywords394.csv')
for i in range(0,len(smd['keywords'])):
  smd['keywords'][i] = smd['keywords'][i].decode('utf-8').encode("ascii","ignore")

smd['keywords'] = smd['keywords'].apply(literal_eval)
print(smd['keywords'][0][0]['name'])

'''smdn = pd.read_csv('/home/axg/Desktop/project1/p4/Movie_recommendation_engine/test_dataset/ml-latest-small/ctest.csv')
print(smdn)
smdn['cast'] = smdn['cast'].apply(literal_eval)
print(smdn['cast'][0][0]['name'])'''