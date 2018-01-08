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

    def get_all_message(self):
        return self.name, self.rate, self.location, self.category, self.info_link, self.cover_link


def getMovieUrl(category, location):
    """
    return a string corresponding to the URL of douban movie lists given category and location.
    """
    req_range = "9,10"
    if location == "":
        req_tags = category
    else:
        req_tags = category + "," + location
    req_sort = "S"
    url = "https://movie.douban.com/tag/#/?sort={}&range={}&tags={},电影".format(req_sort, req_range, req_tags)
    print(url)
    return url


def getMovies(category, location):
    """
    return a list of Movie objects with the given category and location.
    """
    movies = []
    movie_url = getMovieUrl(category, location)
    html = MoviePractice.expanddouban.getHtml(movie_url, True)
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


def get_req_location():
    locations = []
    html = MoviePractice.expanddouban.getHtml("https://movie.douban.com/tag/#/")
    soup = BeautifulSoup(html, "lxml")
    html = soup.find_all("ul", class_="category")
    li_html = html[2].find_all("span", class_="tag")
    for i in range(len(li_html)):
        if i != 0:
            locations.append(li_html[i].get_text())
    return locations


def count_lb_movie(temp_req_category, all_lb_moview):
    if temp_req_category in all_lb_moview:
        all_lb_moview[temp_req_category] += 1
    else:
        all_lb_moview[temp_req_category] = 1


def count_lb_df_movie(temp_req_category, temp_req_location, all_dflb_movie):
    if (temp_req_category, temp_req_location) in all_dflb_movie:
        all_dflb_movie[(temp_req_category, temp_req_location)] += 1
    else:
        all_dflb_movie[(temp_req_category, temp_req_location)] = 1

def get_top_three(temp_sorted_key,all_dflb_movie):



# req_locations = get_req_location();
req_categorys = ["悬疑", "犯罪", "情色"]
# with open("movies.csv", "w", encoding="utf-8", newline="") as csvfile:
#     file_write = csv.writer(csvfile)
#     file_write.writerow(["name", "rate", "location", "category", "info_link", "cover_link"])
# for req_category in req_categorys:
#     for req_location in req_locations:
#         all_movie = getMovies(req_category, req_location)
#         with open("movies.csv", "a", encoding="utf-8", newline="") as csvfile:
#             file_write = csv.writer(csvfile)
#             for temp in all_movie:
#                 file_write.writerow(temp.get_all_message())
lb_movie = {}
dflb_movie = {}
with open("movies.csv", "r", encoding="utf-8") as csvfile:
    read = csv.reader(csvfile)
    read_list = list(read)
    for i in range(len(read_list)):
        if i != 0:
            temp_category = read_list[i][3]
            temp_location = read_list[i][2]
            count_lb_movie(temp_category, lb_movie)
            count_lb_df_movie(temp_category, temp_location, dflb_movie)
sorted_dflb_keys = sorted(dflb_movie, key=dflb_movie.get, reverse=True)
get_top_three(sorted_dflb_keys,dflb_movie);
