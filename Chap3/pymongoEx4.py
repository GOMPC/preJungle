from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbjungle 

target_movie = db.movies.find_one({'title':'매트릭스'})
print(target_movie['star'])

for movie in db.movies:
    if movie['star'] == target_movie['star']:
        print(movie['title'])