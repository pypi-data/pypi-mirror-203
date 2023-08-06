from bs4 import BeautifulSoup
import requests


class Manga:
    def __init__(self, url) -> None:
        self.url = url
        self.__response_object = requests.get(self.url, timeout=10)

    def get_chapter_links(self):
        soup = BeautifulSoup(self.__response_object.content, 'lxml')
        links = {}
        links['metadata'] = {
            "base_url": 'https://mangareader.to', "chapters": None}
        links['chapter_links'] = {}
        en_ul = soup.find(
            'ul', attrs={'id': 'en-chapters'})
        lines = en_ul.find_all(
            'li', attrs={'class': 'item reading-item chapter-item'})
        n = 0
        for i in lines:
            if i.a['class'] == ['item-link']:
                ch_no = i['data-number']
                link = i.a['href']
                title = i.a['title']
                links["chapter_links"][ch_no] = {"chapter_no": ch_no,
                                                 "title": title, "url": link}
                n += 1
        links['metadata']['chapters'] = str(n)

        return links
