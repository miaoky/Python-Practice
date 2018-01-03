import MoviePractice.expanddouban
from bs4 import BeautifulSoup
import csv


class Movie:
    def __init__(self, name, rate, location, category, info_link, cover_link):
        self.name = name
        self.rate = rate
        self.location = location
        self.category = category
        self.info_link = info_link
        self.cover_link = cover_link


def getMovieUrl(category, location):
    """
    return a string corresponding to the URL of douban movie lists given category and location.
    """
    req_range = "9,10"
    req_tags = category + "," + location
    req_sort = "S"
    url = "https://movie.douban.com/tag/#/?sort={}&range={}&tags={}".format(req_sort, req_range, req_tags)
    return url


def getMovies(category, location):
    """
    return a list of Movie objects with the given category and location.
    """
    movies = []
    movie_url = getMovieUrl(category, location)
    html = MoviePractice.expanddouban.getHtml(movie_url)
    soup = BeautifulSoup(html, "lxml")
    all_list = soup.find_all("a", class_="item")
    for item in all_list:
        name = item.find("span", class_="title").get_text()
        rate = item.find("span", class_="rate").get_text()
        info_link = item["href"]
        cover_link = item.find("img")["src"]
        m = Movie(name, rate, location, category, info_link, cover_link)
        movies.append(m)
    return movies


req_category = "音乐"
req_location = "大陆"
all_movie = getMovies(req_category, req_location)
with open("movies.csv", "wb") as csvfile:
    file_write = csv.writer(csvfile, dialect=("excel"))
    file_write.writerow(["name", "rate", "location", "category", "info_link", "cover_link"])
    file_write.writerows(all_movie)
