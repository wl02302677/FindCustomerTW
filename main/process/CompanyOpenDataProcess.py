import os

import requests
import yaml
from bs4 import BeautifulSoup


class LevelsfyiCrawler:
    def __init__(self, url, country):
        config_file = '../config/config.yaml'
        if not os.path.exists(config_file):
            raise Exception("There is no configuration file '{}'".format(config_file))
        else:
            with open(config_file) as f:
                config = yaml.safe_load(f)
        self.url = config['level_url']


    def crawler(self):
        response = requests.get(
            "https://www.levels.fyi/Salaries/Software-Engineer/Taiwan/")
        soup = BeautifulSoup(response.text, "html.parser")

        print(soup.prettify())


if __name__ == '__main__':
    country = 'Taiwan'

    crawler = LevelsfyiCrawler(country)
    crawler.crawler()
