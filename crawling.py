import requests
from bs4 import BeautifulSoup
import re

def get_movie_link(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html5lib')

    movie_links = soup.select('a[href]')

    movie_links_list = []
    for link in movie_links:
        if re.search(r'st=mcode&sword' and r'&target=after', link['href']):
            target_url = r'http://movie.naver.com/movie/point/af/list.nhn'+str(link['href'])
            movie_links_list.append(target_url)

    return movie_links_list

# url = 'http://movie.naver.com/movie/point/af/list.nhn'
# movie_links = get_movie_link(url)
# print(movie_links)
