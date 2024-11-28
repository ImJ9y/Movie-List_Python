import collections

import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
movie_website = response.text

soup = BeautifulSoup(movie_website, "html.parser")
movies = soup.find_all(name = "h3", class_="title")

movie_rank = []

for movie in movies:
    rank = movie.getText()
    movie_rank.append(rank)

new_movieList = collections.deque()
for movie in movie_rank:
    new_movieList.appendleft(movie)

with open("movies.txt", mode = 'w') as file:
    for rank in new_movieList:
        file.write(rank + "\n")






