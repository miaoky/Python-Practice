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
    for k in range(len(li_html)):
        if k != 0:
            locations.append(li_html[k].get_text())
    return locations


def get_lb_df_dict(temp_req_location, temp_req_category, temp_dflb_movie):
    if temp_req_category not in temp_dflb_movie:
        temp_dflb_movie[temp_req_category] = {}
        get_dict_movie(temp_req_location, temp_dflb_movie[temp_req_category])
    else:
        get_dict_movie(temp_req_location, temp_dflb_movie[temp_req_category])


def get_dict_movie(temp_req_location, temp_df_movie):
    if temp_req_location not in temp_df_movie:
        temp_df_movie[temp_req_location] = 1
    else:
        temp_df_movie[temp_req_location] += 1


def get_lb_top_movie(temp_dflb_movie, temp_lb_top_movie):
    for lb in temp_dflb_movie:
        sort_list = sorted(temp_dflb_movie[lb], key=temp_dflb_movie[lb].get, reverse=True)
        end_index = 3
        if len(sort_list) <= 3:
            end_index = len(sort_list)
        else:
            while (end_index + 1 <= len(sort_list)
                   and temp_dflb_movie[lb][sort_list[end_index - 1]] == temp_dflb_movie[lb][sort_list[end_index]]):
                end_index += 1
        temp_lb_top_movie[lb] = sort_list[:end_index]


req_locations = get_req_location();
req_categorys = ["悬疑", "犯罪", "情色"]
with open("movies.csv", "w", encoding="utf-8", newline="") as csvfile:
    file_write = csv.writer(csvfile)
    file_write.writerow(["name", "rate", "location", "category", "info_link", "cover_link"])
for req_category in req_categorys:
    for req_location in req_locations:
        all_movie = getMovies(req_category, req_location)
        with open("movies.csv", "a", encoding="utf-8", newline="") as csvfile:
            file_write = csv.writer(csvfile)
            for temp in all_movie:
                file_write.writerow(temp.get_all_message())
dflb_movie = {}
lb_movie = {}
lb_top_movie = {}
with open("movies.csv", "r", encoding="utf-8") as csvfile:
    read = csv.reader(csvfile)
    read_list = list(read)
    for i in range(len(read_list)):
        if i != 0:
            temp_category = read_list[i][3]
            temp_location = read_list[i][2]
            get_lb_df_dict(temp_location, temp_category, dflb_movie)
            get_dict_movie(temp_category, lb_movie)
get_lb_top_movie(dflb_movie, lb_top_movie)
with open("output.txt", "w", encoding="utf-8", newline="") as outputfile:
    for k in req_categorys:
        out_text = k+' '
        for top_df in lb_top_movie[k]:
            out_text += top_df + ' ' + str(round(dflb_movie[k][top_df] / lb_movie[k] * 100, 2)) + '% '
        outputfile.writelines(out_text+'\n')
