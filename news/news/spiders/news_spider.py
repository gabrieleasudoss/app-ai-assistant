import re

import numpy as np
import requests
import scrapy
import unidecode as unidecode
from bs4 import BeautifulSoup
from ..items import NewsItem
import urllib.parse


def parse_full_title(response):
    print('============================================')
    item = NewsItem()
    url = response.meta['url']
    item['url'] = url
    article = requests.get(url)
    article_content = article.content
    soup_article = BeautifulSoup(article_content, 'html.parser')
    author = response.css('.author__name a::text').get()
    tag = response.css('.tag::text').get()
    place = response.css('.grey-text strong::text').get()
    body = soup_article.find_all('div', class_='grey-text')
    full_title = response.css('.title span::text').get()
    item['full_title'] = unidecode.unidecode(full_title)
    short_desc = soup_article.find('p', class_='shortDesc').get_text()
    item['short_desc'] = unidecode.unidecode(short_desc)
    time = soup_article.find('span', class_='posted-on').get_text()
    x = body[0].find_all('p')
    list_paragraphs = []
    for p in np.arange(0, len(x)):
        paragraph = x[p].get_text()
        list_paragraphs.append(paragraph)
        story = " ".join(list_paragraphs).replace("\n", "")
        item['story'] = unidecode.unidecode(" ".join(story.partition(':')[2:]))
    item['author'] = unidecode.unidecode(" ".join(author.split()))
    item['tag'] = tag
    if place is not None:
        item['place'] = " ".join(place.split(':')).strip()
    else:
        item['place'] = 'Not Specified'
    item['time'] = time

    if 'livewire' in url:
        item['url'] = url
        body = soup_article.find_all('div', class_='entry-content')
        full_title = soup_article.find('h1', class_='entry-title').get_text()
        item['full_title'] = unidecode.unidecode(full_title)
        time = soup_article.find('a', rel='bookmark').get_text()
        item['time'] = time
        author = soup_article.find('a', rel='author').get_text()
        item['author'] = unidecode.unidecode(" ".join(author.split()))
        item['short_desc'] = 'Not Specified'
        tag = response.css('.entry-meta a::text').get()
        x = body[0].find_all('p')
        list_paragraphs = []
        for p in np.arange(0, len(x)):
            paragraph = x[p].get_text()
            list_paragraphs.append(paragraph)
            story = " ".join(list_paragraphs).replace("\n", "")
            item['story'] = unidecode.unidecode(" ".join(story.partition(':')[2:]))
            item['author'] = unidecode.unidecode(" ".join(author.split()))
            item['tag'] = tag
            item['place'] = 'Not Specified'
    yield item


class NewsSpider(scrapy.Spider):
    name = 'news'
    start_urls = [
        'https://thewire.in/'
    ]

    def parse(self, response):
        all_div_news = response.css('.tw-container div.card-stacked')
        for news in all_div_news:
            url = news.css('.card__title a::attr(href)').get()
            url = urllib.parse.urljoin('https://thewire.in/', url)
            if url.startswith('https://thewire.in/'):
                yield scrapy.Request(url=url, callback=parse_full_title, meta={'url': url})
