from bs4 import BeautifulSoup
import requests


class MangaChapter:

    def __init__(self, url) -> None:
        self.url = url
        self.__response_object = requests.get(self.url, timeout=10)
        self.chapter_id = self.__get_ch_id()

    def __get_ch_id(self):
        soup = BeautifulSoup(self.__response_object.content, 'lxml')
        div = soup.find_all('div')
        for i in div:
            try:
                if i['data-reading-id'] != None:
                    return str(i['data-reading-id'])
            except:
                continue

    def get_image_links(self, params=""):
        r = requests.get(
            f"https://mangareader.to/ajax/image/list/chap/{self.chapter_id}?mode=horizontal&quality=high&hozPageSize=1")
        soup = BeautifulSoup(
            eval(r.text.replace('true', 'True', 1))['html'], 'lxml')
        links = {}
        n = 1
        for i in soup.find_all('div', attrs={'class': 'ds-image'}):
            try:
                links[str(n)] = i['data-url']
            except:
                continue
            n += 1
        return links
